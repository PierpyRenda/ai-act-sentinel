"""
Art. 5 EU AI Act — Prohibited Practices
Entry into force: 2 February 2025
Penalty: up to €35M or 7% worldwide turnover
"""

PROHIBITED_PRACTICES = [
    {
        "id": "5a",
        "article": "Art. 5(1)(a)",
        "name": "Subliminal or manipulative techniques",
        "description": "AI deploying subliminal techniques beyond consciousness or purposefully manipulative/deceptive techniques that materially distort behavior causing significant harm.",
        "keywords": ["subliminal", "manipulat", "deceptive", "deception", "distort", "behavior"],
        "questions": [
            "Does the system use techniques acting below the user's threshold of consciousness?",
            "Does the system deliberately manipulate user behavior causing significant harm?",
        ],
    },
    {
        "id": "5b",
        "article": "Art. 5(1)(b)",
        "name": "Exploitation of vulnerabilities",
        "description": "AI exploiting vulnerabilities of specific groups (age, disability, socioeconomic status) to distort behavior causing harm.",
        "keywords": ["vulnerab", "disabil", "children", "elderly", "socioeconomic", "povert"],
        "questions": [
            "Does the system specifically target children, elderly, disabled persons, or those in economic hardship?",
            "Does it exploit vulnerability characteristics to influence decisions?",
        ],
    },
    {
        "id": "5c",
        "article": "Art. 5(1)(c)",
        "name": "Social scoring",
        "description": "AI evaluating/classifying persons based on social behavior or personal traits causing detrimental or disproportionate treatment.",
        "keywords": ["social scor", "scoring", "classif", "social behavior", "social credit", "reputation"],
        "questions": [
            "Does the system assign scores or classifications based on social behavior?",
            "Is the resulting treatment in unrelated contexts or disproportionate?",
        ],
    },
    {
        "id": "5d",
        "article": "Art. 5(1)(d)",
        "name": "Criminal risk assessment (profiling only)",
        "description": "AI predicting criminal offense risk based SOLELY on profiling or personality traits (not objective criminal facts).",
        "keywords": ["criminal", "crime predict", "recidiv", "crime forecast", "profiling"],
        "questions": [
            "Does the system assess the likelihood that a person will commit a crime?",
            "Is the assessment based solely on profiling or personality traits without objective criminal facts?",
        ],
    },
    {
        "id": "5e",
        "article": "Art. 5(1)(e)",
        "name": "Facial recognition database scraping",
        "description": "AI creating/expanding facial recognition databases through untargeted scraping from internet or CCTV.",
        "keywords": ["facial recogn", "scraping", "cctv", "face database", "biometric database"],
        "questions": [
            "Does the system collect face images from the internet or CCTV in an untargeted manner?",
            "Does it build or expand facial recognition databases through scraping?",
        ],
    },
    {
        "id": "5f",
        "article": "Art. 5(1)(f)",
        "name": "Emotion inference in workplace/education",
        "description": "AI inferring emotions in workplaces or educational institutions (except medical/safety purposes).",
        "keywords": ["emotion recogn", "sentiment workplace", "worker emotions", "employee emotions", "worker mood detection", "emotion inference", "emotion detect"],
        "questions": [
            "Does the system detect or infer emotions of workers or students?",
            "Is the use in a workplace or educational context (not medical/safety)?",
        ],
    },
    {
        "id": "5g",
        "article": "Art. 5(1)(g)",
        "name": "Biometric categorization for sensitive attributes",
        "description": "AI categorizing persons from biometric data to infer race, political opinions, union membership, religion, sexual life/orientation.",
        "keywords": ["biometric categ", "race", "political opinion", "union membership", "religion", "sexual orient"],
        "questions": [
            "Does the system categorize persons based on biometric data to infer sensitive attributes?",
        ],
    },
    {
        "id": "5h",
        "article": "Art. 5(1)(h)",
        "name": "Real-time remote biometric identification in public spaces",
        "description": "Real-time biometric identification by law enforcement in publicly accessible spaces (narrow exceptions apply).",
        "keywords": ["real-time biometric", "biometric identification", "public spaces", "law enforcement", "police", "real-time recognition"],
        "questions": [
            "Does the system perform real-time biometric identification in public spaces?",
            "Is it used by law enforcement without judicial authorization?",
        ],
    },
    {
        "id": "omnibus_ncii",
        "article": "Art. 5 — AI Omnibus (May 2026)",
        "name": "Non-consensual intimate content (NCII)",
        "description": "AI generating intimate images of real persons without consent.",
        "keywords": ["deepfake intim", "nude", "non-consensual nude", "intimate content"],
        "questions": [
            "Does the system generate intimate content of real persons without consent?",
        ],
    },
    {
        "id": "omnibus_csam",
        "article": "Art. 5 — AI Omnibus (May 2026)",
        "name": "Child sexual abuse material (CSAM)",
        "description": "AI generating child sexual abuse material.",
        "keywords": ["csam", "child abuse", "child sexual", "child pornography"],
        "questions": [
            "Can the system generate sexual material involving minors?",
        ],
    },
]
