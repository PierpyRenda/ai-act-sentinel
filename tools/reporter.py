"""
Report generator — produces structured compliance report from classifier output.
"""

from datetime import date
from knowledge.sanctions import SANCTION_TIERS


RISK_LEVEL_LABELS = {
    "PROHIBITED": "🔴 PROHIBITED (Art. 5)",
    "HIGH_RISK": "🟠 HIGH RISK (Annex III / Art. 6)",
    "HIGH_RISK_POSSIBLE_EXCEPTION": "🟡 HIGH RISK — POSSIBLE EXCEPTION",
    "LIMITED_RISK": "🟡 LIMITED RISK (Art. 50)",
    "LIMITED_RISK+GPAI": "🟡 LIMITED RISK + GPAI",
    "GPAI": "🔵 GPAI MODEL (Chapter V)",
    "MINIMAL_RISK": "🟢 MINIMAL RISK",
    "OUT_OF_SCOPE": "⚪ OUT OF SCOPE",
}

RISK_LEVEL_DESCRIPTIONS = {
    "PROHIBITED": "The AI system is prohibited under EU law. It cannot be placed on the market or put into service in the EU.",
    "HIGH_RISK": "The AI system falls under a high-risk category. Full Chapter III requirements are mandatory.",
    "HIGH_RISK_POSSIBLE_EXCEPTION": "The system may fall under Annex III but could qualify for the exception (procedural tasks only). Legal review required.",
    "LIMITED_RISK": "The system requires transparency obligations only (Art. 50): disclosure, watermarking, labeling.",
    "LIMITED_RISK+GPAI": "The system has transparency obligations (Art. 50) AND GPAI model obligations (Chapter V).",
    "GPAI": "The system is a General Purpose AI model. Chapter V obligations apply.",
    "MINIMAL_RISK": "No mandatory obligations. Voluntary codes of practice (Art. 95) are encouraged.",
    "OUT_OF_SCOPE": "The system appears to be outside the scope of the EU AI Act.",
}


def _get_max_penalty(risk_level: str) -> str | None:
    if risk_level == "PROHIBITED":
        return "€35,000,000 or 7% of worldwide annual turnover"
    if risk_level in ("HIGH_RISK", "HIGH_RISK_POSSIBLE_EXCEPTION", "LIMITED_RISK", "LIMITED_RISK+GPAI"):
        return "€15,000,000 or 3% of worldwide annual turnover"
    if risk_level == "GPAI":
        return "€15,000,000 or 3% of worldwide annual turnover (Art. 101)"
    return None


def generate_report(classification_result: dict, source: str = "input text", roles: list[str] = None) -> str:
    """Generate a structured EU AI Act compliance report from classifier output."""
    risk_level = classification_result.get("risk_level", "UNKNOWN")
    findings = classification_result.get("findings", [])
    obligations = classification_result.get("obligations", [])
    violated_articles = classification_result.get("violated_articles", [])
    summary = classification_result.get("summary", "")

    label = RISK_LEVEL_LABELS.get(risk_level, risk_level)
    description = RISK_LEVEL_DESCRIPTIONS.get(risk_level, "")
    penalty = _get_max_penalty(risk_level)

    lines = [
        "=" * 70,
        "AI ACT SENTINEL — COMPLIANCE REPORT",
        f"Analysis date: {date.today().isoformat()}",
        f"Source: {source}",
        "=" * 70,
        "",
        f"RISK LEVEL: {label}",
        "",
        f"DESCRIPTION: {description}",
        "",
    ]

    if summary:
        lines += [f"SUMMARY: {summary}", ""]

    if penalty:
        lines += [f"MAXIMUM PENALTY: {penalty}", ""]

    if violated_articles:
        lines += ["POTENTIALLY VIOLATED ARTICLES:"]
        for art in violated_articles:
            lines.append(f"  • {art}")
        lines.append("")

    if findings:
        lines += ["ISSUES DETECTED:"]
        for i, finding in enumerate(findings, 1):
            if isinstance(finding, dict):
                name = finding.get("name") or finding.get("practice") or finding.get("category") or finding.get("rule") or finding.get("type", "Issue")
                article = finding.get("article", "")
                matched = finding.get("matched_keywords", [])
                lines.append(f"  {i}. {name}" + (f" ({article})" if article else ""))
                if matched:
                    lines.append(f"     Matched keywords: {', '.join(matched[:5])}")
                obligation = finding.get("obligation") or finding.get("description", "")
                if obligation:
                    lines.append(f"     Obligation: {obligation}")
        lines.append("")

    if obligations:
        lines += ["APPLICABLE OBLIGATIONS:"]
        for ob in obligations:
            lines.append(f"  ✓ {ob}")
        lines.append("")

    if roles:
        lines += [f"DETECTED ROLES: {', '.join(roles)}", ""]

    lines += ["RECOMMENDATIONS:"]
    if risk_level == "PROHIBITED":
        lines.append("  ⛔ Immediately stop development/deployment in the EU.")
        lines.append("  ⛔ Consult a legal professional specializing in EU AI law before any action.")
    elif risk_level in ("HIGH_RISK", "HIGH_RISK_POSSIBLE_EXCEPTION"):
        lines.append("  1. Implement a risk management system (Art. 9)")
        lines.append("  2. Prepare complete technical documentation (Art. 11, Annex IV)")
        lines.append("  3. Conduct conformity assessment (Art. 43)")
        lines.append("  4. Register in the EU database (Art. 49) before deployment")
        lines.append("  5. Consult a qualified legal professional for final assessment")
    elif "LIMITED_RISK" in risk_level:
        lines.append("  1. Disclose AI interaction to users (Art. 50(1)) where humans interact directly")
        lines.append("  2. Apply C2PA watermark to AI-generated content (Art. 50(2))")
        lines.append("  3. Label deepfakes and synthetic content (Art. 50(4))")
    elif risk_level == "GPAI":
        lines.append("  1. Prepare technical documentation (Annex XI-XII)")
        lines.append("  2. Publish training data summary (Art. 53(1)(d))")
        lines.append("  3. Implement EU copyright compliance policy (Art. 53(1)(c))")
        lines.append("  4. If >10^25 FLOPs: notify the Commission (Art. 51) and apply Art. 55")
    else:
        lines.append("  ✅ No mandatory obligations. Consider voluntary codes of practice (Art. 95).")

    lines += [
        "",
        "─" * 70,
        "DISCLAIMER: This report is auto-generated for informational purposes only.",
        "It does not constitute legal advice. For compliance decisions consult a qualified",
        "legal professional specializing in Regulation (EU) 2024/1689.",
        "Regulatory basis: EU AI Act (Reg. EU 2024/1689) + AI Omnibus (May 2026)",
        "─" * 70,
    ]

    return "\n".join(lines)
