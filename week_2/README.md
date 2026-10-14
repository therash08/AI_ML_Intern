# Customer Churn Prediction — Model Serialization & Standalone Inference

**Crack404 AI/ML Internship | Week 2**

**Module:** Model Serialization, Persistence & Environment Management  
**Project:** Exporting Models and Standalone Inference  
**Tech Stack:** Python, Scikit-learn, Pandas, NumPy, Pickle, Joblib

## 1. Project Overview

This project demonstrates how to serialize a trained Machine Learning model, save it to disk, and use it for predictions in a standalone Python application without retraining.

Building on the Week 1 Customer Churn Prediction project, a Random Forest classification pipeline was trained on the Telco Customer Churn dataset and exported using both Pickle and Joblib.

The saved model is subsequently loaded by an independent `predict.py` script to predict customer churn from new customer information.

## 2. Project Objectives

- Train and serialize a Random Forest model.
- Compare Pickle and Joblib serialization.
- Save and reload the complete preprocessing and classification pipeline.
- Build an independent Python prediction script.
- Generate predictions without opening a Jupyter Notebook.
- Preserve exact Python dependency versions.

## 3. Dataset and Model

**Dataset:** Telco Customer Churn

| Attribute | Details |
|---|---|
| Total Records | 7,043 |
| Original Features | 21 columns, including customer ID and target |
| Model Input Features | 22 |
| Training Samples | 5,634 |
| Testing Samples | 1,409 |
| Algorithm | Random Forest Classifier |
| Number of Trees | 150 |
| Maximum Depth | 4 |
| Classification Threshold | 0.36 |

The preprocessing pipeline includes missing-value handling, numerical scaling, and categorical encoding.

Three additional features were created: `EstimatedLifetimeBilling`, `TenureGroup`, and `NumAddOnServices`.

## 4. Model Serialization

The same trained model package was serialized using two Python libraries.

| Serialization Method | File Name | File Size |
|---|---|---:|
| Pickle | `model_v1.pkl` | 418.67 KB |
| Joblib | `model_v1.joblib` | 438.92 KB |

For this experiment, the Pickle file was slightly smaller than the Joblib file. File size depends on the serialized object, format, and compression settings.

Both saved models were successfully reloaded, and their prediction probabilities matched those produced by the original trained model on the verification samples.

The serialized package includes the trained pipeline, classification threshold, expected feature names, and environment version metadata.

## 5. Standalone Inference

A separate Python script, `predict.py`, was developed to demonstrate independent model inference.

The script loads `model_v1.joblib`, accepts a sample customer record, recreates the required engineered features, and generates a churn prediction using the trained model.

The script performs inference without retraining the classifier or requiring a Jupyter Notebook.

## 6. Sample Prediction Results

The standalone script was tested successfully with a synthetic customer record.

| Output | Result |
|---|---|
| Customer Tenure | 4 months |
| Contract Type | Month-to-month |
| Churn Probability | 83.01% |
| Classification Threshold | 0.36 |
| Final Prediction | **Churn** |

Because the estimated churn probability exceeded the selected threshold, the customer was classified as likely to churn.

This is an example model prediction on synthetic input, not an observed customer outcome or a measure of overall model accuracy.

## 7. Project Structure

| File | Description |
|---|---|
| `notebook.ipynb` | Model training, serialization, and verification |
| `model_v1.pkl` | Pickle-serialized model package |
| `model_v1.joblib` | Joblib-serialized model package |
| `predict.py` | Standalone customer churn predictor |
| `requirements.txt` | Exact installed dependency versions |
| `README.md` | Project documentation |

## 8. Environment Setup and Execution

**Step 1: Open the project directory**

`cd D:\Ai_Ml_intren\week_2`

**Step 2: Activate the existing virtual environment**

`..\.venv\Scripts\Activate.ps1`

**Step 3: Install project dependencies**

`python -m pip install -r requirements.txt`

**Step 4: Run standalone prediction**

`python predict.py`

The script loads the previously saved model and prints the predicted churn probability and classification label.

## 9. Key Dependencies

The verified environment includes:

| Library | Version |
|---|---|
| Pandas | 3.0.6 |
| NumPy | 2.5.4 |
| Scikit-learn | 1.9.1 |
| Joblib | 1.6.0 |

The complete dependency list is included in `requirements.txt`.

## 10. Technical Considerations

**Model Compatibility:** Serialized Scikit-learn models should be loaded using a compatible environment. Different library versions may cause errors or inconsistent behavior.

**Security:** Pickle and Joblib files must only be loaded from trusted sources because deserialization can execute arbitrary Python code.

**Inference Consistency:** New input data must use the same feature definitions, categorical values, and preprocessing logic used during training.

**Model Persistence:** The saved model can be reused without retraining, enabling integration with backend applications.

## 11. Conclusion

This project successfully demonstrates the complete workflow of model serialization, persistence, environment management, and standalone inference.

Both Pickle and Joblib serialization were verified, and the independent Python script successfully loaded the trained Random Forest pipeline and generated customer churn predictions.

The project provides a foundation for integrating machine learning models into backend applications and future deployment workflows.

---

**Crack404 AI/ML Internship — Week 2 Project**