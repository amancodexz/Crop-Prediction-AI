import os
from flask import Flask, render_template, request
import joblib
import pandas as pd
import numpy as np

app = Flask(__name__)

# Model loading with graceful fallback
MODEL_PATH = os.environ.get("MODEL_PATH", "model.pkl")
model = None
if os.path.exists(MODEL_PATH):
    try:
        model = joblib.load(MODEL_PATH)
        app.logger.info("Model loaded from %s", MODEL_PATH)
    except Exception:
        app.logger.exception("Failed to load model from %s", MODEL_PATH)
else:
    app.logger.warning("Model not found at %s; predictions will be disabled.", MODEL_PATH)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        try:
            # Parse inputs
            nitrogen = float(request.form['nitrogen'])
            phosphorus = float(request.form['phosphorus'])
            potassium = float(request.form['potassium'])
            temperature = float(request.form['temperature'])
            humidity = float(request.form['humidity'])
            ph_level = float(request.form['ph'])
            rainfall = float(request.form['rainfall'])

            if model is None:
                return render_template('index.html', prediction="Model not available. Please train the model.")

            # Prepare features with proper column names to avoid sklearn warnings
            cols = ['N','P','K','temperature','humidity','ph','rainfall']
            features = pd.DataFrame([[nitrogen, phosphorus, potassium, temperature, humidity, ph_level, rainfall]], columns=cols)

            # Make prediction
            prediction = model.predict(features)[0]
            return render_template('index.html', prediction=prediction)
        except ValueError:
            app.logger.exception("Invalid input values provided for prediction")
            return render_template('index.html', prediction="Invalid input values. Please check your inputs.")
        except Exception:
            app.logger.exception("Unexpected error during prediction")
            return render_template('index.html', prediction="Internal error. Please contact the administrator.")

if __name__ == '__main__':
    debug = os.environ.get("FLASK_DEBUG", "False").lower() in ("1", "true", "yes")
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=debug)
