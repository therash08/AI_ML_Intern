 
<div align="center">

# 🚀 AI/ML Engineering Internship

### Crack404 | Weekly Projects & Practical Learning

![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python)
![Machine Learning](https://img.shields.io/badge/Machine-Learning-orange)
![Deep Learning](https://img.shields.io/badge/Deep-Learning-red)
![PyTorch](https://img.shields.io/badge/PyTorch-Framework-EE4C2C?logo=pytorch)
![Progress](https://img.shields.io/badge/Completed-Weeks%201--4-brightgreen)

**A collection of hands-on AI and Machine Learning projects completed during my AI/ML Engineering Internship at Crack404.**

[GitHub Profile](https://github.com/therash08) | [Repository](https://github.com/therash08/AI_ML_Intern)

</div>

---

## 📖 About This Repository

This repository documents my practical learning journey as an **AI/ML Engineering Intern at Crack404**.

The internship focuses on developing real-world Artificial Intelligence and Machine Learning solutions through weekly projects, technical experiments, model development, evaluation, and deployment-oriented workflows.

Each week introduces different concepts, ranging from classical machine learning to deep learning and Natural Language Processing.

### Areas Covered

- Data Cleaning and Exploratory Data Analysis
- Feature Engineering and Machine Learning
- Model Training, Optimization and Evaluation
- Model Serialization and Standalone Inference
- Computer Vision and Optical Character Recognition
- Natural Language Processing
- Deep Learning with PyTorch
- Model Checkpointing and Reproducibility
- Git, GitHub and Technical Documentation

---

## 📊 Internship Progress

| Week | Project | Main Technologies | Status |
|---|---|---|---|
| Week 01 | Customer Churn Prediction | Python, Pandas, Scikit-learn | ✅ Completed |
| Week 02 | Model Serialization & Prediction | Pickle, Joblib, Random Forest | ✅ Completed |
| Week 03 | Receipt & Invoice Digitization | OpenCV, EasyOCR | ✅ Completed |
| Week 04 | Automated Sentiment Analysis | NLP, PyTorch, Deep Learning | ✅ Completed |

**Current Progress: 4 Weeks Completed**

---

# 📌 Week 01 — Customer Churn Prediction

### Project: Telecom Customer Churn Analysis and Prediction

**Objective:** Develop a machine learning model to predict whether a telecom customer is likely to leave the company.

### Dataset

IBM Telco Customer Churn Dataset

- Total records: **7,043**
- Target variable: `Churn`
- Customer churn rate: **26.54%**
- Non-churn rate: **73.46%**

### Tasks Completed

**1. Data Understanding and Cleaning**

- Imported and explored the customer churn dataset.
- Checked missing values, duplicates, and data types.
- Converted `TotalCharges` into a numeric format.
- Handled 11 missing `TotalCharges` values.
- Analyzed the target class distribution.

**2. Exploratory Data Analysis**

Investigated churn behavior across:

- Customer tenure
- Monthly and total charges
- Contract types
- Internet services
- Online security
- Technical support
- Additional telecom services

**3. Feature Engineering**

Created additional features:

- `EstimatedLifetimeBilling`
- `TenureGroup`
- `NumAddOnServices`

**4. Machine Learning Models**

Implemented and compared:

- Logistic Regression
- Decision Tree Classifier
- Random Forest Classifier

**5. Model Optimization**

- Performed hyperparameter tuning with `RandomizedSearchCV`.
- Evaluated classification thresholds.
- Selected a decision threshold of **0.36**.
- Prioritized recall to identify more potential churn customers.

### Final Model Performance

| Evaluation Metric | Result |
|---|---|
| Accuracy | 65.44% |
| Precision | 42.86% |
| Recall | **90.64%** |
| F1-Score | 58.20% |
| ROC-AUC | **0.8404** |
| Classification Threshold | 0.36 |

### Key Findings

- Month-to-month customers had significantly higher churn.
- Long-term contracts were associated with lower churn.
- Customers without online security and technical support showed higher churn tendencies.
- Tenure was an important predictor of customer retention.
- The optimized Random Forest achieved high recall but lower precision, indicating a trade-off between capturing churn cases and producing false-positive alerts.

### Learning Outcomes

- Dataset exploration and preprocessing
- Feature engineering
- Class imbalance analysis
- Model comparison
- Hyperparameter optimization
- Classification evaluation
- Business-oriented interpretation of model predictions

📂 [Explore Week 01](./week_1)

---

# 📌 Week 02 — Model Serialization and Standalone Inference

### Project: Customer Churn Model Persistence

**Objective:** Save a trained machine learning model and reuse it for predictions without retraining.

### Tasks Completed

**1. Model Training**

- Rebuilt the customer churn prediction pipeline.
- Trained a Random Forest Classifier.
- Used 22 input features.
- Preserved preprocessing and prediction requirements.

**2. Model Serialization**

Exported the trained model using:

- Python Pickle
- Joblib

Generated model artifacts:

| Model File | Size |
|---|---|
| `model_v1.pkl` | 418.67 KB |
| `model_v1.joblib` | 438.92 KB |

**3. Model Verification**

- Loaded both saved models.
- Compared prediction outputs.
- Confirmed matching predictions.
- Verified model persistence.

**4. Standalone Prediction Script**

Developed:

`predict.py`

The script allows predictions using the saved model without performing model training again.

**5. Environment Management**

- Created and used a Python virtual environment.
- Documented dependencies in `requirements.txt`.
- Tested model loading and inference functionality.

### Example Prediction Result

| Property | Value |
|---|---|
| Algorithm | Random Forest |
| Input Features | 22 |
| Predicted Churn Probability | 83.01% |
| Threshold | 0.36 |
| Prediction | Churn |

**Note:** The 83.01% result represents the model-estimated churn probability of one sample customer, not overall model accuracy.

### Learning Outcomes

- Model serialization
- Saving and loading trained pipelines
- Pickle and Joblib comparison
- Environment dependency management
- Prediction pipeline verification
- Standalone model inference
- Reproducibility and model portability

📂 [Explore Week 02](./week_2)

---

# 📌 Week 03 — Automated Receipt and Invoice Digitization

### Project: Receipt Extractor Using Computer Vision and OCR

**Objective:** Build an automated system that processes receipt images and extracts readable text using Optical Character Recognition.

### Technologies

- Python
- OpenCV
- EasyOCR
- NumPy
- JSON
- Jupyter Notebook

### Tasks Completed

**1. Image Collection**

- Collected 5 receipt images.
- Organized the original images in `raw_images/`.
- Included challenging receipt images for OCR testing.

**2. Image Preprocessing**

Applied different image-processing techniques:

- Grayscale conversion
- Gaussian blur
- Global thresholding
- Adaptive thresholding
- Image enhancement and cleaning

**3. OCR Implementation**

- Applied EasyOCR to original receipt images.
- Applied EasyOCR to cleaned receipt images.
- Extracted text and bounding-box coordinates.
- Collected confidence scores for detected text.

**4. OCR Comparison**

Compared OCR outputs from original and preprocessed images.

The analysis showed that preprocessing did not consistently improve OCR confidence.

**5. Structured Data Export**

Generated:

`outputs/ocr_results.json`

The output contains extracted text, confidence scores, bounding-box information, and review flags.

**6. Standalone OCR Pipeline**

Developed:

`ocr_pipeline.py`

The script performs OCR processing independently of the experimental notebook.

### Final Results

| Measurement | Result |
|---|---|
| Original Receipt Images | 5 |
| Processed Receipt Images | 5 |
| Raw Image OCR Regions | 329 |
| Processed Image OCR Regions | 317 |
| Low-Confidence Detections | 291 |
| OCR JSON Validation | Passed |
| Standalone Pipeline Verification | Passed |

### OCR Confidence Comparison

| Receipt | Original Image | Processed Image |
|---|---|---|
| Receipt 01 | 88.66% | 69.30% |
| Receipt 02 | 78.67% | 50.41% |
| Receipt 03 | 73.16% | 59.05% |
| Receipt 04 | 62.62% | 40.64% |
| Receipt 05 | 49.28% | 38.61% |

### Key Findings

- OCR performance depends heavily on image quality.
- Aggressive thresholding may negatively affect character recognition.
- Raw images sometimes provide higher OCR confidence than cleaned images.
- OCR confidence alone cannot guarantee extraction accuracy.
- Low-confidence fields should be manually reviewed before use in financial or business applications.

### Learning Outcomes

- Computer vision fundamentals
- Image preprocessing
- OCR model integration
- Bounding-box visualization
- Confidence-based result analysis
- JSON data exporting
- Standalone automation pipelines

📂 [Explore Week 03](./week_3)

---

# 📌 Week 04 — Automated Sentiment Analysis Using Deep Learning

### Project: IMDb Review Sentiment Classification

**Objective:** Develop an end-to-end Natural Language Processing system capable of classifying movie reviews into positive and negative sentiment using a PyTorch neural network.

### Technologies

- Python
- Pandas
- NumPy
- NLTK
- Scikit-learn
- PyTorch
- Matplotlib
- Jupyter Notebook

## Phase 1 — Dataset Exploration and Preprocessing

### Dataset Information

IMDb Movie Review Dataset

| Property | Value |
|---|---|
| Original Reviews | 50,000 |
| Duplicate Reviews Removed | 418 |
| Unique Reviews | 49,582 |
| Classification Type | Binary Sentiment |
| Classes | Positive / Negative |

### Tasks Completed

- Imported the dataset.
- Examined class distributions.
- Identified duplicate reviews.
- Removed duplicate entries.
- Checked dataset consistency.
- Created reproducible stratified data splits.
- Prevented exact cross-split review overlap.

### Dataset Splitting

| Dataset | Samples |
|---|---|
| Training | 39,665 |
| Validation | 4,958 |
| Testing | 4,959 |
| Total | 49,582 |

---

## Phase 2 — NLP Text Preprocessing

Implemented a text preprocessing pipeline including:

1. HTML and URL cleaning
2. Text normalization
3. Tokenization
4. Stopword filtering
5. Negation preservation
6. Snowball English stemming
7. Vocabulary construction
8. Word-to-index conversion
9. Sequence encoding
10. Padding and truncation

### Vocabulary Configuration

| Parameter | Value |
|---|---|
| Selected Vocabulary Words | 30,000 |
| Special Tokens | PAD, UNK |
| Final Vocabulary Size | 30,002 |
| Maximum Sequence Length | 298 |

The vocabulary was constructed using training data only to avoid information leakage.

---

## Phase 3 — Neural Network Architecture

Developed a deep learning model using PyTorch.

### Model Components

- Embedding Layer
- Padding-Masked Mean Pooling
- Fully Connected Hidden Layer
- ReLU Activation
- Dropout
- Final Linear Output Layer
- Sigmoid-based Probability Interpretation

### Architecture Configuration

| Component | Configuration |
|---|---|
| Vocabulary Size | 30,002 |
| Embedding Dimension | 128 |
| Hidden Layer Units | 128 |
| Dropout Rate | 0.30 |
| Output Classes | 2 |
| Trainable Parameters | 3,856,897 |

The model was designed for binary sentiment classification using a single output logit.

---

## Phase 4 — Model Training

### Training Configuration

- Framework: PyTorch
- Optimizer: Adam
- Loss Function: `BCEWithLogitsLoss`
- Batch Size: 128
- Learning Rate Scheduling
- Gradient Clipping
- Early Stopping
- Best Model Checkpoint Saving

### Training Results

| Property | Result |
|---|---|
| Training Epochs Completed | 7 |
| Best Checkpoint | Epoch 4 |
| Best Validation Accuracy | 88.75% |
| Best Validation Loss | 0.2766 |

The best checkpoint was selected based on validation loss.

---

## Phase 5 — Model Evaluation and Testing

Evaluated the best model using the untouched test dataset.

### Final Test Performance

| Evaluation Metric | Result |
|---|---|
| Test Accuracy | **88.43%** |
| Test Precision | **89.26%** |
| Test Recall | **87.46%** |
| Test F1-Score | **88.35%** |
| Test ROC-AUC | **0.9550** |
| Test Loss | **0.2754** |
| Correct Predictions | 4,385 |
| Incorrect Predictions | 574 |

Precision, recall, and F1-score refer to the positive sentiment class.

### Confusion Matrix

| Actual / Predicted | Negative | Positive |
|---|---|---|
| Negative | 2,208 | 262 |
| Positive | 312 | 2,177 |

### Evaluation Visualizations

Generated and analyzed:

- Training Loss Curve
- Validation Loss Curve
- Training and Validation Accuracy
- Confusion Matrix
- ROC Curve
- Classification Report

### Model Interpretation

The model achieved 88.43% test accuracy and a ROC-AUC score of 0.9550, demonstrating strong sentiment classification performance on the held-out IMDb dataset.

The similar validation and test accuracies provide a useful indication of generalization within this dataset.

---

## Phase 6 — Custom Predictions and Model Export

### Custom Sentiment Prediction

Tested the trained model on three newly written review examples.

| Test | Expected | Prediction |
|---|---|---|
| Positive Review | Positive | Positive |
| Negative Review | Negative | Negative |
| Mixed but Positive Review | Positive | Positive |

**Custom Prediction Verification: 3/3 Passed**

### Model Export

Saved reusable inference artifacts including:

- Model weights
- Vocabulary mappings
- Inference configuration
- Preprocessing settings
- Prediction outputs
- Final evaluation reports

### Independent Inference Verification

- Reloaded exported model weights.
- Performed independent CPU inference.
- Compared predictions with the original model outputs.
- Verified matching sentiment classifications.
- Checked numerical consistency of prediction probabilities.

### Final Deliverables

- Completed Jupyter Notebook
- Trained Sentiment Classification Model
- Saved Model Checkpoint
- Exported Model Weights
- Vocabulary and Inference Configuration
- Test Predictions
- Performance Metrics
- Evaluation Visualizations
- Custom Prediction Examples
- Final Reports and Submission Artifacts

### Week 4 Key Findings

- Effective preprocessing is essential for NLP.
- Vocabulary and sequence preparation directly affect neural network input quality.
- Word embeddings provide learnable numerical representations of text.
- Early stopping helps select a model based on validation performance.
- Held-out testing gives a more reliable estimate of performance than training accuracy.
- Independent model loading and inference are important for reproducibility.
- Results on movie reviews should not be assumed to generalize automatically to unrelated text domains.

### Week 4 Learning Outcomes

- NLP preprocessing pipelines
- Vocabulary engineering
- Sequence encoding
- Word embeddings
- Neural network architecture design
- PyTorch training workflows
- Model optimization and regularization
- Validation-based checkpoint selection
- Binary classification evaluation
- Model exporting and reloading
- Independent inference verification

📂 [Explore Week 04](./week_4)

---

# 📁 Repository Structure

```text
AI_ML_Intern/
│
├── README.md
│
├── week_1/
│   ├── README.md
│   ├── Telco-Customer-Churn.csv
│   ├── requirements.txt
│   └── outputs/
│
├── week_2/
│   ├── README.md
│   ├── notebook.ipynb
│   ├── model_v1.pkl
│   ├── model_v1.joblib
│   ├── predict.py
│   └── requirements.txt
│
├── week_3/
│   ├── notebook.ipynb
│   ├── raw_images/
│   ├── cleaned_images/
│   ├── ocr_pipeline.py
│   └── outputs/
│       └── ocr_results.json
│
└── week_4/
    ├── notebook.ipynb
    └── outputs/
        ├── architecture/
        ├── checkpoints/
        ├── config/
        ├── encoded_sequences/
        ├── preprocessed/
        ├── training/
        ├── testing/
        ├── vocabulary/
        ├── reports/
        └── submission/
            ├── model_bundle/
            └── screenshots/
```

**Note:** This structure highlights the main project components. Large datasets, generated artifacts, and local dependencies may be excluded from version control.

---

# ⚙️ Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/therash08/AI_ML_Intern.git
cd AI_ML_Intern
```

### 2. Create a Python Virtual Environment

```bash
python -m venv .venv
```

### 3. Activate the Environment

Windows Git Bash:

```bash
source .venv/Scripts/activate
```

### 4. Install Dependencies

For the Week 2 churn model:

```bash
python -m pip install -r week_2/requirements.txt
```

For OCR experimentation:

```bash
python -m pip install opencv-python easyocr
```

For Week 4 NLP experimentation:

```bash
python -m pip install numpy pandas scikit-learn matplotlib nltk nbformat jupyter
```

Install a compatible PyTorch version using the [official PyTorch installation instructions](https://pytorch.org/get-started/locally/).

### 5. Run the Projects

Week 2 standalone churn prediction:

```bash
python week_2/predict.py
```

Week 3 OCR pipeline:

```bash
python week_3/ocr_pipeline.py
```

Week 4 Jupyter Notebook:

```bash
jupyter notebook week_4/notebook.ipynb
```

**Reproducibility note:** Some projects require original datasets and locally generated model files. Ensure the expected inputs are present before rerunning the complete training pipeline. Only load serialized model files from trusted sources.

---

# 🛠️ Technical Skills Developed

| Category | Skills |
|---|---|
| Programming | Python |
| Data Analysis | Pandas, NumPy |
| Data Visualization | Matplotlib, Seaborn |
| Machine Learning | Scikit-learn, Random Forest, Logistic Regression |
| Hyperparameter Tuning | RandomizedSearchCV |
| Model Persistence | Pickle, Joblib |
| Computer Vision | OpenCV |
| OCR | EasyOCR |
| NLP | NLTK, Tokenization, Stemming, Vocabulary Construction |
| Deep Learning | PyTorch, Embeddings, Neural Networks |
| Model Evaluation | Accuracy, Precision, Recall, F1, ROC-AUC |
| Development Tools | VS Code, Jupyter Notebook |
| Version Control | Git, GitHub |

---

# 📈 Internship Summary

During the first four weeks of this internship, I worked on four practical projects covering different areas of Artificial Intelligence and Machine Learning.

**Week 1:** Built and evaluated a telecom customer churn prediction system using classical machine learning.

**Week 2:** Implemented model persistence and standalone prediction using saved machine learning pipelines.

**Week 3:** Developed an OCR-based receipt digitization workflow using computer vision and text extraction.

**Week 4:** Built, trained, evaluated, and exported a deep-learning-based sentiment analysis system using PyTorch.

These projects strengthened my understanding of the complete machine learning lifecycle, from data preprocessing and model development to evaluation, artifact management, and reproducible inference.

---

# 📅 Progress Log

| Milestone | Progress |
|---|---|
| Week 01 — Customer Churn Prediction | Completed |
| Week 02 — Model Serialization | Completed |
| Week 03 — OCR Receipt Extractor | Completed |
| Week 04 — NLP Sentiment Analysis | Completed |

**Last Updated: November 7, 2026**

---

# 👨‍💻 Author

**Rasidul Hoque Chowdhury**

AI/ML Engineering Intern — Crack404

Computer Science and Engineering

[GitHub](https://github.com/therash08)

---

<div align="center">

### ⭐ AI/ML Engineering Internship Journey

*Learning, experimenting, implementing, and improving through real-world AI projects.*

**More projects and updates will be added as the internship progresses.**

</div>
