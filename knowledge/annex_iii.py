"""
Annex III EU AI Act — High-Risk Use Case Matcher
8 categories. Systems listed here = HIGH-RISK by default (Art. 6(2)).
Exception: narrow procedural tasks, not profiling.
"""

ANNEX_III_CATEGORIES = [
    {
        "id": "annex3_1",
        "category": "1. Biometrics",
        "article": "Annex III(1)",
        "use_cases": [
            "remote biometric identification",
            "biometric categorization inferring protected attributes",
            "emotion recognition",
            "face recognition",
            "fingerprint recognition",
            "iris recognition",
            "gait recognition",
            "voice biometrics",
        ],
        "keywords": ["biometric", "facial recognition", "emotion recognition",
                     "fingerprint", "iris", "voice recognition", "remote identification"],
    },
    {
        "id": "annex3_2",
        "category": "2. Critical Infrastructure",
        "article": "Annex III(2)",
        "use_cases": [
            "safety components in digital infrastructure management",
            "road traffic management",
            "water supply management",
            "gas supply management",
            "heating supply management",
            "electricity supply management",
        ],
        "keywords": ["critical infrastructure", "traffic management",
                     "gas", "electricity", "heating", "supply management", "water supply"],
    },
    {
        "id": "annex3_3",
        "category": "3. Education & Vocational Training",
        "article": "Annex III(3)",
        "use_cases": [
            "admission determination to educational institutions",
            "learning outcome assessment",
            "educational level evaluation",
            "student behavior monitoring during exams",
        ],
        "keywords": ["education", "school", "university", "students",
                     "admission", "exam", "learning assessment",
                     "exam monitoring"],
    },
    {
        "id": "annex3_4",
        "category": "4. Employment & Worker Management",
        "article": "Annex III(4)",
        "use_cases": [
            "recruitment and job advertisement targeting",
            "job application filtering",
            "candidate evaluation and selection",
            "employee promotion or termination decisions",
            "task assignment based on personality/behavioral traits",
            "performance monitoring of workers",
        ],
        "keywords": ["recruitment", "hiring", "candidate", "workers",
                     "employees", "termination", "promotion",
                     "employee monitoring", "performance"],
    },
    {
        "id": "annex3_5",
        "category": "5. Essential Public & Private Services",
        "article": "Annex III(5)",
        "use_cases": [
            "public authority benefit/service entitlement assessment",
            "creditworthiness evaluation of natural persons",
            "emergency call triage and dispatch",
            "health and life insurance risk assessment",
        ],
        "keywords": ["creditworthiness", "credit scoring", "scoring", "public services",
                     "benefits", "emergency", "triage", "insurance",
                     "health", "resource allocation"],
    },
    {
        "id": "annex3_6",
        "category": "6. Law Enforcement",
        "article": "Annex III(6)",
        "use_cases": [
            "victim crime-risk assessment",
            "polygraph alternatives",
            "evidence reliability evaluation",
            "criminal risk and recidivism assessment",
            "criminal investigation profiling",
        ],
        "keywords": ["law enforcement", "police", "crime", "recidivism",
                     "criminal profiling", "criminal risk", "evidence",
                     "polygraph", "investigation"],
    },
    {
        "id": "annex3_7",
        "category": "7. Migration, Asylum & Border Control",
        "article": "Annex III(7)",
        "use_cases": [
            "polygraph alternatives for migration",
            "irregular migration or security risk assessment",
            "asylum application examination",
            "visa or residence permit examination",
            "traveler document authenticity verification",
        ],
        "keywords": ["migration", "asylum", "border", "visa",
                     "residence permit", "refugees", "immigration",
                     "travel documents"],
    },
    {
        "id": "annex3_8",
        "category": "8. Justice & Democratic Processes",
        "article": "Annex III(8)",
        "use_cases": [
            "fact investigation/law application assisting judicial decisions",
            "alternative dispute resolution",
            "election/referendum influence systems",
            "voter behavior modification",
        ],
        "keywords": ["justice", "judges", "judicial decisions",
                     "elections", "voting", "referendum", "democracy",
                     "arbitration", "mediation"],
    },
]


EXCEPTION_KEYWORDS = [
    "procedural task",
    "preparatory task",
    "narrow assessment",
    "human review",
    "deviance detection",
]
