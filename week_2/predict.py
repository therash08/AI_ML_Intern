

# =====================================================
# Crack404 AI/ML Internship - Week 2
# Phase 3: Standalone Customer Churn Prediction
# =====================================================

from pathlib import Path

import joblib
import pandas as pd


# -----------------------------------------------------
# Step 1: Load the saved model
# -----------------------------------------------------

model_path = Path(__file__).resolve().parent / "model_v1.joblib"

if not model_path.is_file():
    raise FileNotFoundError(
        f"Saved model not found: {model_path}"
    )

# Only load model files from trusted sources.
model_package = joblib.load(model_path)

model = model_package["model"]
threshold = model_package["threshold"]
feature_names = model_package["feature_names"]

print("Saved Model Loaded Successfully!")


# -----------------------------------------------------
# Step 2: Create fake new customer data
# -----------------------------------------------------

new_customer = [
    {
        "gender": "Male",
        "SeniorCitizen": 0,
        "Partner": "No",
        "Dependents": "No",
        "tenure": 4,
        "PhoneService": "Yes",
        "MultipleLines": "Yes",
        "InternetService": "Fiber optic",
        "OnlineSecurity": "No",
        "OnlineBackup": "No",
        "DeviceProtection": "No",
        "TechSupport": "No",
        "StreamingTV": "Yes",
        "StreamingMovies": "Yes",
        "Contract": "Month-to-month",
        "PaperlessBilling": "Yes",
        "PaymentMethod": "Electronic check",
        "MonthlyCharges": 95.50,
        "TotalCharges": 382.00
    }
]

customer_df = pd.DataFrame(new_customer)


# -----------------------------------------------------
# Step 3: Apply Week 1 feature engineering
# -----------------------------------------------------

customer_df["EstimatedLifetimeBilling"] = (
    customer_df["tenure"] * customer_df["MonthlyCharges"]
)

customer_df["TenureGroup"] = pd.cut(
    customer_df["tenure"],
    bins=[-1, 12, 24, 48, float("inf")],
    labels=[
        "New Customers (0-12)",
        "Short-Term (13-24)",
        "Mid-Term (25-48)",
        "Long-Term (49+)"
    ]
)

service_columns = [
    "OnlineSecurity",
    "OnlineBackup",
    "DeviceProtection",
    "TechSupport",
    "StreamingTV",
    "StreamingMovies"
]

customer_df["NumAddOnServices"] = (
    customer_df[service_columns].eq("Yes").sum(axis=1)
)


# -----------------------------------------------------
# Step 4: Match the training feature order
# -----------------------------------------------------

missing_features = [
    col for col in feature_names
    if col not in customer_df.columns
]

if missing_features:
    raise ValueError(
        f"Missing required features: {missing_features}"
    )

customer_df = customer_df[feature_names]


# -----------------------------------------------------
# Step 5: Predict customer churn probability
# -----------------------------------------------------

churn_probability = model.predict_proba(
    customer_df
)[0, 1]

prediction = int(churn_probability >= threshold)

prediction_label = (
    "Churn" if prediction == 1 else "No Churn"
)


# -----------------------------------------------------
# Step 6: Display prediction results
# -----------------------------------------------------

print("\n" + "=" * 50)
print("CUSTOMER CHURN PREDICTION")
print("=" * 50)

print("Model: Random Forest Classifier")
print("Input Features:", len(feature_names))
print("Customer Tenure:", new_customer[0]["tenure"])
print("Contract:", new_customer[0]["Contract"])

print("-" * 50)

print(f"Churn Probability: {churn_probability:.2%}")
print(f"Classification Threshold: {threshold:.2f}")
print(f"Final Prediction: {prediction_label}")

print("=" * 50)

print("\nSTANDALONE PREDICTION COMPLETED SUCCESSFULLY!")
