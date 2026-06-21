"""
EU AI Act — 6 Operator Roles + Obligations Matrix
"""

ROLES = {
    "provider": {
        "name": "Provider",
        "definition": "Develops AI system and places it on market or puts into service under own name/trademark.",
        "obligations": [
            {"article": "Art. 9", "name": "Risk management system"},
            {"article": "Art. 10", "name": "Data governance"},
            {"article": "Art. 11", "name": "Technical documentation"},
            {"article": "Art. 12", "name": "Automatic logging"},
            {"article": "Art. 13", "name": "Transparency for deployers"},
            {"article": "Art. 14", "name": "Human oversight design"},
            {"article": "Art. 15", "name": "Accuracy, robustness, cybersecurity"},
            {"article": "Art. 17", "name": "Quality management system"},
            {"article": "Art. 43", "name": "Conformity assessment"},
            {"article": "Art. 47", "name": "EU declaration of conformity + CE marking"},
            {"article": "Art. 49", "name": "EU database registration"},
            {"article": "Art. 72", "name": "Post-market monitoring"},
            {"article": "Art. 73", "name": "Serious incident reporting (15/2/10 days)"},
            {"article": "Art. 4", "name": "AI literacy for staff"},
        ],
    },
    "deployer": {
        "name": "Deployer",
        "definition": "Uses AI system under own authority in professional context.",
        "obligations": [
            {"article": "Art. 26(1)", "name": "Follow provider instructions"},
            {"article": "Art. 26(2)", "name": "Assign competent human oversight persons"},
            {"article": "Art. 26(3)", "name": "Ensure input data quality"},
            {"article": "Art. 26(4)", "name": "Monitor and report incidents"},
            {"article": "Art. 26(5)", "name": "Retain logs minimum 6 months"},
            {"article": "Art. 26(6)", "name": "Notify workers before workplace deployment"},
            {"article": "Art. 26(7)", "name": "Verify EU database registration (public authorities)"},
            {"article": "Art. 26(10)", "name": "Inform subjects of AI decisions"},
            {"article": "Art. 27", "name": "Fundamental rights impact assessment (FRIA) — public bodies + essential services"},
            {"article": "Art. 4", "name": "AI literacy for staff"},
        ],
    },
    "importer": {
        "name": "Importer",
        "definition": "EU-established entity placing on market AI system bearing third-country provider's name.",
        "obligations": [
            {"article": "Art. 23", "name": "Verify conformity assessment completed"},
            {"article": "Art. 23", "name": "Verify technical documentation in order"},
            {"article": "Art. 23", "name": "Verify CE marking affixed"},
            {"article": "Art. 23", "name": "Register in EU database"},
            {"article": "Art. 23", "name": "Keep copy of EU declaration of conformity"},
        ],
    },
    "distributor": {
        "name": "Distributor",
        "definition": "Supply chain actor making systems available (not provider or importer).",
        "obligations": [
            {"article": "Art. 24", "name": "Verify CE marking is affixed"},
            {"article": "Art. 24", "name": "Verify EU declaration of conformity is in place"},
            {"article": "Art. 24", "name": "Inform provider/importer of suspected non-compliance"},
        ],
    },
    "authorized_representative": {
        "name": "Authorized Representative",
        "definition": "EU-established entity designated by non-EU provider via written mandate.",
        "obligations": [
            {"article": "Art. 22", "name": "Register high-risk AI system in EU database"},
            {"article": "Art. 22", "name": "Keep copy of EU declaration of conformity and technical docs"},
            {"article": "Art. 22", "name": "Cooperate with competent authorities"},
            {"article": "Art. 22", "name": "Inform provider of risks; terminate mandate if non-compliant"},
        ],
    },
    "product_manufacturer": {
        "name": "Product Manufacturer",
        "definition": "Manufacturer of Annex I products containing high-risk AI as safety component.",
        "obligations": [
            {"article": "Art. 25", "name": "Full provider obligations apply when placing under own name/trademark"},
        ],
    },
}


def detect_role_from_description(description: str) -> list[str]:
    """Heuristic role detection from project description text."""
    text = description.lower()
    roles = []

    if any(k in text for k in ["develop", "build", "create", "training", "deploy own"]):
        roles.append("provider")

    if any(k in text for k in ["use", "implement", "deploy", "apply"]):
        roles.append("deployer")

    if any(k in text for k in ["import", "third country", "distribution"]):
        roles.append("importer")

    if not roles:
        roles.append("deployer")  # default assumption

    return roles
