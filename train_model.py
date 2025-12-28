import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib

# 1. Load Data
try:
    data = pd.read_csv("Crop_recommendation.csv")
    print("Data loaded successfully.")
except FileNotFoundError:
    print("Error: Crop_recommendation.csv not found.")
    exit()

# 2. Prepare Feature and Labels
x = data.iloc[:,:-1]  # features
y = data.iloc[:,-1]   # labels

# 3. Split Data
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

# 4. Train Model
print("Training Random Forest model...")
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(x_train, y_train)

# 5. Evaluate
y_pred = model.predict(x_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {accuracy:.4f}")

# 6. Save Model
joblib.dump(model, 'model.pkl')
print("Model saved to model.pkl")

# Note: Random Forest doesn't strictly require scaling, but if we were using 
# Logistic Regression, we would need to save the scaler too.
# For consistency with the previous plan, let's keep it simple as the user 
# preferred the Random Forest result anyway.
