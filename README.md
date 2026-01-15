# Crop-Prediction-AI

Simple crop recommendation demo using a trained scikit-learn model and a small Flask app.

## Quickstart (local)

1. Create and activate a virtual environment (Windows example):

   ```powershell
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```

2. Install dependencies:

   ```powershell
   pip install -r requirements.txt
   ```

3. Train the model (generates `model.pkl`):

   ```powershell
   python train_model.py
   ```

4. Run the Flask app locally:

   ```powershell
   # optional: enable debug mode
   $env:FLASK_DEBUG = "True"
   python app.py
   ```

5. Open http://127.0.0.1:5000 in your browser.

## Notes
- `model.pkl` is ignored by `.gitignore` and should be stored externally for deployments or uploaded as an artifact.
- For production deployment use a WSGI server (e.g., Gunicorn) and proper environment configuration.

## Troubleshooting
- If the app shows "Model not available", run `python train_model.py` to create `model.pkl`.
- Use `MODEL_PATH` environment variable to point the app to a different model path.

---

Created/updated by GitHub Copilot (Raptor mini (Preview)).

---

## 🚀 Deployment (How to fix the "Static Demo" error)

To make the AI work online, you need to deploy this to a service that supports Python (GitHub Pages does not).

### Deploy on Render (Free)
1. Fork this repository to your GitHub.
2. Sign up at [render.com](https://render.com).
3. Create a **New Web Service**.
4. Connect your GitHub repository.
5. **Important Settings**:
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `gunicorn app:app`
6. Click **Deploy**.

Once deployed, Render will give you a new URL (e.g., `https://crop-prediction-ai.onrender.com`). Use that link instead of GitHub Pages!