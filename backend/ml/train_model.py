import os
import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_absolute_error, r2_score

# ==========================================
# Configuration & Paths
# ==========================================
# Resolve exact paths so the script works no matter where you run it from
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATASET_PATH = os.path.join(BASE_DIR, "dataset.csv")
MODEL_PATH = os.path.join(BASE_DIR, "aqi_forecast.pkl")
SCALER_PATH = os.path.join(BASE_DIR, "scaler.pkl")

# Define the columns the AI will learn from
# Change these lines in train_model.py (Line 16-17 roughly):
FEATURES = ["Temperature", "Humidity", "WindSpeed"]
TARGET = "AQI"

# ==========================================
# Training Pipeline
# ==========================================

def train_aqi_model():
    print("🚀 Initializing Machine Learning Pipeline...")

    # 1. Load Data
    if not os.path.exists(DATASET_PATH):
        print(f"❌ Error: Dataset not found at {DATASET_PATH}")
        return

    df = pd.read_csv(DATASET_PATH)
    
    # 2. Prepare Features (X) and Target (y)
    # Drop rows with missing values to ensure clean training
    df = df.dropna(subset=FEATURES + [TARGET])
    X = df[FEATURES]
    y = df[TARGET]

    # 3. Split the data (80% for learning, 20% for testing the AI's accuracy)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # 4. Scale the data (Standardizes the numbers so the AI learns efficiently)
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    # 5. Train the Algorithm
    print("🧠 Training Random Forest Regressor...")
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train_scaled, y_train)

    # 6. Evaluate Accuracy
    predictions = model.predict(X_test_scaled)
    mae = mean_absolute_error(y_test, predictions)
    accuracy = r2_score(y_test, predictions) * 100

    print(f"✅ Training Complete!")
    print(f"📊 Model Accuracy (R2 Score): {accuracy:.2f}%")
    print(f"📉 Mean Absolute Error: ±{mae:.2f} AQI points")

    # 7. Export the Model and Scaler to .pkl files
    joblib.dump(model, MODEL_PATH)
    joblib.dump(scaler, SCALER_PATH)
    print("💾 Model and Scaler successfully saved to disk.")

if __name__ == "__main__":
    train_aqi_model()