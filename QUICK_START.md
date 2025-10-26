# 🚀 QUICK START GUIDE
## AI for Visual Accessibility - Tactile Graphics

**Complete setup in 15 minutes on your Windows laptop!**

---

## ✅ STEP 1: Install Prerequisites (5 minutes)

### 1.1 Install Python 3.9+
1. Go to https://www.python.org/downloads/
2. Download Python 3.9 or higher
3. Run installer
4. **IMPORTANT**: Check ☑️ "Add Python to PATH"
5. Click "Install Now"

**Verify installation:**
```cmd
python --version
```
Should show: `Python 3.9.x` or higher

### 1.2 Install VS Code
1. Go to https://code.visualstudio.com/
2. Download for Windows
3. Run installer
4. Launch VS Code
5. Install Python extension:
   - Click Extensions icon (left sidebar)
   - Search "Python"
   - Install official Microsoft Python extension

### 1.3 Install Git (Optional but Recommended)
1. Go to https://git-scm.com/download/win
2. Download and install
3. Use default settings

---

## 📁 STEP 2: Create Project (2 minutes)

### 2.1 Create Project Folder
```cmd
cd C:\Users\YourName\Documents
mkdir AI-Visual-Accessibility
cd AI-Visual-Accessibility
```

### 2.2 Open in VS Code
```cmd
code .
```
This opens VS Code in your project folder.

---

## 🐍 STEP 3: Set Up Python Environment (3 minutes)

### 3.1 Create Virtual Environment
In VS Code, open Terminal (`Ctrl + ~` or Terminal menu):

```cmd
python -m venv venv
```

Wait for creation to complete...

### 3.2 Activate Virtual Environment
**Windows:**
```cmd
venv\Scripts\activate
```

You should see `(venv)` at the start of your terminal prompt.

### 3.3 Upgrade pip
```cmd
python -m pip install --upgrade pip
```

---

## 📦 STEP 4: Install Dependencies (5 minutes)

### 4.1 Create requirements.txt
In VS Code, create new file `requirements.txt` and paste this:

```txt
streamlit==1.31.0
Pillow==10.2.0
numpy==1.26.3
opencv-python==4.9.0.80
matplotlib==3.8.2
python-dotenv==1.0.0
```

### 4.2 Install Packages
```cmd
pip install -r requirements.txt
```

This takes 3-5 minutes. Wait for completion.

**Verify installation:**
```cmd
python -c "import streamlit; print('✓ Streamlit installed')"
python -c "import PIL; print('✓ PIL installed')"
python -c "import cv2; print('✓ OpenCV installed')"
```

---

## 📂 STEP 5: Create Project Structure (2 minutes)

### 5.1 Create Folders
In VS Code Terminal:
```cmd
mkdir src
mkdir assets
mkdir outputs
mkdir outputs\patterns
mkdir outputs\hardware_files
mkdir models
mkdir tests
mkdir notebooks
```

### 5.2 Create Files
Right-click in VS Code Explorer → New File:
- `app.py` (main Streamlit app)
- `config.py` (configuration)
- `src\tactile_converter.py` (converter logic)
- `.gitignore` (optional)

---

## 💻 STEP 6: Add Code Files

### 6.1 Copy app.py
Use the `app.py` file provided earlier.

### 6.2 Copy config.py
Use the `config.py` file provided earlier.

### 6.3 Copy src/tactile_converter.py
Use the `src-tactile_converter.py` file provided earlier.

**Note:** Remove the dash and save as `src/tactile_converter.py`

---

## 🎉 STEP 7: Run the Application!

### 7.1 Start Streamlit
In Terminal (with venv activated):
```cmd
streamlit run app.py
```

### 7.2 Open Browser
- Should automatically open `http://localhost:8501`
- If not, manually navigate to that address

### 7.3 Test It Out!
1. Upload a test image (any PNG/JPG)
2. Select grid size (start with 4×4)
3. Click "Convert to Tactile Pattern"
4. See the results!
5. Download the hardware file

---

## 🔧 TROUBLESHOOTING

### Issue: "Python not found"
**Solution:** Reinstall Python with "Add to PATH" checked

