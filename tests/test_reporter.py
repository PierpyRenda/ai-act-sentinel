import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pytest
from tools.reporter import generate_report

PROHIBITED = {
    "risk_level": "PROHIBITED",
    "summary": "System matches 1 PROHIBITED practice(s) under Art. 5.",
    "findings": [{"practice": "Social scoring", "article": "Art. 5(1)(c)", "matched_keywords": ["scoring"], "description": "Scores citizens."}],
    "violated_articles": ["Art. 5(1)(c)"],
    "obligations": ["STOP — system cannot be placed on market or put into service in the EU."],
}

HIGH_RISK = {
    "risk_level": "HIGH_RISK",
    "summary": "System matches 1 Annex III high-risk category.",
    "findings": [{"category": "Employment (Annex III(4))", "article": "Annex III(4)", "matched_keywords": ["cv", "recruitment"], "use_cases": []}],
    "violated_articles": ["Annex III(4)"],
    "obligations": [
        "Art. 9 — Risk management system",
        "Art. 11 — Technical documentation",
        "Art. 43 — Conformity assessment",
        "Art. 49 — EU database registration",
    ],
}

LIMITED_RISK = {
    "risk_level": "LIMITED_RISK",
    "summary": "System triggers Art. 50 transparency obligations.",
    "findings": [{"rule": "Chatbot disclosure", "article": "Art. 50(1)", "matched_keywords": ["chatbot"], "obligation": "Inform users they are interacting with an AI."}],
    "violated_articles": ["Art. 50(1)"],
    "obligations": ["Inform users they are interacting with an AI."],
}

GPAI = {
    "risk_level": "GPAI",
    "summary": "System is a General Purpose AI model.",
    "findings": [{"type": "gpai", "matched_keywords": ["llm"], "obligations": [], "note": "..."}],
    "violated_articles": ["Art. 53"],
    "obligations": ["Technical documentation (Annex XI-XII)", "Training data summary (Art. 53(1)(d))"],
}

MINIMAL = {
    "risk_level": "MINIMAL_RISK",
    "summary": "No mandatory obligations.",
    "findings": [],
    "violated_articles": [],
    "obligations": [],
}


def test_report_has_header():
    report = generate_report(MINIMAL)
    assert "AI ACT SENTINEL" in report
    assert "COMPLIANCE REPORT" in report

def test_report_has_date():
    from datetime import date
    report = generate_report(MINIMAL)
    assert date.today().isoformat() in report

def test_report_has_disclaimer():
    report = generate_report(MINIMAL)
    assert "DISCLAIMER" in report
    assert "2024/1689" in report

def test_report_prohibited_stop_instruction():
    report = generate_report(PROHIBITED)
    assert "⛔" in report
    assert "35,000,000" in report

def test_report_prohibited_label():
    report = generate_report(PROHIBITED)
    assert "PROHIBITED" in report

def test_report_high_risk_recommendations():
    report = generate_report(HIGH_RISK)
    assert "Art. 9" in report
    assert "Art. 11" in report
    assert "Art. 43" in report
    assert "Art. 49" in report

def test_report_high_risk_penalty():
    report = generate_report(HIGH_RISK)
    assert "15,000,000" in report

def test_report_limited_risk_art50():
    report = generate_report(LIMITED_RISK)
    assert "Art. 50" in report

def test_report_gpai_flops_mention():
    report = generate_report(GPAI)
    assert "10^25" in report

def test_report_minimal_risk_voluntary():
    report = generate_report(MINIMAL)
    assert "Art. 95" in report

def test_report_source_included():
    report = generate_report(MINIMAL, source="project_brief.pdf")
    assert "project_brief.pdf" in report

def test_report_roles_included():
    report = generate_report(MINIMAL, roles=["provider", "deployer"])
    assert "provider" in report
    assert "deployer" in report

def test_report_findings_listed():
    report = generate_report(HIGH_RISK)
    assert "Employment" in report

def test_report_violated_articles_listed():
    report = generate_report(PROHIBITED)
    assert "Art. 5(1)(c)" in report

def test_report_returns_string():
    for result in [PROHIBITED, HIGH_RISK, LIMITED_RISK, GPAI, MINIMAL]:
        report = generate_report(result)
        assert isinstance(report, str)
        assert len(report) > 100
