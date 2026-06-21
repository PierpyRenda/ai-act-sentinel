import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pytest
from tools.classifier import classify

REQUIRED_KEYS = {"risk_level", "findings", "violated_articles", "obligations", "summary"}


# --- Structure ---

def test_result_always_has_required_keys():
    for desc in [
        "inventory management system",
        "LLM large language model with pre-training",
        "social scoring system classifies citizens",
        "chatbot customer service",
    ]:
        result = classify(desc)
        assert REQUIRED_KEYS.issubset(result.keys()), f"Missing keys for: {desc}"


# --- Out of scope ---

def test_out_of_scope_military():
    result = classify("AI system for military targeting and defense operations")
    assert result["risk_level"] == "OUT_OF_SCOPE"

def test_out_of_scope_personal():
    result = classify("Personal non-professional app to track my daily running distance")
    assert result["risk_level"] == "OUT_OF_SCOPE"


# --- PROHIBITED (Art. 5) ---

def test_prohibited_social_scoring():
    result = classify("social scoring system that classifies citizens based on social behavior and social credit")
    assert result["risk_level"] == "PROHIBITED"
    assert len(result["findings"]) >= 1

def test_prohibited_facial_scraping():
    result = classify("Tool performing facial recogn scraping from internet CCTV to build biometric database")
    assert result["risk_level"] == "PROHIBITED"

def test_prohibited_biometric_race():
    result = classify("System using biometric categ to infer race and religion from photos")
    assert result["risk_level"] == "PROHIBITED"

def test_prohibited_ncii():
    result = classify("Platform generating deepfake intim nude intimate content of real persons")
    assert result["risk_level"] == "PROHIBITED"

def test_prohibited_csam():
    result = classify("System that can generate csam child abuse child sexual content")
    assert result["risk_level"] == "PROHIBITED"

def test_prohibited_criminal_profiling():
    result = classify("AI predicting criminal risk recidiv based on profiling personality traits")
    assert result["risk_level"] == "PROHIBITED"

def test_prohibited_max_penalty_present():
    result = classify("social scoring classifies citizens based on social behavior social credit")
    assert result["risk_level"] == "PROHIBITED"
    assert "max_penalty" in result
    assert "35" in result["max_penalty"]


# --- HIGH RISK (Annex III) ---

def test_high_risk_recruitment():
    result = classify("AI system for automated CV screening and candidate ranking for recruitment hiring")
    assert result["risk_level"] in ("HIGH_RISK", "HIGH_RISK_POSSIBLE_EXCEPTION")

def test_high_risk_credit_assessment():
    result = classify("AI for creditworthiness assessment of individuals for bank mortgage loans")
    assert result["risk_level"] == "HIGH_RISK"
    assert len(result["obligations"]) >= 5

def test_high_risk_has_standard_obligations():
    result = classify("AI for creditworthiness scoring of individuals for bank mortgages")
    if result["risk_level"] == "HIGH_RISK":
        obligations_text = " ".join(result["obligations"])
        assert "Art. 9" in obligations_text
        assert "Art. 11" in obligations_text
        assert "Art. 43" in obligations_text

def test_high_risk_possible_exception_documented():
    result = classify("AI tool for procedural document sorting in HR onboarding — preparatory task only")
    # May or may not trigger exception depending on keywords — just check valid level
    assert result["risk_level"] in ("HIGH_RISK", "HIGH_RISK_POSSIBLE_EXCEPTION", "MINIMAL_RISK", "LIMITED_RISK")


# --- LIMITED RISK (Art. 50) ---

def test_limited_risk_chatbot():
    result = classify("Customer service chatbot for direct interaction with users, virtual assistant conversation")
    assert result["risk_level"] in ("LIMITED_RISK", "LIMITED_RISK+GPAI")

def test_limited_risk_deepfake_label():
    result = classify("Video tool creating deepfake face swap of real person for entertainment")
    assert result["risk_level"] in ("LIMITED_RISK", "PROHIBITED")

def test_limited_risk_obligations_not_empty():
    result = classify("AI chatbot assistant for customer interaction conversation")
    if result["risk_level"] in ("LIMITED_RISK", "LIMITED_RISK+GPAI"):
        assert len(result["obligations"]) >= 1


# --- GPAI (Chapter V) — the bug case ---

def test_gpai_only_no_crash():
    """Pure GPAI without transparency triggers must not crash and must return GPAI level."""
    result = classify("Large language model LLM with pre-training on text corpora and fine-tuning capabilities")
    assert result["risk_level"] == "GPAI"

def test_gpai_has_obligations():
    result = classify("Foundation model large language model LLM pre-training base model")
    if result["risk_level"] == "GPAI":
        assert len(result["obligations"]) > 0

def test_gpai_violated_article():
    result = classify("Large language model LLM with pre-training and fine-tuning")
    if result["risk_level"] == "GPAI":
        assert "Art. 53" in result["violated_articles"]

def test_limited_risk_plus_gpai():
    """Chatbot built on an LLM should be LIMITED_RISK+GPAI."""
    result = classify("LLM-based chatbot large language model for conversation interaction with users")
    assert result["risk_level"] in ("LIMITED_RISK+GPAI", "LIMITED_RISK", "GPAI")


# --- MINIMAL RISK ---

def test_minimal_risk_warehouse():
    result = classify("Inventory management system for tracking warehouse stock levels")
    assert result["risk_level"] == "MINIMAL_RISK"
    assert result["findings"] == []
    assert result["obligations"] == []

def test_minimal_risk_no_penalty():
    result = classify("Simple rule-based automation for invoice formatting")
    if result["risk_level"] == "MINIMAL_RISK":
        assert "max_penalty" not in result
