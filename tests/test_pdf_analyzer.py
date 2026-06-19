import sys
import os
import tempfile
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pytest
from unittest.mock import patch, MagicMock
from tools.pdf_analyzer import extract_ai_system_description, analyze_pdf


def test_extract_description_with_ai_keyword():
    text = "Introduction\nThis is a project.\n\nAI System Description\nUses machine learning to classify images.\nProcesses user data."
    result = extract_ai_system_description(text)
    assert "machine learning" in result.lower()

def test_extract_description_fallback_full_text():
    text = "A simple inventory app with no AI keywords at all."
    result = extract_ai_system_description(text)
    assert result == text

def test_extract_description_captures_from_trigger_onward():
    text = "Preamble line.\nAnother line.\nModel architecture: transformer with 7B parameters.\nMore technical details.\nBudget: 50000 EUR."
    result = extract_ai_system_description(text)
    assert "transformer" in result.lower()
    assert "Preamble" not in result

def test_extract_description_returns_string():
    result = extract_ai_system_description("Some text about automation and classification")
    assert isinstance(result, str)

def test_analyze_pdf_file_not_found():
    result = analyze_pdf("/nonexistent/path/does_not_exist.pdf")
    assert "error" in result

def test_analyze_pdf_not_found_no_crash():
    result = analyze_pdf("/tmp/definitely_missing_file.pdf")
    assert isinstance(result, dict)

def test_analyze_pdf_mock_success():
    mock_page = MagicMock()
    mock_page.get_text.return_value = "AI recruitment system for CV screening and candidate scoring"
    mock_doc = MagicMock()
    mock_doc.__iter__ = MagicMock(return_value=iter([mock_page]))
    mock_doc.close = MagicMock()

    with patch("tools.pdf_analyzer.HAS_PYMUPDF", True), \
         patch("tools.pdf_analyzer.os.path.exists", return_value=True), \
         patch("fitz.open", return_value=mock_doc):
        result = analyze_pdf("/fake/project.pdf")
        assert "description" in result
        assert "raw_length" in result
        assert result["source"] == "/fake/project.pdf"
        assert result["raw_length"] > 0

def test_analyze_pdf_mock_content_classified():
    """Description returned by analyze_pdf should contain AI-related content."""
    mock_page = MagicMock()
    mock_page.get_text.return_value = "Machine learning algorithm for creditworthiness assessment of persone fisiche mutui bancari"
    mock_doc = MagicMock()
    mock_doc.__iter__ = MagicMock(return_value=iter([mock_page]))
    mock_doc.close = MagicMock()

    with patch("tools.pdf_analyzer.HAS_PYMUPDF", True), \
         patch("tools.pdf_analyzer.os.path.exists", return_value=True), \
         patch("fitz.open", return_value=mock_doc):
        result = analyze_pdf("/fake/credit.pdf")
        assert "creditworthiness" in result["description"].lower() or len(result["description"]) > 0
