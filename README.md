# AI Act Sentinel 🛡️

> MCP server for EU AI Act compliance analysis — classify any AI system or workflow against Regulation (EU) 2024/1689, updated with AI Omnibus 2026.

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)
[![EU AI Act](https://img.shields.io/badge/EU%20AI%20Act-2024%2F1689-navy)](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R1689)
[![MCP](https://img.shields.io/badge/MCP-compatible-orange)](https://modelcontextprotocol.io)
[![Last Updated](https://img.shields.io/badge/Updated-June%202026-brightgreen)](https://github.com/PierpyRenda/ai-act-sentinel)

Pass a PDF project document or plain text description — get back a structured Italian compliance report: **risk level, violated articles, operator obligations, and remediation steps**.

---

## Why AI Act Sentinel?

The EU AI Act (Reg. EU 2024/1689) is the world's first comprehensive AI regulation. With the main deadline on **2 August 2026** and fines up to **€35 million or 7% of worldwide turnover**, understanding your compliance position is not optional.

Existing tools either:
- Cover only ~30% of the Act (outdated repos from late 2024)
- Require expensive legal consultations for every new workflow
- Provide no automated pipeline integration

AI Act Sentinel runs **locally as an MCP server**, integrates directly with Claude Code, and fires automatically every time you build or modify an AI system.

---

## Features

- 🔴 **Prohibited practice detection** — all 10 Art. 5 cases including AI Omnibus 2026 (NCII + CSAM)
- 🟠 **High-risk classification** — all 8 Annex III categories + Annex I safety components
- 🟡 **Transparency obligations** — all 5 Art. 50 rules (chatbot disclosure, C2PA watermarking, deepfake labeling)
- 🔵 **GPAI model detection** — Chapter V obligations + systemic risk threshold (10²⁵ FLOPs)
- 📄 **PDF project analysis** — extract text from any project document and run full compliance check
- 👤 **Role-aware reports** — obligations differ by role (provider, deployer, importer, distributor…)
- 🔗 **Ansvar integration** — optional live article lookup via [Ansvar Systems EU Compliance MCP](https://github.com/Ansvar-Systems/EU_compliance_MCP) gateway
- 🇮🇹 **Italian reports** — structured output in Italian with article citations and remediation steps

---

## Risk Levels

| Level | Trigger | Max Penalty |
|-------|---------|-------------|
| 🔴 **PROHIBITED** | Art. 5 violation | €35M or 7% worldwide turnover |
| 🟠 **HIGH_RISK** | Annex III or Annex I safety component | €15M or 3% worldwide turnover |
| 🟡 **LIMITED_RISK** | Art. 50 transparency obligations only | €15M or 3% worldwide turnover |
| 🔵 **GPAI** | General Purpose AI model (Chapter V) | €15M or 3% worldwide turnover |
| 🟢 **MINIMAL_RISK** | No mandatory obligations | — |
| ⚪ **OUT_OF_SCOPE** | Military / personal / pre-commercial R&D | — |

---

## Coverage

| Chapter | Articles | Status |
|---------|----------|--------|
| Ch. II — Prohibited Practices | Art. 5 (10 cases incl. Omnibus 2026) | ✅ Complete |
| Ch. III — High-Risk Systems | Art. 6, Annex III (8 categories) | ✅ Complete |
| Ch. IV — Transparency | Art. 50 (5 rules) | ✅ Complete |
| Ch. V — GPAI Models | Art. 51-55, systemic risk | ✅ Complete |
| Ch. XI-XIII — Sanctions | Art. 99-101 | ✅ Complete |
| Roles & Obligations | 6 operator roles | ✅ Complete |
| Implementation Timeline | 2024-2031 | ✅ Complete |

---

## MCP Tools

| Tool | Description |
|------|-------------|
| `analyze_pdf` | Analyze a PDF project document — full compliance pipeline |
| `classify_text` | Classify any text description against the Act |
| `generate_report` | Generate full Italian compliance report |
| `lookup_article` | Fetch article text from Ansvar gateway |
| `search_act` | Full-text search across EU AI Act |
| `get_obligations` | Get obligations by operator role |

---

## Installation

### Prerequisites

```bash
pip install pymupdf
```

### Add to Claude Code (MCP config)

Add to `~/.mcp.json` or `~/Orchestrator/.mcp.json`:

```json
{
  "mcpServers": {
    "ai-act-sentinel": {
      "command": "python3",
      "args": ["/path/to/ai-act-sentinel/server.py"]
    }
  }
}
```

Restart Claude Code. The 6 tools will be available in your session.

---

## Usage

### Analyze a PDF project

```
analyze_pdf(pdf_path="/path/to/your/project.pdf")
```

### Classify a text description

```
classify_text(
  description="Sistema di recruitment AI con filtraggio automatico CV e ranking candidati",
  generate_full_report=True
)
```

### Quick Python test

```bash
cd ai-act-sentinel
python3 -c "
from tools.classifier import classify
from tools.reporter import generate_report

desc = 'Sistema AI per valutare creditworthiness di persone fisiche per mutui bancari'
result = classify(desc)
print(generate_report(result, source='test'))
"
```

### Sample output

```
======================================================================
AI ACT SENTINEL — RAPPORTO DI CONFORMITÀ
Data analisi: 2026-06-18
Fonte: test
======================================================================

LIVELLO DI RISCHIO: 🟠 ALTO RISCHIO (Annex III / Art. 6)

DESCRIZIONE: Il sistema AI rientra nelle categorie ad alto rischio.
Sono obbligatori requisiti completi del Capitolo III.

SINTESI: System matches 1 Annex III high-risk category.

SANZIONE MASSIMA: €15.000.000 o 3% del fatturato mondiale annuo

ARTICOLI POTENZIALMENTE VIOLATI:
  • Annex III(5)

PROBLEMI RILEVATI:
  1. 5. Essential Public & Private Services (Annex III(5))
     Keywords trovate: creditworthiness, persone fisiche, mutui

OBBLIGHI APPLICABILI:
  ✓ Art. 9 — Risk management system
  ✓ Art. 10 — Data governance
  ✓ Art. 11 — Technical documentation
  ✓ Art. 43 — Conformity assessment
  ✓ Art. 49 — EU database registration
  ...

RACCOMANDAZIONI:
  1. Implementare un sistema di gestione del rischio (Art. 9)
  2. Predisporre documentazione tecnica completa (Art. 11)
  3. Effettuare valutazione di conformità (Art. 43)
  4. Registrarsi nel database UE (Art. 49) prima del deployment
```

---

## Project Structure

```
ai-act-sentinel/
├── server.py                    # MCP server — JSON-RPC 2.0 over stdio
├── knowledge/
│   ├── prohibited.py            # Art. 5 — 10 prohibited practices
│   ├── annex_iii.py             # Annex III — 8 high-risk categories
│   ├── transparency.py          # Art. 50 — 5 transparency rules
│   ├── gpai.py                  # Chapter V — GPAI + systemic risk
│   ├── roles.py                 # 6 operator roles + obligations matrix
│   └── sanctions.py             # Art. 99-101 sanction tiers
├── tools/
│   ├── classifier.py            # 6-question decision tree (Q1→Q6)
│   ├── reporter.py              # Italian report generator
│   ├── pdf_analyzer.py          # PDF text extraction (PyMuPDF)
│   └── ansvar.py                # HTTP client → gateway.ansvar.eu/mcp
└── requirements.txt
```

### Classification Decision Tree

```
Q1: In scope? (not military / personal / pre-commercial)
Q2: Art. 5 prohibited practice? → PROHIBITED (stop)
Q3: Annex III use case? → HIGH_RISK (or exception if only procedural + no profiling)
Q4: Annex I safety component? → HIGH_RISK Art. 6(1)
Q5: Art. 50 trigger? (chatbot / synthetic content / emotion / deepfake) → LIMITED_RISK
Q6: GPAI model? → Chapter V obligations (+ Art. 55 if >10²⁵ FLOPs)
→ else: MINIMAL_RISK
```

---

## Key Deadlines

| Date | What enters into force |
|------|------------------------|
| ✅ 2 Feb 2025 | Art. 5 prohibited practices + AI literacy (Art. 4) |
| ✅ 2 Aug 2025 | GPAI obligations (Ch. V) + governance + sanctions |
| ⚠️ **2 Aug 2026** | **Everything else**: high-risk, Art. 50, deployer obligations, EU DB registration |
| 2 Aug 2027 | Art. 6(1) Annex I products + pre-2025 GPAI compliance |
| 7 May 2026 | AI Omnibus: NCII/CSAM prohibitions, SME relief, EU sandboxes |

---

## External Data Layer

For live article lookups, AI Act Sentinel integrates with **[Ansvar Systems EU Compliance MCP](https://github.com/Ansvar-Systems/EU_compliance_MCP)**:

- 126 AI Act articles, 68 definitions, 181 recitals
- Updated daily from EUR-Lex
- 50 free queries/day at `https://gateway.ansvar.eu/mcp`
- Graceful fallback to local knowledge if gateway is unavailable

---

## Auto-Trigger Integration

When used with Claude Code and the provided `CLAUDE.md` configuration, AI Act Sentinel fires automatically:

- Every time you create or modify an N8N / Make workflow
- Every time you build an AI-powered application
- Every time you describe a system that processes personal data with ML
- When you pass a PDF project document for review

Behavior by risk level:
- **PROHIBITED** → Claude stops and refuses to deploy
- **HIGH_RISK** → Report shown, user confirmation required before deploy
- **LIMITED_RISK** → Art. 50 disclosures added to system design automatically

---

## Privacy

AI Act Sentinel is designed to be **private by default**:

- 🖥️ **Runs entirely on your machine** — it's a local MCP server. Your project documents and descriptions never leave your computer for processing.
- 🔑 **No API keys required** — the classifier and report generator need no credentials and read no environment secrets.
- 🚫 **No data collection, no telemetry** — nothing is logged to or sent to the author or any analytics service.
- 🔗 **One optional external call** — only the `lookup_article` / `search_act` tools may contact the public [Ansvar Systems](https://github.com/Ansvar-Systems/EU_compliance_MCP) gateway (`gateway.ansvar.eu`) for live article text. Only the article ID or query *you* request is sent, from *your* machine. If the gateway is unavailable, it falls back to the bundled local knowledge base — so the tool works fully offline too.

---

## Disclaimer

AI Act Sentinel is an **automated compliance screening tool** for informational purposes only. It does not constitute legal advice. For deployment decisions involving high-risk AI systems, consult a qualified legal professional specializing in EU AI regulation.

Regulatory basis: **Regulation (EU) 2024/1689** (EU AI Act) as amended by **AI Omnibus (May 2026)**. Last knowledge update: **June 2026**.

---

## License

MIT — see [LICENSE](LICENSE)

---

*Built with ❤️ for the EU AI compliance ecosystem.*
