# Smart Lender — Project Development Phase

## Project Overview
Smart Lender is an AI-powered Loan Approval Prediction System built using Machine Learning. The model analyzes applicant financial and personal data to predict whether a loan application should be **Approved** or **Rejected**.

The model uses:
- Gender
- Marital Status
- Number of Dependents
- Education Level
- Self-Employment Status
- Applicant Income
- Co-Applicant Income
- Loan Amount
- Loan Amount Term
- Credit History
- Property Area

to predict the loan approval status and output a **probability confidence score**.

---

## Technologies Used
- Python 3.11
- Pandas
- NumPy
- Scikit-Learn
- XGBoost
- FastAPI / Uvicorn
- Flask
- SQLAlchemy
- Pydantic v2
- HTML5 / CSS3 (Glassmorphism)
- Vanilla JavaScript

---

## Machine Learning Model
**Model Used:** XGBoost Classifier

**Preprocessing:**
- Categorical features: `OneHotEncoder(drop='first')`
- Numerical features: `StandardScaler()`

**Data:** Synthetically generated dataset of 1,200 applicant records with statistically calibrated distributions.

**Performance Metrics (Approximate):**
- Training Accuracy: ~91%
- Testing Accuracy: ~88%

---

## Project Structure
```
5.Project Development Phase/
├── Dataset/
│   └── (synthetic data generated at training time)
├── Flask/
│   ├── static/
│   │   ├── index.html         # Interactive SPA Dashboard
│   │   ├── styles.css         # Glassmorphism CSS Design System
│   │   └── app.js             # Frontend API Client
│   ├── templates/
│   │   ├── home.html          # Landing page
│   │   ├── predict.html       # Loan application form
│   │   └── submit.html        # Prediction result page
│   ├── app.py                 # Standalone Flask server
│   ├── main.py                # FastAPI backend server
│   ├── models.py              # SQLAlchemy ORM models
│   ├── crud.py                # CRUD database operations
│   ├── database.py            # DB engine and session
│   ├── schemas.py             # Pydantic request/response schemas
│   ├── ml.py                  # ML inference module
│   ├── init_db.py             # Database initialization script
│   ├── schema.sql             # Raw SQL DDL schema
│   ├── loan_model.pkl         # Serialized trained XGBoost pipeline
│   ├── loans.db               # Seeded SQLite database
│   ├── Procfile               # Heroku/Render process file
│   ├── requirements.txt       # Python dependencies
│   └── runtime.txt            # Python environment version
├── Training/
│   └── train_model.py         # Synthetic data generation & model training
├── README.md                  # This file
└── render.yaml                # Render.com deployment configuration
```

---

## Setup & Installation

### Clone Repository
```bash
git clone <repository-url>
```

### Navigate to Flask Folder
```bash
cd "5.Project Development Phase/Flask"
```

### Install Dependencies
```bash
pip install -r requirements.txt
```

### Initialize Database
```bash
python init_db.py
```

### Train & Serialize the ML Model
```bash
python ../Training/train_model.py
```

### Run FastAPI Server (Full Stack Dashboard)
```bash
uvicorn main:app --reload --port 5000
```
Open: `http://127.0.0.1:5000/`
API Docs: `http://127.0.0.1:5000/docs`

### Run Flask Server (Form-Based Interface)
```bash
python app.py
```
Open: `http://127.0.0.1:5000/`

---

## Key Features
- XGBoost ML-powered loan approval prediction
- Instant approval / rejection with probability confidence score
- Glassmorphism premium dark-mode UI
- Interactive SPA dashboard with real-time statistics
- Fully relational SQLite database with SQLAlchemy ORM
- RESTful FastAPI backend with auto-generated `/docs`
- Traditional Flask form-based interface as fallback

## Developed By
- Rajputh Dheeraj Kumar Singh
- Kummari Yogendranadh  
- Vadisela Naga Sri Harshitha
- Srinivasulu Golla
- Gulam Abdul Rahman
