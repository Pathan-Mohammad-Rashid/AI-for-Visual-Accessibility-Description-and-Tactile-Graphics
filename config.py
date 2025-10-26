"""
Configuration Settings for AI Visual Accessibility Project
"""

import os
from pathlib import Path

# Project Paths
PROJECT_ROOT = Path(__file__).parent
SRC_DIR = PROJECT_ROOT / "src"
ASSETS_DIR = PROJECT_ROOT / "assets"
OUTPUTS_DIR = PROJECT_ROOT / "outputs"
MODELS_DIR = PROJECT_ROOT / "models"

# Create directories if they don't exist
ASSETS_DIR.mkdir(parents=True, exist_ok=True)
OUTPUTS_DIR.mkdir(parents=True, exist_ok=True)
(OUTPUTS_DIR / "patterns").mkdir(parents=True, exist_ok=True)
(OUTPUTS_DIR / "hardware_files").mkdir(parents=True, exist_ok=True)

# Tactile Display Settings
TACTILE_CONFIG = {
    "ball_diameter_mm": 3.0,
    "ball_spacing_mm": 3.5,
    "grid_sizes": [4, 8, 16, 32],  # Powers of 2
    "default_grid_size": 4,
    "ball_weight_g": 0.11,  # Weight of 3mm steel ball
}

# Image Processing Settings
IMAGE_CONFIG = {
    "max_upload_size_mb": 10,
    "supported_formats": ["png", "jpg", "jpeg", "bmp", "tiff"],
    "processing_methods": ["edge", "threshold", "high_contrast", "adaptive"],
    "default_method": "threshold",
}

# VLM (Vision-Language Model) Settings
VLM_CONFIG = {
    # Choose VLM backend: "openai", "huggingface", "local", "none"
    "backend": "none",  # Start with none, upgrade to openai or huggingface later
    
    # OpenAI Settings (if using GPT-4V)
    "openai": {
        "model": "gpt-4-vision-preview",
        "api_key": os.getenv("OPENAI_API_KEY", ""),
        "max_tokens": 500,
        "temperature": 0.3,
    },
    
    # Hugging Face Settings (if using open-source VLM)
    "huggingface": {
        "model_name": "HuggingFaceTB/SmolVLM-Instruct",  # or "llava-hf/llava-1.5-7b-hf"
        "device": "cpu",  # or "cuda" if GPU available
        "max_new_tokens": 200,
    },
    
    # VLM Prompts
    "prompts": {
        "describe": "Describe the main objects and shapes in this image in simple terms.",
        "simplify": "Identify the key visual elements that would be important for a tactile representation.",
        "extract": "What are the most important shapes and outlines in this image?",
    }
}

# Streamlit UI Settings
UI_CONFIG = {
    "page_title": "AI Visual Accessibility - Tactile Graphics",
    "page_icon": "👁️",
    "layout": "wide",
    "theme": {
        "primaryColor": "#4CAF50",
        "backgroundColor": "#FFFFFF",
        "secondaryBackgroundColor": "#F0F2F6",
        "textColor": "#262730",
    }
}

# Hardware Export Settings
HARDWARE_CONFIG = {
    "formats": ["txt", "arduino", "json", "csv"],
    "default_format": "arduino",
    "microcontrollers": ["Arduino Mega", "ESP32", "Raspberry Pi Pico"],
}

# Development Settings
DEBUG = os.getenv("DEBUG", "False").lower() == "true"
VERBOSE = os.getenv("VERBOSE", "False").lower() == "true"