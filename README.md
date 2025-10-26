# AI for Visual Accessibility - Tactile Graphics 

Transform visual images into tactile patterns for visually impaired users using **3mm magnetic balls** and **AI-enhanced processing**.

![Project Status](https://img.shields.io/badge/status-active-success.svg)
![Python Version](https://img.shields.io/badge/python-3.9%2B-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

## 🌐 Live Demo

**Try the app now:** [![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://pathan-mohammad-rashid-ai-for-visual-accessibility-app.streamlit.app)

The application is deployed on Streamlit Community Cloud and ready to use! No installation required.

## 🎯 Project Overview

This system converts any image into a tactile representation that can be felt by visually impaired users. Using electromagnetically controlled 3mm magnetic balls, we create dynamic, refreshable tactile displays with AI-enhanced image processing.

### Key Features

- 🤖 **AI-Enhanced Processing**: Optional Vision-Language Model support for intelligent object extraction
- 📐 **Variable Resolution**: Support for 4×4, 8×8, 16×16, and 32×32 grids
- 💾 **Multiple Export Formats**: Arduino, JSON, TXT, CSV for various hardware platforms
- 🎨 **Real-time Preview**: Visual simulation of tactile patterns
- 📊 **Detailed Statistics**: Physical dimensions, coverage, and specifications
- 🌐 **Web Interface**: Beautiful Streamlit-based UI for easy interaction

## 🚀 Quick Start

### Option 1: Use the Live Demo (Easiest)

**No installation required!** Try the app instantly at:
[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://pathan-mohammad-rashid-ai-for-visual-accessibility-app.streamlit.app)

### Option 2: Run Locally

#### Prerequisites

- Python 3.9 or higher
- VS Code (recommended) or any Python IDE
- Windows, macOS, or Linux

#### Installation

1. **Clone or download the project:**
   ```bash
   mkdir AI-Visual-Accessibility
   cd AI-Visual-Accessibility
   ```

2. **Create virtual environment:**
   ```bash
   python -m venv venv
   
   # Windows:
   venv\\Scripts\\activate
   
   # macOS/Linux:
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application:**
   ```bash
   streamlit run app.py
   ```

5. **Open browser:**
   - Automatically opens at `http://localhost:8501`
   - If not, navigate manually to the address

## 📁 Project Structure

```
AI-Visual-Accessibility-Tactile-Graphics/
├── app.py                          # Main Streamlit web application
├── config.py                       # Configuration settings
├── requirements.txt                # Python dependencies
├── README.md                       # This file
│
├── src/                           # Source code
│   ├── tactile_converter.py      # Core conversion logic
│   ├── vlm_handler.py            # AI/VLM integration
│   ├── image_processor.py        # Image preprocessing
│   └── utils.py                  # Utility functions
│
├── assets/                        # Static assets
│   └── sample_images/            # Example images
│
├── outputs/                       # Generated outputs
│   ├── patterns/                 # Tactile patterns
│   └── hardware_files/           # Hardware files
│
├── models/                        # Model configurations
│   └── vlm_config.py            # VLM settings
│
├── tests/                         # Unit tests
│   └── test_converter.py
│
└── notebooks/                     # Jupyter/Colab notebooks
    └── vlm_testing.ipynb         # VLM experimentation
```

## 💻 Usage

### Basic Workflow

1. **Upload an image** through the web interface
2. **Select grid size** (4×4, 8×8, 16×16, or 32×32)
3. **Choose processing method** (edge, threshold, high_contrast, adaptive)
4. **Click "Convert"** to generate tactile pattern
5. **Preview the pattern** visually
6. **Download hardware file** (Arduino, JSON, TXT, or CSV)

### Processing Methods

- **Edge Detection**: Best for outlines and contours
- **Threshold**: Simple black/white conversion
- **High Contrast**: Enhanced contrast before conversion
- **Adaptive**: Smart local thresholding

### Grid Sizes

| Size | Points | Display Size | Weight | Use Case |
|------|--------|--------------|--------|----------|
| 4×4 | 16 | 14mm × 14mm | 1.8g | Proof of concept |
| 8×8 | 64 | 28mm × 28mm | 7g | Good resolution |
| 16×16 | 256 | 56mm × 56mm | 28g | High quality |
| 32×32 | 1024 | 112mm × 112mm | 113g | Professional |

## 🤖 AI/VLM Integration

### Option 1: Traditional Computer Vision (Default)
No additional setup required. Uses OpenCV and PIL for image processing.

### Option 2: OpenAI GPT-4 Vision API
1. Get API key from [OpenAI Platform](https://platform.openai.com/)
2. Set environment variable:
   ```bash
   export OPENAI_API_KEY="your-api-key-here"
   ```
3. Enable "Use Vision-Language Model" in sidebar
4. Select "OpenAI GPT-4V" backend

### Option 3: Open-Source VLM (Hugging Face)
Best tested in Google Colab with free GPU:
1. Open `notebooks/vlm_testing.ipynb` in Colab
2. Run cells to test SmolVLM or LLaVA
3. Export best configuration
4. Integrate into main app

## 📊 Technical Specifications

### Tactile Display
- **Ball diameter**: 3mm
- **Ball spacing**: 3.5mm center-to-center
- **Ball material**: Steel/ferromagnetic
- **Ball weight**: 0.11g each
- **Actuation**: Electromagnetic control

### Hardware Requirements (for physical prototype)
- N × N magnetic balls (N = grid size)
- N × N electromagnets or solenoids
- Microcontroller (Arduino Mega 2560 or ESP32)
- Driver circuits (MOSFETs or H-bridges)
- Power supply (12V, 2-5A)

### Software Stack
- **Backend**: Python 3.9+
- **Web Framework**: Streamlit
- **Image Processing**: PIL, OpenCV
- **AI/ML**: Transformers, PyTorch (optional)
- **Visualization**: Matplotlib, Plotly

## 🛠️ Development

### Running Tests
```bash
pytest tests/
```

### Code Style
```bash
pip install black flake8
black src/
flake8 src/
```

### VS Code Setup
1. Install Python extension
2. Select Python interpreter (from venv)
3. Install recommended extensions:
   - Python
   - Pylance
   - Python Test Explorer

### Google Colab Testing
1. Upload `notebooks/vlm_testing.ipynb` to Colab
2. Enable GPU runtime (Runtime → Change runtime type → GPU)
3. Run cells to test VLM models
4. Export results and integrate

## 🚀 Deployment

### Streamlit Community Cloud (Recommended)

This app is deployed on Streamlit Community Cloud. To deploy your own instance:

1. **Fork this repository** to your GitHub account

2. **Sign up** for [Streamlit Community Cloud](https://streamlit.io/cloud) (free)

3. **Deploy the app:**
   - Click "New app" in your Streamlit Cloud dashboard
   - Select your forked repository
   - Set main file path: `app.py`
   - Click "Deploy"

4. **Configure secrets** (if using VLM features):
   - Go to app settings → Secrets
   - Add your API keys:
     ```toml
     OPENAI_API_KEY = "your-key-here"
     ```

5. **Access your app** at: `https://[your-username]-[repo-name]-app.streamlit.app`

### Alternative Deployment Options

#### Docker
```bash
# Build Docker image
docker build -t tactile-graphics .

# Run container
docker run -p 8501:8501 tactile-graphics
```

#### Local Server
```bash
# Install dependencies
pip install -r requirements.txt

# Run with Streamlit
streamlit run app.py --server.port 8501
```

#### Cloud Platforms
- **Heroku**: Use Streamlit's [deployment guide](https://docs.streamlit.io/knowledge-base/deploy/deploy-streamlit-heroku-aws-google-cloud)
- **AWS/GCP/Azure**: Deploy using container services (ECS, Cloud Run, App Service)
- **Railway**: Connect GitHub repo and deploy automatically

### Deployment Files

The repository includes these deployment configuration files:
- `.streamlit/config.toml` - Streamlit configuration
- `packages.txt` - System dependencies (for OpenCV)
- `requirements.txt` - Python dependencies

📚 **For detailed deployment instructions, see [DEPLOYMENT.md](DEPLOYMENT.md)**

## 📖 Documentation

### For Users
- See `docs/USER_GUIDE.md` (coming soon)
- Watch video tutorial (link coming soon)

### For Developers
- See `docs/DEVELOPER_GUIDE.md` (coming soon)
- API documentation: `docs/API.md` (coming soon)

### For Hardware Builders
- See `docs/HARDWARE_GUIDE.md` (coming soon)
- Circuit schematics: `hardware/schematics/` (coming soon)

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Inspired by refreshable braille display research
- VLM models from Hugging Face and OpenAI
- Streamlit for amazing web framework
- Open-source computer vision libraries

## 📞 Contact

**Project Maintainer**: Pathan Mohammad Rashid
- Email: mohammadrashid.pathan@iitgn.ac.in
- GitHub: [@Pathan-Mohammad-Rashid]((https://github.com/Pathan-Mohammad-Rashid))

## 🗺️ Roadmap

### Phase 1: Software (Current)
- ✅ Image-to-tactile conversion
- ✅ Streamlit web interface
- ✅ Multiple export formats
- 🔄 VLM integration (in progress)

### Phase 2: Hardware Prototype
- ⏳ 4×4 electromagnetic array
- ⏳ Arduino control system
- ⏳ Power management
- ⏳ Testing and refinement

### Phase 3: Enhanced Features
- ⏳ Real-time camera input
- ⏳ Text-to-braille conversion
- ⏳ Multi-level height control
- ⏳ Mobile app interface

### Phase 4: Scaling
- ⏳ Larger displays (16×16, 32×32)
- ⏳ Manufacturing optimization
- ⏳ Community distribution
- ⏳ Open-source hardware

## 🎓 Academic Context

This project is part of **"AI for Visual Accessibility: Description and Tactile Graphics"** research initiative, exploring how AI and physical computing can improve accessibility for visually impaired individuals.

### Key Research Questions
1. How can VLMs enhance tactile image conversion?
2. What resolution provides optimal tactile recognition?
3. How can we make tactile displays affordable and accessible?
4. What are the best practices for tactile graphic design?

### Publications
- Paper 1: "AI-Enhanced Tactile Graphics" (in preparation)
- Paper 2: "Low-Cost Refreshable Tactile Displays" (in preparation)

---

**Made with ❤️ for accessibility**

*If this project helps you or your organization, please consider giving it a ⭐ on GitHub!*
