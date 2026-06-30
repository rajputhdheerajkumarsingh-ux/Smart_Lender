# Smart Lender - Loan Approval Prediction System

A full-stack machine learning application built with **FastAPI**, **SQLite + SQLAlchemy**, **XGBoost Classifier**, and a premium **Glassmorphism Web Dashboard** to automate credit risk assessment and predict loan eligibility.

## Features
- **Database Schema**: Follows the ER diagram normalized structure (Users, Applicant Profiles, Credit Histories, Loan Requests, Model Engines, and Prediction Logs).
- **Machine Learning**: Features an XGBoost Classifier trained on a simulated dataset representing real-world credit guidelines, including CIBIL credit scores, income, loan amount, and applicant profiles.
- **Glassmorphism UI**: High-end dark theme dashboard with responsive form wizards, evaluation animations, interactive tables, and analytical charts.
- **REST API Endpoints**: Full CRUD endpoints for applicant profile management, loan applications, and predictions.

## Technologies Used

The project was developed using a set of powerful Python-based tools and libraries for data processing, machine learning, visualization, and deployment.

| Tool / Library | Purpose | Docs |
|---|---|---|
| **Anaconda Navigator** | Desktop GUI to manage Python packages and environments for data science | [anaconda.com](https://www.anaconda.com/download) |
| **PyCharm** | Python IDE with code analysis, debugging, and refactoring tools | [jetbrains.com](https://www.jetbrains.com/pycharm/) |
| **NumPy** | Core library for numerical computing with multi-dimensional array support | [numpy.org](https://numpy.org/doc/stable/) |
| **Pandas** | Data manipulation and analysis with powerful DataFrame structures | [pandas.pydata.org](https://pandas.pydata.org/docs/) |
| **Scikit-learn** | Machine learning library with classification, regression, and clustering algorithms | [scikit-learn.org](https://scikit-learn.org/stable/) |
| **Matplotlib** | Comprehensive library for static, animated, and interactive visualizations | [matplotlib.org](https://matplotlib.org/stable/) |
| **Seaborn** | High-level statistical data visualization built on top of Matplotlib | [seaborn.pydata.org](https://seaborn.pydata.org/) |
| **Flask** | Lightweight WSGI web framework for building APIs and deploying ML models | [flask.palletsprojects.com](https://flask.palletsprojects.com/) |

## Dataset

There are many popular open-source repositories for collecting data, with **Kaggle** and the **UCI Machine Learning Repository** being among the most widely used platforms in the data science community.

For this project, the **Loan Prediction Dataset** is sourced from **Google Sheets** and contains applicant information such as gender, marital status, education, income, loan amount, credit history, and loan approval status.

### 📥 Download the Dataset

| Source | Link |
|---|---|
| **Google Drive (Project Dataset)** | [Click here to download](https://drive.google.com/drive/folders/1fOen6--02V7Ka6E24R8lPAAZ8V0vnENI?usp=sharing) |
| **Kaggle** | [kaggle.com/datasets](https://www.kaggle.com/datasets) |
| **UCI Machine Learning Repository** | [archive.ics.uci.edu](https://archive.ics.uci.edu/ml/index.php) |

> **Instructions:** Download the dataset CSV file from the Google Drive link above and place it inside the `data/` directory of the project before running any scripts.

### 📋 Dataset Features

| Feature | Description |
|---|---|
| `Loan_ID` | Unique identifier for each loan application |
| `Gender` | Applicant's gender (Male / Female) |
| `Married` | Marital status of the applicant |
| `Dependents` | Number of dependents |
| `Education` | Applicant's education level (Graduate / Not Graduate) |
| `Self_Employed` | Whether the applicant is self-employed |
| `ApplicantIncome` | Monthly income of the applicant |
| `CoapplicantIncome` | Monthly income of the co-applicant |
| `LoanAmount` | Requested loan amount (in thousands) |
| `Loan_Amount_Term` | Loan repayment term (in months) |
| `Credit_History` | Credit history meets guidelines (1 = Yes, 0 = No) |
| `Property_Area` | Location of property (Urban / Semiurban / Rural) |
| `Loan_Status` | Target variable — loan approved (Y / N) |

---

## Project Workflow

The project is developed through a structured workflow consisting of multiple epics, covering data collection, analysis, preprocessing, model development, and deployment. Each epic focuses on a specific stage of the machine learning lifecycle to ensure systematic and efficient project execution.

---

### 🗂️ Epic 1: Data Collection and Architecture Design

> Establishing the foundation — sourcing data and defining the system blueprint.

| Story | Description |
|---|---|
| **Story 1** | Download the required dataset from the provided source and store it in the project directory. |
| **Story 2** | Define the application architecture, including data flow, machine learning workflow, and deployment structure. |

---

### 📊 Epic 2: Visualizing and Analyzing the Data

> Exploring the dataset to understand distributions, relationships, and hidden patterns.

| Story | Description |
|---|---|
| **Story 1** | Import and read the dataset using Pandas for further analysis. |
| **Story 2** | Perform univariate analysis to understand the distribution of individual features. |
| **Story 3** | Conduct bivariate analysis to identify relationships between two variables. |
| **Story 4** | Perform multivariate analysis to uncover patterns involving multiple features. |

---

### ⚙️ Epic 3: Data Pre-Processing

> Cleaning, balancing, and transforming raw data into a model-ready format.

| Story | Description |
|---|---|
| **Story 1** | Check for missing values, duplicates, and inconsistencies, and handle them appropriately. |
| **Story 2** | Balance the dataset to ensure fair representation of all target classes. |
| **Story 3** | Scale and normalize numerical features to improve model performance. |
| **Story 4** | Split the dataset into training and testing sets for model development and evaluation. |

---

### 🤖 Epic 4: Model Building

> Training, tuning, and comparing multiple machine learning models to find the best performer.

| Story | Description |
|---|---|
| **Story 1** | Train and evaluate a **Decision Tree** model on the prepared dataset. |
| **Story 2** | Build and test a **Random Forest** model to improve predictive performance. |
| **Story 3** | Implement a **K-Nearest Neighbors (KNN)** model and analyze its accuracy. |
| **Story 4** | Train an **XGBoost** model and compare its performance with other models. |
| **Story 5** | Evaluate all models using appropriate metrics and save the best-performing model for deployment. |

---

### 🚀 Epic 5: Application Building

> Packaging the trained model into a live, user-facing web application.

| Story | Description |
|---|---|
| **Story 1** | Design and develop HTML pages to create a user-friendly interface. |
| **Story 2** | Build the Flask application and integrate the trained machine learning model. |
| **Story 3** | Run, test, and validate the application to ensure accurate predictions and smooth functionality. |

---

## Application Architecture

After data collection, a modular and scalable application architecture was designed to ensure **separation of concerns**, **maintainability**, and **future extensibility**. The system follows a **three-tier architecture**, consisting of the user interface, backend API layer, and AI/ML service modules.

A well-structured directory hierarchy was adopted to separate frontend, backend, model, and testing components, improving code organization, development efficiency, and scalability.

---

### 🏛️ Three-Tier Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                     TIER 1 — USER INTERFACE                 │
│           HTML · CSS · JavaScript (Glassmorphism UI)        │
│         static/index.html · static/styles.css · app.js      │
└────────────────────────────┬────────────────────────────────┘
                             │  HTTP Requests / REST API
┌────────────────────────────▼────────────────────────────────┐
│                  TIER 2 — BACKEND API LAYER                 │
│              FastAPI / Flask · SQLAlchemy · SQLite          │
│          main.py · crud.py · models.py · schemas.py         │
└────────────────────────────┬────────────────────────────────┘
                             │  Model Inference Calls
┌────────────────────────────▼────────────────────────────────┐
│                 TIER 3 — AI / ML SERVICE MODULE             │
│     XGBoost · Scikit-learn · Pandas · NumPy · Pickle       │
│        ml.py · xgboost_loan_model.pkl · train_model.py     │
└─────────────────────────────────────────────────────────────┘
```

---

### 🔄 Data Flow Diagram

```
User fills Loan Form
        │
        ▼
Frontend (HTML/JS) ──► POST /predict ──► FastAPI Backend
                                                │
                                                ▼
                                     Load Applicant Data
                                                │
                                                ▼
                                    ML Pipeline (ml.py)
                                    ┌───────────────────┐
                                    │ Feature Encoding  │
                                    │ Scaling / Scaler  │
                                    │ XGBoost Inference │
                                    └────────┬──────────┘
                                             │
                                             ▼
                              Prediction Result (Approved / Rejected)
                                             │
                                             ▼
                                  Save to SQLite DB (Prediction Log)
                                             │
                                             ▼
                              JSON Response ──► Frontend Dashboard
```

---

### 📁 Project Directory Structure

```
SmartLender/
│
├── 📂 Dataset/                        # Raw data files
│   ├── loan_prediction.csv            # Primary training dataset (CSV)
│   ├── loan_prediction.xlsx           # Excel version of the dataset
│   └── loan_prediction(1).csv        # Alternate / cleaned dataset copy
│
├── 📂 Flask/                          # Flask web application
│   ├── 📂 static/                     # Static assets (CSS, JS, images)
│   ├── 📂 templates/                  # HTML Jinja2 templates
│   ├── app1.py                        # Main Flask application entry point
│   ├── app1(1).py                     # Alternate / updated Flask app version
│   ├── rdf.pkl                        # Serialized Random Forest model
│   ├── scale1.pkl                     # Fitted feature scaler (StandardScaler)
│   └── scale1(1).pkl                  # Alternate scaler version
│
├── 📂 IBM/                            # IBM Cloud deployment configurations
│
├── 📂 Training/                       # Model training notebooks
│   └── Loan Prediction using ML.ipynb # Jupyter Notebook — full ML pipeline
│
├── 📂 app/                            # FastAPI backend (production server)
│   ├── main.py                        # API routing & server initialization
│   ├── database.py                    # SQLAlchemy & SQLite configuration
│   ├── models.py                      # ORM database models
│   ├── schemas.py                     # Pydantic request/response schemas
│   ├── crud.py                        # Database CRUD operations
│   ├── ml.py                          # ML model loader & inference engine
│   ├── 📂 models/
│   │   └── xgboost_loan_model.pkl     # Trained XGBoost pipeline (pickle)
│   └── 📂 static/                     # Glassmorphism web dashboard
│       ├── index.html
│       ├── styles.css
│       └── app.js
│
├── 📂 scripts/
│   └── train_model.py                 # Model training & DB registration script
│
├── requirements.txt                   # Python dependencies
└── README.md                          # Project documentation
```

---

## Notebook — Library Imports & Data Loading

All model training and exploratory data analysis is performed in the Jupyter Notebook:
📓 `Training/Loan Prediction using ML.ipynb`

---

### 📦 Step 1 — Importing the Libraries

The following libraries are imported at the start of the notebook. The visualization style **`fivethirtyeight`** is used for consistent and readable plots throughout the analysis.

```python
import pandas as pd
import numpy as np
import pickle
import matplotlib.pyplot as plt
%matplotlib inline
import seaborn as sns
import sklearn
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import GradientBoostingClassifier, RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import RandomizedSearchCV
import imblearn
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix, f1_score
```

| Library | Role |
|---|---|
| `pandas` | Load, explore, and manipulate the dataset |
| `numpy` | Numerical operations and array handling |
| `pickle` | Serialize and save trained model objects |
| `matplotlib.pyplot` | Core plotting library (inline rendering via `%matplotlib inline`) |
| `seaborn` | Statistical visualization with the `fivethirtyeight` style |
| `sklearn` | ML algorithms, preprocessing, model selection, and evaluation metrics |
| `DecisionTreeClassifier` | Decision Tree model training |
| `GradientBoostingClassifier` | Gradient Boosting ensemble model |
| `RandomForestClassifier` | Random Forest ensemble model |
| `KNeighborsClassifier` | K-Nearest Neighbors classifier |
| `RandomizedSearchCV` | Hyperparameter tuning via random search |
| `imblearn` | Handling class imbalance (oversampling / undersampling) |
| `train_test_split` | Splitting data into training and testing sets |
| `StandardScaler` | Feature scaling and normalization |
| `accuracy_score`, `f1_score`, etc. | Model evaluation metrics |

---

### 📂 Step 2 — Importing and Reading the Dataset

The dataset is loaded from the CSV file using Pandas for further analysis.

```python
# importing the dataset which is in csv file
data = pd.read_csv('/content/loan_prediction.csv')
data
```

**Dataset Preview (first 5 rows of 612 total):**

| | Loan_ID | Gender | Married | Dependents | Education | Self_Employed | ApplicantIncome | CoapplicantIncome | LoanAmount | Loan_Amount_Term | Credit_History | Property_Area | Loan_Status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | LP001002 | Male | No | 0 | Graduate | No | 5849 | 0.0 | NaN | 360.0 | ... | ... | ... |
| 1 | LP001003 | Male | Yes | 1 | Graduate | No | 4583 | 1508.0 | 128.0 | 360.0 | ... | ... | ... |
| 2 | LP001005 | Male | Yes | 0 | Graduate | Yes | 3000 | 0.0 | 66.0 | 360.0 | ... | ... | ... |
| 3 | LP001006 | Male | Yes | 0 | Not Graduate | No | 2583 | 2358.0 | 120.0 | 360.0 | ... | ... | ... |
| 4 | LP001008 | Male | No | 0 | Graduate | No | 6000 | 0.0 | 141.0 | 360.0 | ... | ... | ... |

> **Shape:** 612 rows × 13 columns — Each row represents one loan application with demographic, financial, and credit features.

---

## Setup & Running


1. **Setup Python Virtual Environment**
   ```bash
   python -m venv .venv
   .venv\Scripts\activate
   ```

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Train the XGBoost Model**
   ```bash
   python scripts/train_model.py
   ```
   *This trains the model, saves the pipeline pickle (`app/models/xgboost_loan_model.pkl`), and registers the model inside the SQLite database.*

4. **Start the API Server**
   ```bash
   uvicorn app.main:app --reload
   ```

5. **Access the Dashboard**
   Open your browser and navigate to `http://localhost:8000`.
