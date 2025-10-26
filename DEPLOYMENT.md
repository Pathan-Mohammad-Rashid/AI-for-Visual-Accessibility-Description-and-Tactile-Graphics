# Deployment Guide

This guide provides detailed instructions for deploying the AI Visual Accessibility - Tactile Graphics application on various platforms.

## 🌐 Live Demo

The application is currently deployed at: [![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://pathan-mohammad-rashid-ai-for-visual-accessibility-app.streamlit.app)

## Quick Deployment Options

### Option 1: Streamlit Community Cloud (Recommended - FREE)

**Easiest and free option for public apps**

1. **Prerequisites:**
   - GitHub account
   - Fork of this repository

2. **Steps:**
   ```
   1. Visit https://streamlit.io/cloud
   2. Sign in with your GitHub account
   3. Click "New app"
   4. Select your forked repository
   5. Branch: main (or master)
   6. Main file path: app.py
   7. Click "Deploy"
   ```

3. **Configuration:**
   - The app will automatically detect `requirements.txt` and `packages.txt`
   - Your app will be live at: `https://[your-username]-[repo-name]-app.streamlit.app`

4. **Secrets (Optional):**
   If you want to use VLM features with API keys:
   ```
   1. Go to your app's settings
   2. Click on "Secrets"
   3. Add your secrets in TOML format:
   
   OPENAI_API_KEY = "your-key-here"
   ```

5. **Updating the App:**
   - Simply push changes to your GitHub repository
   - Streamlit Cloud will automatically redeploy

---

### Option 2: Docker Deployment

**For running on your own infrastructure**

1. **Build the Docker image:**
   ```bash
   docker build -t tactile-graphics .
   ```

2. **Run the container:**
   ```bash
   docker run -d -p 8501:8501 --name tactile-app tactile-graphics
   ```

3. **Access the app:**
   Open http://localhost:8501 in your browser

4. **With environment variables:**
   ```bash
   docker run -d -p 8501:8501 \
     -e OPENAI_API_KEY="your-key" \
     --name tactile-app \
     tactile-graphics
   ```

5. **Stop the container:**
   ```bash
   docker stop tactile-app
   docker rm tactile-app
   ```

---

### Option 3: Local Development Server

**For development and testing**

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the app:**
   ```bash
   streamlit run app.py
   ```

3. **Configure port (optional):**
   ```bash
   streamlit run app.py --server.port 8080
   ```

4. **Access the app:**
   Open http://localhost:8501 in your browser

---

### Option 4: Railway

**Quick deployment with automatic HTTPS**

1. **Prerequisites:**
   - Railway account (free tier available)
   - GitHub repository

2. **Steps:**
   ```
   1. Visit https://railway.app
   2. Sign in with GitHub
   3. Click "New Project"
   4. Select "Deploy from GitHub repo"
   5. Choose your repository
   6. Railway will auto-detect Streamlit and deploy
   ```

3. **Environment Variables:**
   - Add variables in Railway dashboard under "Variables" tab
   - Example: `OPENAI_API_KEY=your-key`

---

### Option 5: Heroku

**Traditional PaaS deployment**

1. **Prerequisites:**
   - Heroku account
   - Heroku CLI installed

2. **Create required files:**

   `setup.sh`:
   ```bash
   mkdir -p ~/.streamlit/
   echo "\
   [server]\n\
   headless = true\n\
   port = $PORT\n\
   enableCORS = false\n\
   \n\
   " > ~/.streamlit/config.toml
   ```

   `Procfile`:
   ```
   web: sh setup.sh && streamlit run app.py
   ```

3. **Deploy:**
   ```bash
   heroku create your-app-name
   git push heroku main
   heroku open
   ```

---

### Option 6: AWS (Advanced)

**For production deployments with custom infrastructure**

#### Using AWS Elastic Beanstalk:

1. **Install AWS CLI and EB CLI:**
   ```bash
   pip install awsebcli
   ```

2. **Initialize:**
   ```bash
   eb init -p docker your-app-name
   ```

3. **Create environment:**
   ```bash
   eb create production-env
   ```

4. **Deploy:**
   ```bash
   eb deploy
   ```

#### Using AWS ECS (Fargate):

1. Build and push Docker image to ECR
2. Create ECS cluster
3. Define task with your Docker image
4. Create service and configure load balancer
5. Access via Load Balancer DNS

---

### Option 7: Google Cloud Run

**Serverless container deployment**

1. **Prerequisites:**
   - Google Cloud account
   - gcloud CLI installed

2. **Build and deploy:**
   ```bash
   # Authenticate
   gcloud auth login
   
   # Set project
   gcloud config set project YOUR_PROJECT_ID
   
   # Build and deploy
   gcloud run deploy tactile-graphics \
     --source . \
     --platform managed \
     --region us-central1 \
     --allow-unauthenticated
   ```

3. **Access:**
   Google Cloud will provide a URL like: `https://tactile-graphics-xxx.run.app`

---

## Configuration Files

The repository includes these deployment configuration files:

### `.streamlit/config.toml`
```toml
[theme]
primaryColor = "#4CAF50"
backgroundColor = "#FFFFFF"
secondaryBackgroundColor = "#F0F2F6"
textColor = "#262730"

[server]
headless = true
port = 8501
enableCORS = false
```

### `packages.txt`
System dependencies for OpenCV:
```
libgl1-mesa-glx
libglib2.0-0
```

### `requirements.txt`
All Python dependencies are listed here.

---

## Environment Variables

### Required for VLM Features:
- `OPENAI_API_KEY`: Your OpenAI API key (optional)

### Optional Configuration:
- `DEBUG`: Set to "true" for debug mode
- `VERBOSE`: Set to "true" for verbose logging

---

## Troubleshooting

### Common Issues:

1. **OpenCV errors:**
   - Ensure `packages.txt` includes system dependencies
   - On Streamlit Cloud, this is handled automatically

2. **Memory issues:**
   - Reduce grid size or image resolution
   - Consider upgrading to a paid plan with more resources

3. **Slow startup:**
   - Large ML models take time to load
   - Consider using lighter models or disabling VLM features

4. **Port conflicts:**
   - Change the port using `--server.port` flag
   - Default is 8501

### Getting Help:

- Check [Streamlit documentation](https://docs.streamlit.io)
- Open an issue on GitHub
- Contact: mohammadrashid.pathan@iitgn.ac.in

---

## Deployment Checklist

- [ ] Fork/clone repository
- [ ] Choose deployment platform
- [ ] Configure environment variables (if needed)
- [ ] Deploy application
- [ ] Test all features
- [ ] Set up monitoring (optional)
- [ ] Configure custom domain (optional)
- [ ] Set up CI/CD (optional)

---

## Security Considerations

1. **API Keys:**
   - Never commit API keys to repository
   - Use environment variables or secrets management
   - Rotate keys regularly

2. **HTTPS:**
   - Most platforms provide HTTPS by default
   - Ensure SSL/TLS is enabled for production

3. **Access Control:**
   - Consider authentication for sensitive deployments
   - Use Streamlit's authentication features if needed

---

## Cost Considerations

| Platform | Free Tier | Paid Plans | Best For |
|----------|-----------|------------|----------|
| Streamlit Cloud | ✅ (public apps) | Starting at $20/month | Quick demos, public apps |
| Railway | ✅ ($5 credit) | Pay-as-you-go | Small projects |
| Heroku | ✅ (limited) | Starting at $7/month | Small to medium apps |
| AWS | ⚠️ (12 months) | Pay-as-you-go | Enterprise, scalability |
| GCP | ✅ ($300 credit) | Pay-as-you-go | Enterprise, ML workloads |
| Docker (self-host) | ✅ | Infrastructure costs | Full control |

---

## Next Steps

After deployment:

1. Test all functionality
2. Share the URL with users
3. Monitor performance and usage
4. Collect feedback
5. Iterate and improve

For questions or issues, please open an issue on GitHub or contact the maintainer.

---

**Happy Deploying! 🚀**
