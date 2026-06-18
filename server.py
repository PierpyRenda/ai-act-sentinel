"""
AI Act Sentinel — MCP Server
Exposes EU AI Act compliance tools to Claude via Model Context Protocol.

Tools:
  - analyze_pdf        : Analyze a PDF project document for compliance
  - classify_text      : Classify any text description
  - lookup_article     : Fetch article text from Ansvar gateway
  - search_act         : Full-text search across EU AI Act
  - get_obligations    : Get obligations for a role
  - generate_report    : Generate full compliance report from raw description
"""

import json
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from tools.classifier import classify
from tools.reporter import generate_report
from tools.pdf_analyzer import analyze_pdf as _analyze_pdf
from tools.ansvar import lookup_article, search_act, get_obligations_for_role
from knowledge.roles import detect_role_from_description


TOOLS = [
    {
        "name": "analyze_pdf",
        "description": "Analyze a PDF project document against EU AI Act 2024/1689 (updated 2026). "
                       "Returns risk level, violated articles, obligations, and remediation steps in Italian.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "pdf_path": {
                    "type": "string",
                    "description": "Absolute path to the PDF file to analyze.",
                },
            },
            "required": ["pdf_path"],
        },
    },
    {
        "name": "classify_text",
        "description": "Classify a text description of an AI system against EU AI Act risk levels. "
                       "Returns: PROHIBITED / HIGH_RISK / LIMITED_RISK / GPAI / MINIMAL_RISK.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "description": {
                    "type": "string",
                    "description": "Natural language description of the AI system (any language).",
                },
                "generate_full_report": {
                    "type": "boolean",
                    "description": "If true, returns a full formatted compliance report. Default: false.",
                    "default": False,
                },
            },
            "required": ["description"],
        },
    },
    {
        "name": "lookup_article",
        "description": "Fetch the full text of a specific EU AI Act article from the Ansvar gateway.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "article_id": {
                    "type": "string",
                    "description": "Article number, e.g. '5', '6', '50', '53'.",
                },
            },
            "required": ["article_id"],
        },
    },
    {
        "name": "search_act",
        "description": "Full-text search across EU AI Act articles and recitals via Ansvar gateway.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "query": {
                    "type": "string",
                    "description": "Search query in any language.",
                },
            },
            "required": ["query"],
        },
    },
    {
        "name": "get_obligations",
        "description": "Get the complete list of EU AI Act obligations for a specific operator role.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "role": {
                    "type": "string",
                    "enum": ["provider", "deployer", "importer", "distributor", "authorized_representative", "product_manufacturer"],
                    "description": "The operator role to get obligations for.",
                },
            },
            "required": ["role"],
        },
    },
    {
        "name": "generate_report",
        "description": "Generate a complete structured EU AI Act compliance report for a project description.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "description": {
                    "type": "string",
                    "description": "Full project description (can be multi-paragraph).",
                },
                "source": {
                    "type": "string",
                    "description": "Source label for the report (e.g. filename, project name).",
                    "default": "input",
                },
            },
            "required": ["description"],
        },
    },
]


def handle_tool_call(tool_name: str, arguments: dict) -> str:
    if tool_name == "analyze_pdf":
        pdf_path = arguments["pdf_path"]
        pdf_data = _analyze_pdf(pdf_path)
        description = pdf_data["description"]
        roles = detect_role_from_description(description)
        result = classify(description)
        report = generate_report(result, source=os.path.basename(pdf_path), roles=roles)
        return report

    elif tool_name == "classify_text":
        description = arguments["description"]
        result = classify(description)
        if arguments.get("generate_full_report", False):
            roles = detect_role_from_description(description)
            return generate_report(result, source="text input", roles=roles)
        return json.dumps(result, ensure_ascii=False, indent=2)

    elif tool_name == "lookup_article":
        return lookup_article(arguments["article_id"])

    elif tool_name == "search_act":
        return search_act(arguments["query"])

    elif tool_name == "get_obligations":
        return get_obligations_for_role(arguments["role"])

    elif tool_name == "generate_report":
        description = arguments["description"]
        source = arguments.get("source", "input")
        roles = detect_role_from_description(description)
        result = classify(description)
        return generate_report(result, source=source, roles=roles)

    else:
        return f"Unknown tool: {tool_name}"


def run_stdio():
    """Run MCP server over stdio (JSON-RPC 2.0)."""
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        try:
            request = json.loads(line)
        except json.JSONDecodeError:
            continue

        method = request.get("method")
        req_id = request.get("id")
        params = request.get("params", {})

        if method == "initialize":
            response = {
                "jsonrpc": "2.0",
                "id": req_id,
                "result": {
                    "protocolVersion": "2024-11-05",
                    "capabilities": {"tools": {}},
                    "serverInfo": {"name": "ai-act-sentinel", "version": "1.0.0"},
                },
            }

        elif method == "tools/list":
            response = {"jsonrpc": "2.0", "id": req_id, "result": {"tools": TOOLS}}

        elif method == "tools/call":
            tool_name = params.get("name")
            arguments = params.get("arguments", {})
            try:
                content = handle_tool_call(tool_name, arguments)
                response = {
                    "jsonrpc": "2.0",
                    "id": req_id,
                    "result": {"content": [{"type": "text", "text": content}]},
                }
            except Exception as e:
                response = {
                    "jsonrpc": "2.0",
                    "id": req_id,
                    "error": {"code": -32603, "message": str(e)},
                }

        else:
            response = {
                "jsonrpc": "2.0",
                "id": req_id,
                "error": {"code": -32601, "message": f"Method not found: {method}"},
            }

        print(json.dumps(response), flush=True)


if __name__ == "__main__":
    run_stdio()
