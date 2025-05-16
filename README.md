# 🔥 ML-Based Firewall Classifier

A machine learning-powered web application that detects malicious HTTP requests such as SQL Injection (SQLi), Cross-Site Scripting (XSS), Command Injection (CMDi), CSRF, and CDMI.  
Trained on simulated attack data and allows comparison across multiple ML models: **Random Forest**, **K-Nearest Neighbors**, and **SVM**.

---

## 🚀 Features

- 🧠 ML Models: Random Forest, KNN, and SVM
- 🌐 Flask web app with modern UI
- 📊 Model prediction comparison chart
- 🕓 Request classification history
- 📁 Pretrained models + dataset
- 🔒 Detects: `sqli`, `xss`, `cmdi`, `csrf`, `cdmi`, `normal`

---

## 📁 Project Structure

Firewall_classifier/
├── app.py # Flask web app
├── train_models.py # Training script for all models
├── requests_dataset.csv # Sample dataset
├── rf_model.joblib # Trained Random Forest
├── knn_model.joblib # Trained KNN
├── svm_model.joblib # Trained SVM
├── vectorizer.joblib # TF-IDF vectorizer
├── templates/
│ └── index.html # Frontend with dark UI and charts
└── README.md

yaml
Copy
Edit

---

## 🛠 Setup Instructions

### 1. Clone the repo

```bash
git clone https://github.com/Yatin-khajuria/Firewall_classifier.git
cd Firewall_classifier
2. Create virtual environment
bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
3. Install dependencies
bash
Copy
Edit
pip install -r requirements.txt
If requirements.txt is missing, manually install:

bash
Copy
Edit
pip install flask scikit-learn pandas joblib
4. Train models (if .joblib files are missing)
bash
Copy
Edit
python train_models.py
5. Run the app
bash
Copy
Edit
python app.py
Then visit: http://127.0.0.1:5000

🧪 Example Inputs
GET /product?id=1 OR 1=1 → 🟥 SQL Injection

<script>alert('xss')</script> → 🟥 XSS

POST /login HTTP/1.1 → ✅ Normal

📊 Model Comparison Chart
The dashboard shows:

All model predictions (side by side)

Chart visualization with color-coded classes

History of recent HTTP request classifications
