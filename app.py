from flask import Flask, render_template, request
import joblib
import pandas as pd
import numpy as np

app = Flask(__name__)

# Load the trained model
try:
    model = joblib.load('model.pkl')
except FileNotFoundError:
    print("Error: model.pkl not found. Run train_model.py first.")
    exit()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        try:
            # Get data from form
            nitrogen = float(request.form['nitrogen'])
            phosphorus = float(request.form['phosphorus'])
            potassium = float(request.form['potassium'])
            temperature = float(request.form['temperature'])
            humidity = float(request.form['humidity'])
            ph_level = float(request.form['ph'])
            rainfall = float(request.form['rainfall'])

            # Prepare features for prediction
            features = np.array([[nitrogen, phosphorus, potassium, temperature, humidity, ph_level, rainfall]])
            
            # Make prediction
            prediction = model.predict(features)[0]
            
            return render_template('index.html', prediction=prediction)
        except Exception as e:
            return render_template('index.html', prediction=f"Error: {e}")

if __name__ == '__main__':
    app.run(debug=True)
