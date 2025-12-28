# 🌱 Smart Crop Prediction AI

## 📖 Overview
**Smart Crop Prediction AI** is a machine learning-based web application designed to help farmers and agricultural enthusiasts make informed decisions about which crops to grow. By analyzing key soil and climate parameters, the system recommends the most suitable crop to maximize yield and efficiency.

This project leverages a **Random Forest** machine learning model trained on agricultural data to provide accurate real-time predictions through a user-friendly Flask we interface.

## ✨ Key Features
*   **Precision Agriculture**: Uses scientific data (N, P, K values, temperature, etc.) to recommend crops.
*   **High Accuracy**: Powered by a robust **Random Forest Classifier**.
*   **User-Friendly Interface**: Clean, modern, and responsive web UI for easy interaction.
*   **Real-time Predictions**: Instant results upon entering environmental data.

## 🛠️ Tech Stack
*   **Frontend**: HTML5, CSS3, JavaScript (responsive design).
*   **Backend**: Python, Flask.
*   **Machine Learning**: Scikit-Learn (Random Forest), Pandas, NumPy.
*   **Model Persistence**: Joblib.

## 📂 Dataset
The model works on the following input parameters:
*   **Nitrogen (N)** ratio in soil
*   **Phosphorus (P)** ratio in soil
*   **Potassium (K)** ratio in soil
*   **Temperature** (°C)
*   **Humidity** (%)
*   **pH Level** of the soil
*   **Rainfall** (mm)

## 🚀 How to Run
1.  **Clone the repository**:
    ```bash
    git clone https://github.com/amancodexz/Crop-Prediction-AI.git
    cd Crop_Predection
    ```

2.  **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3.  **Train the model** (Optional, if `model.pkl` is missing):
    ```bash
    python train_model.py
    ```

4.  **Run the application**:
    ```bash
    python app.py
    ```

5.  Open your browser and visit: `http://127.0.0.1:5000/`

## 🔮 Future Enhancements
*   Add more crop varieties and larger datasets.
*   Implement localized weather API integration to auto-fetch climate data.
*   Deploy to cloud platforms like Heroku or AWS.