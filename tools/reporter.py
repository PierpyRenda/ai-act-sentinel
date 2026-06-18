"""
Report generator — produces structured compliance report from classifier output.
"""

from datetime import date
from knowledge.sanctions import SANCTION_TIERS


RISK_LEVEL_LABELS = {
    "PROHIBITED": "🔴 VIETATO (Art. 5)",
    "HIGH_RISK": "🟠 ALTO RISCHIO (Annex III / Art. 6)",
    "HIGH_RISK_POSSIBLE_EXCEPTION": "🟡 ALTO RISCHIO — POSSIBILE ECCEZIONE",
    "LIMITED_RISK": "🟡 RISCHIO LIMITATO (Art. 50)",
    "LIMITED_RISK+GPAI": "🟡 RISCHIO LIMITATO + GPAI",
    "GPAI": "🔵 MODELLO GPAI (Chapter V)",
    "MINIMAL_RISK": "🟢 RISCHIO MINIMO",
    "OUT_OF_SCOPE": "⚪ FUORI AMBITO",
}

RISK_LEVEL_DESCRIPTIONS = {
    "PROHIBITED": "Il sistema AI è vietato dalla normativa UE. Non può essere immesso sul mercato né messo in servizio nell'UE.",
    "HIGH_RISK": "Il sistema AI rientra nelle categorie ad alto rischio. Sono obbligatori requisiti completi del Capitolo III.",
    "HIGH_RISK_POSSIBLE_EXCEPTION": "Il sistema potrebbe rientrare in Annex III ma potrebbe qualificarsi per l'eccezione (solo compiti procedurali). Necessaria verifica legale.",
    "LIMITED_RISK": "Il sistema richiede solo obblighi di trasparenza (Art. 50): disclosure, watermark, etichettatura.",
    "LIMITED_RISK+GPAI": "Il sistema ha obblighi di trasparenza (Art. 50) E obblighi come modello GPAI (Chapter V).",
    "GPAI": "Il sistema è un modello di IA per uso generale. Si applicano gli obblighi del Capitolo V.",
    "MINIMAL_RISK": "Nessun obbligo obbligatorio. Codici di condotta volontari (Art. 95) raccomandati.",
    "OUT_OF_SCOPE": "Il sistema sembra fuori dall'ambito del Regolamento UE sull'IA.",
}


def _get_max_penalty(risk_level: str) -> str | None:
    if risk_level == "PROHIBITED":
        return "€35.000.000 o 7% del fatturato mondiale annuo"
    if risk_level in ("HIGH_RISK", "HIGH_RISK_POSSIBLE_EXCEPTION", "LIMITED_RISK", "LIMITED_RISK+GPAI"):
        return "€15.000.000 o 3% del fatturato mondiale annuo"
    if risk_level == "GPAI":
        return "€15.000.000 o 3% del fatturato mondiale annuo (Art. 101)"
    return None


def generate_report(classification_result: dict, source: str = "input text", roles: list[str] = None) -> str:
    """
    Generate a human-readable Italian compliance report from classifier output.
    """
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
        "AI ACT SENTINEL — RAPPORTO DI CONFORMITÀ",
        f"Data analisi: {date.today().isoformat()}",
        f"Fonte: {source}",
        "=" * 70,
        "",
        f"LIVELLO DI RISCHIO: {label}",
        "",
        f"DESCRIZIONE: {description}",
        "",
    ]

    if summary:
        lines += [f"SINTESI: {summary}", ""]

    if penalty:
        lines += [f"SANZIONE MASSIMA: {penalty}", ""]

    if violated_articles:
        lines += ["ARTICOLI POTENZIALMENTE VIOLATI:"]
        for art in violated_articles:
            lines.append(f"  • {art}")
        lines.append("")

    if findings:
        lines += ["PROBLEMI RILEVATI:"]
        for i, finding in enumerate(findings, 1):
            if isinstance(finding, dict):
                name = finding.get("name") or finding.get("practice") or finding.get("category") or finding.get("rule") or finding.get("type", "Issue")
                article = finding.get("article", "")
                matched = finding.get("matched_keywords", [])
                lines.append(f"  {i}. {name}" + (f" ({article})" if article else ""))
                if matched:
                    lines.append(f"     Keywords trovate: {', '.join(matched[:5])}")
                obligation = finding.get("obligation") or finding.get("description", "")
                if obligation:
                    lines.append(f"     Obbligo: {obligation}")
        lines.append("")

    if obligations:
        lines += ["OBBLIGHI APPLICABILI:"]
        for ob in obligations:
            lines.append(f"  ✓ {ob}")
        lines.append("")

    if roles:
        lines += [f"RUOLI RILEVATI: {', '.join(roles)}", ""]

    # Recommendations
    lines += ["RACCOMANDAZIONI:"]
    if risk_level == "PROHIBITED":
        lines.append("  ⛔ Interrompere immediatamente lo sviluppo/deployment nell'UE.")
        lines.append("  ⛔ Consultare un avvocato specializzato in diritto AI prima di qualsiasi azione.")
    elif risk_level in ("HIGH_RISK", "HIGH_RISK_POSSIBLE_EXCEPTION"):
        lines.append("  1. Implementare un sistema di gestione del rischio (Art. 9)")
        lines.append("  2. Predisporre documentazione tecnica completa (Art. 11)")
        lines.append("  3. Effettuare valutazione di conformità (Art. 43)")
        lines.append("  4. Registrarsi nel database UE (Art. 49) prima del deployment")
        lines.append("  5. Consultare un legale specializzato per la valutazione finale")
    elif "LIMITED_RISK" in risk_level:
        lines.append("  1. Implementare disclosure all'utente (Art. 50(1)) se c'è interazione umana")
        lines.append("  2. Applicare watermark C2PA ai contenuti generati (Art. 50(2))")
        lines.append("  3. Etichettare deepfake/contenuti sintetici (Art. 50(4))")
    elif risk_level == "GPAI":
        lines.append("  1. Preparare documentazione tecnica (Annex XI-XII)")
        lines.append("  2. Pubblicare sommario dei dati di training (Art. 53(1)(d))")
        lines.append("  3. Implementare policy copyright (Art. 53(1)(c))")
        lines.append("  4. Se >10^25 FLOPs: notificare la Commissione (Art. 51) e applicare Art. 55")
    else:
        lines.append("  ✅ Nessun obbligo obbligatorio. Considerare codici di condotta volontari (Art. 95).")

    lines += [
        "",
        "─" * 70,
        "DISCLAIMER: Questo rapporto è generato automaticamente a scopo informativo.",
        "Non costituisce parere legale. Per decisioni di compliance consultare un avvocato",
        "specializzato nel Regolamento UE sull'Intelligenza Artificiale.",
        "Fonte normativa: Regolamento (UE) 2024/1689 + AI Omnibus (maggio 2026)",
        "─" * 70,
    ]

    return "\n".join(lines)
