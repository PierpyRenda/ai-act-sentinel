"""
Chapter V EU AI Act — General Purpose AI (GPAI) Models
In force: 2 August 2025
"""

GPAI_INDICATORS = [
    "language model", "llm", "large language model",
    "foundation model", "generative ai",
    "text generation", "image generation",
    "multimodal", "base model",
    "training data", "pre-training", "fine-tuning",
    "gpt", "claude", "gemini", "llama", "mistral", "falcon",
]

SYSTEMIC_RISK_THRESHOLD_FLOPS = 1e25  # 10^25 FLOPs

GPAI_UNIVERSAL_OBLIGATIONS = [
    {
        "id": "art53_1a",
        "article": "Art. 53(1)(a)",
        "name": "Technical documentation",
        "description": "Draw up and keep technical documentation (Annexes XI and XII) and make it available to AI Office and competent authorities.",
    },
    {
        "id": "art53_1b",
        "article": "Art. 53(1)(b)",
        "name": "Downstream provider information",
        "description": "Provide information and documentation to AI system providers downstream enabling compliance.",
    },
    {
        "id": "art53_1c",
        "article": "Art. 53(1)(c)",
        "name": "Copyright policy",
        "description": "Implement policy to respect and comply with EU copyright law including opt-out mechanisms.",
    },
    {
        "id": "art53_1d",
        "article": "Art. 53(1)(d)",
        "name": "Training data summary",
        "description": "Publish sufficiently detailed summary of training content (publicly available).",
    },
]

OPEN_SOURCE_EXCEPTION_OBLIGATIONS = ["art53_1c", "art53_1d"]  # Only these apply to open-source models

SYSTEMIC_RISK_ADDITIONAL_OBLIGATIONS = [
    {
        "id": "art55_1a",
        "article": "Art. 55(1)(a)",
        "name": "Adversarial testing",
        "description": "Perform model evaluation per standardized protocols, adversarial testing to identify risks.",
    },
    {
        "id": "art55_1b",
        "article": "Art. 55(1)(b)",
        "name": "Systemic risk mitigation",
        "description": "Assess and mitigate possible systemic risks at EU level.",
    },
    {
        "id": "art55_1c",
        "article": "Art. 55(1)(c)",
        "name": "Serious incident reporting",
        "description": "Track, document and report serious incidents to the AI Office without undue delay.",
    },
    {
        "id": "art55_1d",
        "article": "Art. 55(1)(d)",
        "name": "Cybersecurity",
        "description": "Ensure adequate level of cybersecurity protection for GPAI model and physical infrastructure.",
    },
]
