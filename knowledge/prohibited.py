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
        "keywords": ["subliminal", "manipol", "deceptive", "inganno", "manipolazione", "comportamento", "distort", "behavior"],
        "questions": [
            "Il sistema usa tecniche che agiscono al di sotto della soglia di coscienza dell'utente?",
            "Il sistema manipola deliberatamente il comportamento degli utenti causando danni significativi?",
        ],
    },
    {
        "id": "5b",
        "article": "Art. 5(1)(b)",
        "name": "Exploitation of vulnerabilities",
        "description": "AI exploiting vulnerabilities of specific groups (age, disability, socioeconomic status) to distort behavior causing harm.",
        "keywords": ["vulnerab", "anzian", "disabil", "minori", "children", "elderly", "socioeconomic", "povert"],
        "questions": [
            "Il sistema si rivolge specificamente a minori, anziani, disabili o persone in difficoltà economica?",
            "Sfrutta caratteristiche di vulnerabilità per influenzare decisioni?",
        ],
    },
    {
        "id": "5c",
        "article": "Art. 5(1)(c)",
        "name": "Social scoring",
        "description": "AI evaluating/classifying persons based on social behavior or personal traits causing detrimental or disproportionate treatment.",
        "keywords": ["social scor", "punteggio social", "scoring", "classif", "comportamento social", "credit social", "reputazione"],
        "questions": [
            "Il sistema assegna punteggi o classificazioni basate sul comportamento sociale?",
            "Il trattamento risultante è in contesti non correlati o sproporzionato?",
        ],
    },
    {
        "id": "5d",
        "article": "Art. 5(1)(d)",
        "name": "Criminal risk assessment (profiling only)",
        "description": "AI predicting criminal offense risk based SOLELY on profiling or personality traits (not objective criminal facts).",
        "keywords": ["criminal", "crime predict", "recidiv", "criminale", "previsione reato", "profilag"],
        "questions": [
            "Il sistema valuta la probabilità che una persona commetta un reato?",
            "La valutazione si basa esclusivamente su profiling o tratti della personalità senza fatti criminali oggettivi?",
        ],
    },
    {
        "id": "5e",
        "article": "Art. 5(1)(e)",
        "name": "Facial recognition database scraping",
        "description": "AI creating/expanding facial recognition databases through untargeted scraping from internet or CCTV.",
        "keywords": ["facial recogn", "riconoscimento facciale", "scraping", "cctv", "database volti", "biometric database"],
        "questions": [
            "Il sistema raccoglie immagini di volti da internet o CCTV in modo non mirato?",
            "Costruisce o espande database di riconoscimento facciale tramite scraping?",
        ],
    },
    {
        "id": "5f",
        "article": "Art. 5(1)(f)",
        "name": "Emotion inference in workplace/education",
        "description": "AI inferring emotions in workplaces or educational institutions (except medical/safety purposes).",
        "keywords": ["emotion recogn", "riconoscimento emozioni", "sentiment workplace", "emozioni lavoratori", "emozioni dipendenti", "rilevamento umore lavoratori", "inferire emozioni", "emotion detect"],
        "questions": [
            "Il sistema rileva o inferisce le emozioni di lavoratori o studenti?",
            "L'uso è in contesto lavorativo o educativo (non medico/sicurezza)?",
        ],
    },
    {
        "id": "5g",
        "article": "Art. 5(1)(g)",
        "name": "Biometric categorization for sensitive attributes",
        "description": "AI categorizing persons from biometric data to infer race, political opinions, union membership, religion, sexual life/orientation.",
        "keywords": ["biometric categ", "razza", "race", "opinione politica", "sindacato", "religione", "orientamento sessuale", "sexual orient"],
        "questions": [
            "Il sistema categorizza persone in base a dati biometrici per dedurre attributi sensibili?",
        ],
    },
    {
        "id": "5h",
        "article": "Art. 5(1)(h)",
        "name": "Real-time remote biometric identification in public spaces",
        "description": "Real-time biometric identification by law enforcement in publicly accessible spaces (narrow exceptions apply).",
        "keywords": ["real-time biometric", "identificazione biometrica", "spazi pubblici", "law enforcement", "polizia", "riconoscimento in tempo reale"],
        "questions": [
            "Il sistema esegue identificazione biometrica in tempo reale in spazi pubblici?",
            "È usato da forze dell'ordine senza autorizzazione giudiziaria?",
        ],
    },
    {
        "id": "omnibus_ncii",
        "article": "Art. 5 — AI Omnibus (maggio 2026)",
        "name": "Non-consensual intimate content (NCII)",
        "description": "AI generating intimate images of real persons without consent.",
        "keywords": ["deepfake intim", "nude", "nudi non consensual", "intimate content", "contenuto intimo"],
        "questions": [
            "Il sistema genera contenuti intimi di persone reali senza consenso?",
        ],
    },
    {
        "id": "omnibus_csam",
        "article": "Art. 5 — AI Omnibus (maggio 2026)",
        "name": "Child sexual abuse material (CSAM)",
        "description": "AI generating child sexual abuse material.",
        "keywords": ["csam", "child abuse", "minori sessual", "pedopornografi"],
        "questions": [
            "Il sistema può generare materiale sessuale che coinvolge minori?",
        ],
    },
]
