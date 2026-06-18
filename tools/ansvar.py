"""
Ansvar Systems EU Compliance MCP client.
Gateway: https://gateway.ansvar.eu/mcp
Free tier: 50 queries/day
Docs: https://github.com/Ansvar-Systems/EU_compliance_MCP
"""

import json
import urllib.request
import urllib.error

ANSVAR_GATEWAY = "https://gateway.ansvar.eu/mcp"
TIMEOUT = 15


def _call_tool(tool_name: str, arguments: dict) -> dict:
    """Call a tool on the Ansvar MCP gateway via HTTP POST."""
    payload = json.dumps({
        "jsonrpc": "2.0",
        "method": "tools/call",
        "params": {"name": tool_name, "arguments": arguments},
        "id": 1,
    }).encode("utf-8")

    req = urllib.request.Request(
        ANSVAR_GATEWAY,
        data=payload,
        headers={"Content-Type": "application/json"},
        method="POST",
    )

    try:
        with urllib.request.urlopen(req, timeout=TIMEOUT) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except urllib.error.URLError as e:
        return {"error": str(e), "fallback": True}


def lookup_article(article_id: str) -> str:
    """
    Fetch full text of an EU AI Act article from Ansvar.
    article_id examples: "5", "6", "50", "53"
    Returns article text or error message.
    """
    result = _call_tool("get_ai_act_article", {"article": article_id})
    if "error" in result:
        return f"[Ansvar unavailable: {result['error']}]"
    return result.get("result", {}).get("content", [{}])[0].get("text", "No content")


def search_act(query: str) -> str:
    """
    Full-text search across EU AI Act via Ansvar.
    Returns top matching passages.
    """
    result = _call_tool("search_ai_act", {"query": query})
    if "error" in result:
        return f"[Ansvar search unavailable: {result['error']}]"
    return result.get("result", {}).get("content", [{}])[0].get("text", "No results")


def get_obligations_for_role(role: str) -> str:
    """
    Get obligations for a specific role (provider, deployer, importer, etc.)
    """
    result = _call_tool("get_obligations_by_role", {"role": role})
    if "error" in result:
        return f"[Ansvar unavailable: {result['error']}]"
    return result.get("result", {}).get("content", [{}])[0].get("text", "No content")


def get_definition(term: str) -> str:
    """
    Look up a specific definition from Art. 3 (68 definitions).
    """
    result = _call_tool("get_definition", {"term": term})
    if "error" in result:
        return f"[Ansvar unavailable: {result['error']}]"
    return result.get("result", {}).get("content", [{}])[0].get("text", "No content")
