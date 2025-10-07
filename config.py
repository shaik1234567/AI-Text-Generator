"""
Configuration file for AI Text Generator
Contains model names, parameters, and prompt templates
"""

# Model Configuration
SENTIMENT_MODEL = "distilbert-base-uncased-finetuned-sst-2-english"
TEXT_GENERATION_MODEL = "distilgpt2"

# Generation Parameters
DEFAULT_MAX_LENGTH = 150  # Default length for generated text
MIN_LENGTH = 50
MAX_LENGTH = 500

# Temperature settings (controls randomness)
TEMPERATURE = 0.8
TOP_K = 50
TOP_P = 0.95

# Sentiment labels mapping
SENTIMENT_LABELS = {
    "POSITIVE": "positive",
    "NEGATIVE": "negative", 
    "NEUTRAL": "neutral"
}

# Prompt templates for sentiment-aligned generation
PROMPT_TEMPLATES = {
    "positive": {
        "prefix": "Write an uplifting and positive text about: ",
        "style_words": ["wonderful", "amazing", "delightful", "excellent", "fantastic"]
    },
    "negative": {
        "prefix": "Write a critical and negative text about: ",
        "style_words": ["disappointing", "unfortunate", "problematic", "concerning", "troubling"]
    },
    "neutral": {
        "prefix": "Write an objective and balanced text about: ",
        "style_words": ["regarding", "concerning", "about", "related to", "pertaining to"]
    }
}

# Length presets for user selection
LENGTH_PRESETS = {
    "Short": 80,
    "Medium": 150,
    "Long": 300
}

# UI Configuration
APP_TITLE = "🤖 AI Text Generator"
APP_DESCRIPTION = """
Generate sentiment-aligned text based on your prompts!
This app analyzes the sentiment of your input and generates text that matches that emotional tone.
"""

# Confidence threshold for sentiment detection
CONFIDENCE_THRESHOLD = 0.6