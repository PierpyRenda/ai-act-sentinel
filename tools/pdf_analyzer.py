"""
PDF Analyzer — extract text from project documents for compliance analysis.
Requires: pip install pymupdf
"""

import os
import sys

try:
    import fitz  # PyMuPDF
    HAS_PYMUPDF = True
except ImportError:
    HAS_PYMUPDF = False


def extract_text_from_pdf(pdf_path: str) -> str:
    """Extract full text from a PDF file."""
    if not os.path.exists(pdf_path):
        raise FileNotFoundError(f"PDF not found: {pdf_path}")

    if not HAS_PYMUPDF:
        raise ImportError("PyMuPDF not installed. Run: pip install pymupdf")

    doc = fitz.open(pdf_path)
    pages_text = []
    for page in doc:
        pages_text.append(page.get_text())
    doc.close()
    return "\n".join(pages_text)


def extract_ai_system_description(text: str) -> str:
    """
    Extract the relevant portion of a document describing the AI system.
    Looks for key sections by heading pattern.
    Returns the full text if no sections found.
    """
    section_triggers = [
        "sistema di intelligenza artificiale",
        "sistema ai",
        "ai system",
        "artificial intelligence system",
        "machine learning",
        "algoritmo",
        "algorithm",
        "modello",
        "model",
        "automazione",
        "automation",
        "analisi predittiva",
        "predictive analysis",
        "classificazione",
        "classification",
        "riconoscimento",
        "recognition",
        "descrizione del progetto",
        "project description",
        "obiettivi",
        "objectives",
        "funzionalità",
        "features",
        "architettura tecnica",
        "technical architecture",
    ]

    lines = text.split("\n")
    relevant_lines = []
    capture = False

    for line in lines:
        line_lower = line.lower().strip()
        if any(trigger in line_lower for trigger in section_triggers):
            capture = True
        if capture:
            relevant_lines.append(line)

    if relevant_lines:
        return "\n".join(relevant_lines)
    return text  # fallback: return everything


def analyze_pdf(pdf_path: str) -> dict:
    """
    Full pipeline: extract text from PDF, return structured content for classifier.
    Returns {"error": ...} on failure instead of raising.
    """
    try:
        raw_text = extract_text_from_pdf(pdf_path)
    except (FileNotFoundError, ImportError, Exception) as e:
        return {"error": str(e), "source": pdf_path}
    description = extract_ai_system_description(raw_text)

    return {
        "raw_length": len(raw_text),
        "description_length": len(description),
        "description": description,
        "source": pdf_path,
    }