### Issue: "Module not found: streamlit"
**Solution:** 
```cmd
venv\Scripts\activate
pip install streamlit
```

### Issue: "ImportError: libGL.so.1"
**Solution:** This is a Linux error. On Windows, install:
```cmd
pip install opencv-python-headless
```

### Issue: Port 8501 already in use
**Solution:**
```cmd
streamlit run app.py --server.port 8502
```

### Issue: "Cannot import config"
**Solution:** Make sure `config.py` is in the same folder as `app.py`

---

## 🎯 WHAT TO DO NEXT

### Immediate (Today)
1. ✅ Test the app with sample images
2. ✅ Try different grid sizes (4×4, 8×8)
3. ✅ Experiment with processing methods
4. ✅ Download some hardware files

### This Week
1. Add your own test images
2. Customize the UI colors/theme
3. Read through the code to understand it
4. Share with team/classmates for feedback

### Next Week (Session 2)
1. Start hardware component research
2. Source 3mm magnetic balls
3. Plan electromagnetic control system
4. Design circuit schematics

---

## 🤖 ADDING AI/VLM SUPPORT (OPTIONAL)

### Option A: OpenAI GPT-4 Vision (Paid)
1. Get API key from https://platform.openai.com/
2. Create `.env` file in project root:
   ```
   OPENAI_API_KEY=your-api-key-here
   ```
3. Enable VLM in app sidebar
4. Select "OpenAI GPT-4V" backend

### Option B: Open-Source VLM (Free, needs GPU)
1. Open Google Colab: https://colab.research.google.com/
2. Upload `notebooks/vlm_testing.ipynb`
3. Enable GPU (Runtime → Change runtime type → GPU)
4. Run cells to test models
5. Export best configuration

### Option C: Skip AI for Now (Recommended)
- Start with traditional computer vision (no AI)
- Works perfectly without VLM
- Add AI later when you're ready

---

## 📚 RESOURCES

### Documentation
- **Streamlit Docs**: https://docs.streamlit.io/
- **PIL Docs**: https://pillow.readthedocs.io/
- **OpenCV Docs**: https://docs.opencv.org/

### Tutorials
- **Python Tutorial**: https://www.python.org/about/gettingstarted/
- **VS Code Python**: https://code.visualstudio.com/docs/python/python-tutorial
- **Streamlit Tutorial**: https://docs.streamlit.io/get-started/tutorials

### Community
- **Stack Overflow**: https://stackoverflow.com/questions/tagged/streamlit
- **Streamlit Community**: https://discuss.streamlit.io/

---

## 📋 CHECKLIST

Before moving to Session 2, make sure you have:

- [ ] Python 3.9+ installed and working
- [ ] VS Code installed with Python extension
- [ ] Virtual environment created and activated
- [ ] All dependencies installed (`pip list` shows streamlit, etc.)
- [ ] Project structure created (src/, outputs/, etc.)
- [ ] All code files copied and saved
- [ ] App runs successfully (`streamlit run app.py`)
- [ ] Browser opens and shows the UI
- [ ] Can upload and process an image
- [ ] Can download hardware files
- [ ] Understand basic workflow

**All checked?** → You're ready for Session 2! 🎉

---

## 🆘 GETTING HELP

### If You're Stuck:
1. Read error messages carefully
2. Check this guide again
3. Google the error message
4. Ask on Streamlit Community
5. Check Stack Overflow

### Common Commands Reference:
```cmd
# Activate virtual environment
venv\Scripts\activate

# Install package
pip install package-name

# List installed packages
pip list

# Run Streamlit app
streamlit run app.py

# Check Python version
python --version

# Upgrade pip
python -m pip install --upgrade pip
```

---

## ✨ SUCCESS!

If your app is running, **CONGRATULATIONS!** 🎉

You've successfully:
✅ Set up a complete Python development environment
✅ Created a working Streamlit web application
✅ Implemented image-to-tactile conversion
✅ Generated hardware-ready files
✅ Built your first AI accessibility tool

**Next**: Head to Session 2 for hardware design!

---

**Questions?** Create an issue on GitHub or ask your instructor.

**Good luck!** 🚀👁️