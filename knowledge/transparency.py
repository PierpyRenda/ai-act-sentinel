"""
Art. 50 EU AI Act — Transparency Obligations
In force: 2 August 2026
"""

TRANSPARENCY_RULES = [
    {
        "id": "art50_1",
        "article": "Art. 50(1)",
        "name": "Chatbot disclosure",
        "trigger": "Direct human interaction with AI system",
        "obligation": "Inform the natural person they are interacting with an AI system (unless obvious from context).",
        "keywords": ["chatbot", "chat", "conversazione", "conversation", "assistente virtuale", "virtual assistant",
                     "chatgpt-like", "ai assistant", "dialogo", "dialog", "interazione", "interaction"],
        "exception": "Natural persons that have been informed by the deployer that they are interacting with an AI.",
    },
    {
        "id": "art50_2",
        "article": "Art. 50(2)",
        "name": "AI-generated content watermarking",
        "trigger": "AI system generating synthetic image, audio, or video content",
        "obligation": "Mark the output as AI-generated in machine-readable format (C2PA standard).",
        "keywords": ["immagine generata", "generated image", "audio sintetico", "synthetic audio", "video AI",
                     "deepfake", "generazione contenuto", "content generation", "immagini AI", "ai images",
                     "image generation", "stable diffusion", "midjourney", "dall-e"],
        "exception": "Narrow exception for authorized law enforcement purposes.",
        "standard": "C2PA (Coalition for Content Provenance and Authenticity)",
    },
    {
        "id": "art50_3",
        "article": "Art. 50(3)",
        "name": "Emotion/biometric disclosure",
        "trigger": "AI system performing emotion recognition or biometric categorization",
        "obligation": "Inform natural persons that they are subject to emotion recognition or biometric categorization.",
        "keywords": ["riconoscimento emozioni", "emotion recognition", "categorizzazione biometrica", "biometric categorization",
                     "sentiment analysis", "analisi sentimenti", "humor detection", "rilevamento umore"],
        "exception": "Emotion recognition for medical or safety purposes under specific conditions.",
    },
    {
        "id": "art50_4",
        "article": "Art. 50(4)",
        "name": "Deepfake labeling",
        "trigger": "Deploying deepfake audio, image, or video of real persons/places/events",
        "obligation": "Disclose that the content is artificially generated or manipulated.",
        "keywords": ["deepfake", "deep fake", "face swap", "voice clone", "voce clonata", "persona reale", "real person",
                     "manipolazione video", "video manipulation", "sintesi vocale", "voice synthesis"],
        "exception": "Artistic, creative, satire, or fictional contexts — exception applies only if appropriately marked.",
    },
    {
        "id": "art50_5",
        "article": "Art. 50(5)",
        "name": "AI-generated text public interest",
        "trigger": "Publishing AI-generated text on matters of public interest",
        "obligation": "Label the text as AI-generated.",
        "keywords": ["notizie", "news", "articolo", "article", "politica", "politics", "giornalismo", "journalism",
                     "comunicazione pubblica", "public communication", "interesse pubblico", "public interest"],
    },
]
