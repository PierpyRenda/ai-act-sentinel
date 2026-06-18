"""
EU AI Act — Sanctions & Monitoring
Art. 99-101 + Art. 72-73
"""

SANCTION_TIERS = [
    {
        "tier": 1,
        "article": "Art. 99(3)",
        "trigger": "Prohibited practices (Art. 5)",
        "max_fine": "€35,000,000",
        "max_pct": "7%",
        "description": "Violation of prohibited AI practices.",
    },
    {
        "tier": 2,
        "article": "Art. 99(4)",
        "trigger": "High-risk AI obligations, GPAI obligations, transparency obligations",
        "max_fine": "€15,000,000",
        "max_pct": "3%",
        "description": "Violations of Art. 16 (provider), Art. 25 (role change), Art. 26 (deployer), Art. 50 (transparency), etc.",
    },
    {
        "tier": 3,
        "article": "Art. 99(5)",
        "trigger": "Providing false/misleading information to notified bodies or authorities",
        "max_fine": "€7,500,000",
        "max_pct": "1%",
        "description": "Incorrect or misleading information to authorities.",
    },
    {
        "tier": "gpai",
        "article": "Art. 101",
        "trigger": "GPAI model provider violations",
        "max_fine": "€15,000,000",
        "max_pct": "3%",
        "description": "Violations by GPAI model providers of Chapter V obligations.",
    },
    {
        "tier": "eu_institutions",
        "article": "Art. 100",
        "trigger": "EU institution violations",
        "max_fine_high": "€1,500,000",
        "max_fine_low": "€750,000",
        "description": "Administrative fines for EU institutions, bodies, offices, agencies.",
    },
]

MONITORING_OBLIGATIONS = {
    "post_market": {
        "article": "Art. 72",
        "description": "Providers must actively monitor high-risk AI systems after deployment.",
        "template_deadline": "2 February 2026",
        "note": "Commission provides template by Feb 2026.",
    },
    "incident_reporting": {
        "article": "Art. 73",
        "standard_window_days": 15,
        "severe_window_days": 2,
        "death_window_days": 10,
        "description": "Serious incidents must be reported to national market surveillance authority.",
    },
    "regulatory_sandbox": {
        "article": "Art. 57",
        "description": "No fines during regulatory sandbox participation if acting in good faith.",
        "deadline": "2 August 2026 (Member States must establish)",
    },
}
