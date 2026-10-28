🚀 AI/ML Internship
Welcome to my AI/ML Internship Repository!

This repository documents my weekly internship assignments, hands-on projects, experiments, and practical implementations completed during my AI/ML Engineering Internship at Crack404.

The projects explore real-world AI/ML workflows, from data cleaning, feature engineering, and model evaluation to serialization, standalone inference, computer vision, and optical character recognition (OCR).
🛠️ Technologies & Tools
- Programming: Python
- Data Processing: NumPy, Pandas
- Data Visualization: Matplotlib, Seaborn
- Machine Learning: Scikit-learn
- Model Serialization: Pickle, Joblib
- Computer Vision & Image Processing: OpenCV
- OCR & Deep Learning: EasyOCR, PyTorch
- Data Export: JSON
- Development Environment: Jupyter Notebook, VS Code
- Version Control: Git & GitHub
📂 Weekly Projects
📌 Week 1 - Customer Churn Prediction
Module: Data Foundations & Classical Machine Learning

Developed an end-to-end machine learning pipeline to predict customer churn using the Telco Customer Churn dataset, with an emphasis on detecting customers at risk of leaving.

Key Implementations:
- Data cleaning, missing-value handling, and categorical encoding
- Exploratory Data Analysis (EDA) and feature engineering
- Feature scaling and leakage-aware train/validation/test splitting
- Logistic Regression, Decision Tree, and Random Forest baselines
- Hyperparameter tuning using RandomizedSearchCV
- Classification threshold optimization with recall-focused evaluation
- Confusion matrix, classification metrics, and feature importance analysis
- Business insights and documentation
Final held-out test results:
Metric	Result
Model	Tuned Random Forest Classifier
Recall	90.64%
Accuracy	65.44%
Precision	42.86%
F1-Score	58.20%
ROC-AUC	0.8404


Key takeaway: A lower classification threshold improved churn recall, but increased false positives, illustrating the trade-off between recall and precision.

View Week 1 Project
📌 Week 2 - Model Serialization & Standalone Inference
Module: Model Serialization, Persistence & Environment Management

Rebuilt and trained a Random Forest pipeline using the Week 1 preprocessing approach and tuned settings, then demonstrated how to persist and reuse a trained model independently of a notebook.

Key Implementations:
- Rebuilt and trained a Random Forest classification pipeline
- Saved the same Week 2 trained pipeline using Pickle and Joblib
- Compared serialized file sizes and verified matching predictions after loading
- Created a standalone predict.py script using the Joblib artifact
- Predicted customer churn from 22 input features
- Stored a decision threshold and model metadata with the saved pipeline
- Captured dependencies in requirements.txt
- Reviewed model compatibility and deserialization security considerations
Serialization Results:
Method	File	Size
Pickle	model_v1.pkl	418.67 KB
Joblib	model_v1.joblib	438.92 KB


Both models were successfully reloaded and produced predictions matching the original Week 2 pipeline.

Standalone Inference Example:
- Model: Random Forest Classifier
- Input Features: 22
- Sample Churn Probability: 83.01%
- Classification Threshold: 0.36
- Predicted Class: Churn
The 83.01% figure is the model's estimated probability for one synthetic customer, not test accuracy.

View Week 2 Project
📌 Week 3 - Automated Invoice & Receipt Digitization
Module: Real-World Business Models (Computer Vision & OCR)

Built a Python pipeline that processes photographs of receipts and invoices, extracts text with EasyOCR, and exports machine-readable results with confidence scores and text-location coordinates.

Key Implementations:
- Collected and verified 5 real receipt images with varying image quality
- Built OpenCV preprocessing stages: grayscale conversion, Gaussian blur, global thresholding, and adaptive thresholding
- Saved intermediate outputs and 5 final cleaned receipt images
- Integrated EasyOCR for English-language text recognition on CPU
- Extracted text regions, confidence scores, and bounding-box coordinates
- Visualized OCR bounding boxes and inspected high/low-confidence detections
- Flagged results below a 0.60 confidence threshold for potential human review
- Compared OCR output from original and preprocessed images
- Exported results to outputs/ocr_results.json
- Tested the standalone ocr_pipeline.py script successfully outside the notebook
Verified Pipeline Results:
Metric	Result
Original Receipt Images	5
Cleaned Receipt Images	5
Text Regions Detected (Raw Images)	329
Text Regions Detected (Cleaned Images)	317
Standalone Script	Passed (exit code 0)
JSON Validation	Passed


Raw vs. Cleaned Average OCR Confidence:
Receipt	Raw	Cleaned
Receipt 01	88.66%	69.30%
Receipt 02	78.67%	50.41%
Receipt 03	73.16%	59.05%
Receipt 04	62.62%	40.64%
Receipt 05	49.28%	38.61%


Key Findings & Limitations:
- Adaptive thresholding reduced average OCR confidence on all five tested receipts. Preprocessing is not guaranteed to improve recognition on every image.
- Confidence is not the same as accuracy: no ground-truth transcription accuracy was established by this comparison.
- Difficult lighting, image noise, and non-English receipt text can affect English-only OCR results.
- The needs_review flag identifies low-confidence outputs; it is not an implemented human-review interface.
Week 3 Project Structure:
week_3/
|-- raw_images/                # Original receipt photographs
|-- cleaned_images/            # Processed images
|-- outputs/
|   |-- ocr_results.json       # Text, confidence, bounding boxes
|-- notebook.ipynb             # Development and experiments
|-- ocr_pipeline.py            # Standalone OCR pipeline
Run the Standalone OCR Pipeline (from the repository root, after installing Python):
python -m pip install easyocr opencv-python numpy matplotlib
python week_3/ocr_pipeline.py
EasyOCR may download pretrained model weights the first time it runs. The script reads the images in week_3/raw_images/ and writes cleaned images and JSON output to their corresponding project folders.

View Week 3 Project
🎯 Internship Objectives
- Strengthen practical Artificial Intelligence, Machine Learning, and Computer Vision skills.
- Build reproducible, end-to-end solutions for real-world problems.
- Practice data preparation, feature engineering, model tuning, and evaluation.
- Understand model serialization, persistence, and standalone inference.
- Apply OCR and image preprocessing to business documents.
- Improve experimentation, technical documentation, and version control.
- Develop a foundation for deploying reliable AI-powered applications.
📈 Learning Progress
Week	Project	Status
Week 1	Customer Churn Prediction	Completed
Week 2	Model Serialization & Standalone Inference	Completed
Week 3	Automated Invoice & Receipt Digitization	Completed


👨‍💻 Author
Rasidul Hoque Chowdhury
AI/ML Engineering Intern - Crack404
GitHub: @therash08