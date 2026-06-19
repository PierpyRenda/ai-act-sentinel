"""
Risk classifier — implements the 6-question compliance checker decision tree.
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from knowledge.prohibited import PROHIBITED_PRACTICES
from knowledge.annex_iii import ANNEX_III_CATEGORIES, EXCEPTION_KEYWORDS
from knowledge.transparency import TRANSPARENCY_RULES
from knowledge.gpai import GPAI_INDICATORS, GPAI_UNIVERSAL_OBLIGATIONS, SYSTEMIC_RISK_ADDITIONAL_OBLIGATIONS


EXCLUDED_CONTEXTS = [
    "military", "militare", "national security", "sicurezza nazionale",
    "personal non-professional", "uso personale", "research pre-commercial", "ricerca pre-commerciale",
]


def _keyword_match(text: str, keywords: list[str]) -> list[str]:
    text_lower = text.lower()
    return [kw for kw in keywords if kw.lower() in text_lower]


def classify(description: str) -> dict:
    """
    Classify an AI system description against EU AI Act risk categories.
    Returns structured result with risk_level, findings, and obligations.
    """
    text = description.lower()
    findings = []
    violated_articles = []

    # Q1 — Scope check
    excluded_matches = _keyword_match(text, EXCLUDED_CONTEXTS)
    if excluded_matches:
        return {
            "risk_level": "OUT_OF_SCOPE",
            "summary": f"System appears to be out of EU AI Act scope: {excluded_matches}",
            "findings": [],
            "violated_articles": [],
            "obligations": [],
        }

    # Q2 — Art. 5 prohibited practices check
    prohibited_hits = []
    for practice in PROHIBITED_PRACTICES:
        matches = _keyword_match(text, practice["keywords"])
        if matches:
            prohibited_hits.append({
                "practice": practice["name"],
                "article": practice["article"],
                "matched_keywords": matches,
                "description": practice["description"],
            })
            violated_articles.append(practice["article"])

    if prohibited_hits:
        return {
            "risk_level": "PROHIBITED",
            "summary": f"System matches {len(prohibited_hits)} PROHIBITED practice(s) under Art. 5.",
            "findings": prohibited_hits,
            "violated_articles": violated_articles,
            "obligations": ["STOP — system cannot be placed on market or put into service in the EU."],
            "max_penalty": "€35M or 7% worldwide annual turnover",
        }

    # Q3 — Annex III high-risk check
    annex3_hits = []
    exception_matches = _keyword_match(text, EXCEPTION_KEYWORDS)
    for category in ANNEX_III_CATEGORIES:
        matches = _keyword_match(text, category["keywords"])
        if matches:
            annex3_hits.append({
                "category": category["category"],
                "article": category["article"],
                "matched_keywords": matches,
                "use_cases": category["use_cases"],
            })
            violated_articles.append(category["article"])

    if annex3_hits:
        if exception_matches and not _keyword_match(text, ["profiling", "profilag"]):
            findings.append({
                "type": "potential_annex3_exception",
                "note": f"Annex III match found BUT exception keywords present ({exception_matches}). "
                        "Must document that system only performs preparatory/procedural tasks without profiling.",
                "categories": annex3_hits,
            })
            return {
                "risk_level": "HIGH_RISK_POSSIBLE_EXCEPTION",
                "summary": "System matches Annex III but may qualify for exception. Legal review required.",
                "findings": findings,
                "violated_articles": violated_articles,
                "obligations": _get_high_risk_obligations(),
            }

        return {
            "risk_level": "HIGH_RISK",
            "summary": f"System matches {len(annex3_hits)} Annex III high-risk category/ies.",
            "findings": annex3_hits,
            "violated_articles": violated_articles,
            "obligations": _get_high_risk_obligations(),
            "max_penalty": "€15M or 3% worldwide annual turnover",
        }

    # Q4 — Art. 6(1) Annex I safety component (keyword heuristic)
    annex1_keywords = ["safety component", "componente di sicurezza", "ce marking", "marcatura ce",
                       "machinery regulation", "medical device", "dispositivo medico", "aeronautica", "aviation"]
    annex1_matches = _keyword_match(text, annex1_keywords)
    if annex1_matches:
        return {
            "risk_level": "HIGH_RISK",
            "summary": "System appears to be a safety component of an Annex I product (Art. 6(1)).",
            "findings": [{"type": "annex1_safety_component", "matched_keywords": annex1_matches}],
            "violated_articles": ["Art. 6(1)"],
            "obligations": _get_high_risk_obligations(),
            "note": "Requires third-party conformity assessment (Annex VII).",
        }

    # Q5 — Art. 50 transparency (Limited-Risk)
    transparency_hits = []
    for rule in TRANSPARENCY_RULES:
        matches = _keyword_match(text, rule["keywords"])
        if matches:
            transparency_hits.append({
                "rule": rule["name"],
                "article": rule["article"],
                "matched_keywords": matches,
                "obligation": rule["obligation"],
            })
            violated_articles.append(rule["article"])

    # Q6 — GPAI check (can stack with other classifications)
    gpai_matches = _keyword_match(text, GPAI_INDICATORS)
    gpai_result = None
    if gpai_matches:
        gpai_result = {
            "type": "gpai",
            "matched_keywords": gpai_matches,
            "obligations": GPAI_UNIVERSAL_OBLIGATIONS,
            "note": "If training compute > 10^25 FLOPs, systemic risk obligations (Art. 55) also apply.",
        }

    if transparency_hits:
        findings = transparency_hits[:]
        if gpai_result:
            findings.append(gpai_result)
        return {
            "risk_level": "LIMITED_RISK" if not gpai_result else "LIMITED_RISK+GPAI",
            "summary": "System triggers Art. 50 transparency obligations"
                       + (" and GPAI Chapter V obligations." if gpai_result else "."),
            "findings": findings,
            "violated_articles": violated_articles,
            "obligations": [f["obligation"] for f in transparency_hits],
        }

    if gpai_result:
        return {
            "risk_level": "GPAI",
            "summary": "System is a General Purpose AI model — Chapter V obligations apply.",
            "findings": [gpai_result],
            "violated_articles": ["Art. 53"],
            "obligations": [o["description"] for o in GPAI_UNIVERSAL_OBLIGATIONS],
        }

    # Minimal risk
    return {
        "risk_level": "MINIMAL_RISK",
        "summary": "No mandatory obligations detected. Voluntary codes of practice (Art. 95) encouraged.",
        "findings": [],
        "violated_articles": [],
        "obligations": [],
    }


def _get_high_risk_obligations() -> list[str]:
    return [
        "Art. 9 — Risk management system (identify, estimate, analyze, mitigate)",
        "Art. 10 — Data governance (relevant, representative, error-free datasets)",
        "Art. 11 — Technical documentation (before market, Annex IV)",
        "Art. 12 — Automatic logging",
        "Art. 13 — Transparency for deployers",
        "Art. 14 — Human oversight measures",
        "Art. 15 — Accuracy, robustness, cybersecurity",
        "Art. 16 — 12 provider obligations (CE marking, QMS, conformity assessment, registration)",
        "Art. 43 — Conformity assessment",
        "Art. 49 — EU database registration",
    ]
