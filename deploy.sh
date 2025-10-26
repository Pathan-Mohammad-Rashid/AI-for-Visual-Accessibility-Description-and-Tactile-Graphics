#!/bin/bash

# Deployment Helper Script for AI Visual Accessibility - Tactile Graphics

echo "🚀 AI Visual Accessibility - Deployment Helper"
echo "=============================================="
echo ""

# Function to check if command exists
command_exists() {
    command -v "$1" >/dev/null 2>&1
}

# Check Python installation
if ! command_exists python && ! command_exists python3; then
    echo "❌ Python is not installed. Please install Python 3.9 or higher."
    exit 1
fi

PYTHON_CMD=$(command_exists python3 && echo "python3" || echo "python")

# Get Python version
PYTHON_VERSION=$($PYTHON_CMD --version 2>&1 | awk '{print $2}')
echo "✓ Python version: $PYTHON_VERSION"

# Check if streamlit is installed
if ! $PYTHON_CMD -c "import streamlit" 2>/dev/null; then
    echo "📦 Streamlit not found. Installing dependencies..."
    $PYTHON_CMD -m pip install -r requirements.txt
else
    echo "✓ Streamlit is installed"
fi

echo ""
echo "Deployment options:"
echo "1. Run locally (localhost:8501)"
echo "2. Show deployment instructions"
echo "3. Build Docker image"
echo ""
read -p "Select option (1-3): " option

case $option in
    1)
        echo ""
        echo "🌟 Starting Streamlit app locally..."
        echo "📍 The app will be available at http://localhost:8501"
        echo ""
        streamlit run app.py
        ;;
    2)
        echo ""
        echo "📖 Deployment Instructions:"
        echo ""
        echo "🌐 Streamlit Community Cloud (Recommended - FREE):"
        echo "   1. Fork this repository"
        echo "   2. Sign up at https://streamlit.io/cloud"
        echo "   3. Click 'New app' and select your forked repo"
        echo "   4. Set main file: app.py"
        echo "   5. Click 'Deploy'"
        echo ""
        echo "🐳 Docker:"
        echo "   docker build -t tactile-graphics ."
        echo "   docker run -p 8501:8501 tactile-graphics"
        echo ""
        echo "☁️ Other Cloud Platforms:"
        echo "   - Heroku: Use Streamlit deployment guide"
        echo "   - Railway: Connect GitHub and auto-deploy"
        echo "   - AWS/GCP/Azure: Deploy using containers"
        echo ""
        ;;
    3)
        if ! command_exists docker; then
            echo "❌ Docker is not installed."
            exit 1
        fi
        echo ""
        echo "🐳 Building Docker image..."
        docker build -t tactile-graphics .
        echo ""
        echo "✓ Docker image built successfully!"
        echo ""
        echo "To run the container:"
        echo "  docker run -p 8501:8501 tactile-graphics"
        echo ""
        echo "Then open http://localhost:8501 in your browser"
        ;;
    *)
        echo "❌ Invalid option"
        exit 1
        ;;
esac
