# 🚀 AI/ML Internship

Welcome to my **AI/ML Internship Repository!**

This repository documents my weekly internship tasks, hands-on projects, and practical implementations completed during my **AI/ML Engineering Internship at Crack404**.

The projects focus on applying Artificial Intelligence and Machine Learning concepts to real-world problems, covering the complete workflow from data preprocessing and model development to model serialization and standalone inference.

## 🛠️ Technologies & Tools

- **Programming:** Python
- **Data Analysis:** NumPy, Pandas
- **Data Visualization:** Matplotlib, Seaborn
- **Machine Learning:** Scikit-learn
- **Model Serialization:** Pickle, Joblib
- **Development Environment:** Jupyter Notebook, VS Code
- **Version Control:** Git & GitHub

## 📂 Weekly Projects

### 📌 Week 1 — Customer Churn Prediction

**Module:** Data Foundations & Classical Machine Learning

Developed an end-to-end machine learning pipeline to predict customer churn using the Telco Customer Churn dataset.

**Key Implementations:**
- Data Cleaning and Preprocessing
- Exploratory Data Analysis (EDA)
- Feature Engineering and Feature Scaling
- Logistic Regression, Decision Tree, and Random Forest
- Hyperparameter Tuning using RandomizedSearchCV
- Classification Threshold Optimization
- Model Evaluation and Performance Comparison
- Feature Importance Analysis
- Business Insights and Final Documentation

**Key Results:**
- **Final Model:** Tuned Random Forest Classifier
- **Recall:** 90.64%
- **Accuracy:** 65.44%
- **F1-Score:** 58.20%
- **ROC-AUC:** 0.8404

The final model prioritized identifying customers at risk of churn while considering the trade-off between precision and recall.

📁 **[View Week 1 Project](./week_1)**

---

### 📌 Week 2 — Model Serialization & Standalone Inference

**Module:** Model Serialization, Persistence & Environment Management

Extended the Week 1 Customer Churn Prediction project by implementing model persistence and standalone inference using Python.

**Key Implementations:**
- Rebuilt and trained a Random Forest classification pipeline
- Model Serialization using Pickle and Joblib
- Model File Size Comparison
- Saved Model Loading and Verification
- Standalone Prediction using `predict.py`
- Customer Churn Probability Prediction
- Environment Management using `requirements.txt`
- Model Compatibility and Serialization Security Concepts

**Serialization Results:**

| Method | File | Size |
|---|---|---|
| Pickle | `model_v1.pkl` | 418.67 KB |
| Joblib | `model_v1.joblib` | 438.92 KB |

Both serialized models were successfully reloaded and produced matching predictions during verification.

**Standalone Inference Results:**
- **Model:** Random Forest Classifier
- **Input Features:** 22
- **Sample Churn Probability:** 83.01%
- **Classification Threshold:** 0.36
- **Sample Prediction:** Churn

Successfully implemented an independent Python inference script capable of loading the saved machine learning model and generating predictions without retraining or running a Jupyter Notebook.

📁 **[View Week 2 Project](./week_2)**

---

## 🎯 Internship Objectives

- Strengthen practical Artificial Intelligence and Machine Learning skills.
- Develop end-to-end machine learning solutions.
- Apply data preprocessing, feature engineering, and model optimization techniques.
- Understand model serialization, persistence, and inference workflows.
- Improve problem-solving, experimentation, and model evaluation skills.
- Learn professional project documentation and version control.
- Build a strong foundation for real-world AI/ML development and deployment.

## 📈 Learning Progress

| Week | Project | Status |
|---|---|---|
| Week 1 | Customer Churn Prediction | ✅ Completed |
| Week 2 | Model Serialization & Standalone Inference | ✅ Completed |

## 👨‍💻 Author

**Rasidul Hoque Chowdhury**

AI/ML Engineering Intern — Crack404

**GitHub:** [@therash08](https://github.com/therash08)

---

⭐ This repository will be updated with new projects, experiments, and practical implementations throughout my AI/ML internship.