# Customer Churn Prediction using Machine Learning

**Crack404 AI/ML Internship | Week 1**

**Module:** Data Foundations & Classical Machine Learning  
**Project:** Customer Churn Prediction (Tabular Data)  
**Tech Stack:** Python, Pandas, NumPy, Scikit-learn, Matplotlib, Seaborn

## Project Overview

This project aims to predict customer churn using machine learning techniques. The primary objective is to identify customers who are likely to discontinue their services, allowing businesses to take proactive retention measures.

The project covers data preprocessing, exploratory data analysis (EDA), feature engineering, baseline model development, hyperparameter tuning, and recall-focused model evaluation.

## Dataset

**Dataset:** Telco Customer Churn

| Description | Value |
|---|---|
| Total Customers | 7,043 |
| Original Columns | 21 |
| Model Input Features | 22 |
| Churned Customers | 1,869 (26.54%) |
| Non-Churned Customers | 5,174 (73.46%) |
| Training Set | 80% |
| Testing Set | 20% |

## Methodology

**1. Data Preprocessing**
- Identified and handled 11 missing values in `TotalCharges`.
- Checked duplicates and performed categorical encoding.
- Explored StandardScaler and MinMaxScaler.
- Developed a preprocessing pipeline to prevent data leakage.

**2. Exploratory Data Analysis**
- Analyzed churn distribution and feature relationships.
- Generated correlation heatmaps and categorical/numerical visualizations.
- Investigated customer contract, tenure, payment, and service-related churn patterns.

**3. Feature Engineering**

Created three additional features:
- `EstimatedLifetimeBilling`
- `TenureGroup`
- `NumAddOnServices`

**4. Machine Learning Models**

Trained and evaluated:
- Logistic Regression
- Decision Tree Classifier
- Random Forest Classifier

**5. Model Optimization**
- Applied RandomizedSearchCV with Stratified Cross-Validation.
- Optimized Random Forest hyperparameters.
- Selected a classification threshold of **0.36** using validation data to prioritize churn recall.

## Final Model Performance

**Selected Model:** Tuned Random Forest Classifier

| Evaluation Metric | Test Result |
|---|---:|
| Accuracy | 65.44% |
| Precision | 42.86% |
| **Recall** | **90.64%** |
| F1-Score | 58.20% |
| F2-Score | 74.11% |
| ROC-AUC | 0.8404 |

**Confusion Matrix Results:**

| Metric | Count |
|---|---:|
| True Positive (TP) | 339 |
| True Negative (TN) | 583 |
| False Positive (FP) | 452 |
| False Negative (FN) | 35 |

The final model successfully identified **339 out of 374 actual churn customers**, achieving 90.64% recall. However, the high-recall approach also produced additional false-positive predictions.

## Feature Importance Analysis

The five strongest predictors identified through grouped Random Forest feature importance were:

| Rank | Feature | Importance |
|---|---|---:|
| 1 | Contract | 29.68% |
| 2 | OnlineSecurity | 10.92% |
| 3 | TechSupport | 9.51% |
| 4 | InternetService | 9.36% |
| 5 | TenureGroup | 8.16% |

**Key Business Insight:** Customers with month-to-month contracts, shorter tenure, and no online security or technical support showed comparatively higher churn rates. These are predictive associations rather than evidence of causation.

## Project Structure

The recommended Week 1 directory contains:

- `Customer_Churn_Prediction.ipynb` — Complete analysis and machine learning notebook
- `Telco-Customer-Churn.csv` — Customer churn dataset
- `requirements.txt` — Python dependencies
- `README.md` — Project documentation
- `outputs/` — Generated visualizations, evaluation results, feature importance, and `one_paragraph_summary.txt`

## How to Run

**Step 1:** Clone or download the project and open the `week_1` directory in VS Code.

**Step 2:** Create and activate a Python virtual environment.

**Step 3:** Install the required dependencies:

`python -m pip install -r requirements.txt`

**Step 4:** Open `Customer_Churn_Prediction.ipynb` in VS Code.

**Step 5:** Select the correct Python kernel and execute the notebook cells sequentially.

## Conclusion

This project demonstrates an end-to-end machine learning workflow for customer churn prediction. Through feature engineering, hyperparameter tuning, and validation-based threshold optimization, the final Random Forest model achieved **90.64% recall** on the unseen test dataset.

The model prioritizes identifying customers at risk of churn while acknowledging the trade-off between recall and precision.

---

**Crack404 AI/ML Internship — Week 1 Project**