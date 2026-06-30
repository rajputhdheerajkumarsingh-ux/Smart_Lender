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

## Univariate Analysis

Univariate analysis is performed to examine the **distribution and characteristics of individual features** in the dataset, one variable at a time.

---

### 📈 Continuous Features — Distribution Plot (Distplot)

Distribution plots (`distplot`) are used to visualize **continuous variables** and understand their data distribution. Subplots enable multiple feature visualizations within a single figure for easier comparison.

```python
# plotting the using distplot
plt.figure(figsize=(12, 5))
plt.subplot(121)
sns.distplot(data['ApplicantIncome'], color='r')
plt.subplot(122)
sns.distplot(data['Credit_History'])
plt.show()
```

> ⚠️ **Deprecation Note:** `distplot` is deprecated in Seaborn v0.14.0+.
> Use `sns.displot()` (figure-level) or `sns.histplot()` (axes-level) as modern alternatives.

| Feature | Plot Type | Observation |
|---|---|---|
| `ApplicantIncome` | Distplot (red) | Exhibits a **left-skewed distribution** — most applicants have lower income with a long right tail |
| `Credit_History` | Distplot | **Binary feature** with values `0` and `1` only |

---

### 📊 Categorical Features — Count Plot (Countplot)

Count plots (`countplot`) are used for **categorical variables** to display the frequency of each unique category. A dummy DataFrame is created with all categorical features and plotted using a `for` loop with subplots.

```python
# categorical features countplot using subplot
cat_data = data[['Gender', 'Married', 'Dependents',
                  'Education', 'Self_Employed',
                  'Property_Area', 'Loan_Status']]

fig, axes = plt.subplots(2, 4, figsize=(20, 10))
for idx, col in enumerate(cat_data.columns):
    ax = axes[idx // 4, idx % 4]
    sns.countplot(x=col, data=cat_data, ax=ax)
    ax.set_title(col)
plt.tight_layout()
plt.show()
```

| Feature | Categories | Observation |
|---|---|---|
| `Gender` | Male / Female | **2 categories** — frequency of Male (category 0) is higher |
| `Education` | Graduate / Not Graduate | **2 categories** — Graduate (category 0) frequency is higher |
| `Married` | Yes / No | Binary — majority are married |
| `Dependents` | 0 / 1 / 2 / 3+ | Most applicants have 0 dependents |
| `Self_Employed` | Yes / No | Most applicants are not self-employed |
| `Property_Area` | Urban / Semiurban / Rural | Semiurban has the highest count |
| `Loan_Status` | Y / N | Class imbalance visible — more approvals than rejections |

---

### 🔍 Key Observations

- **ApplicantIncome** exhibits a **left-skewed distribution** — skewness needs to be addressed during preprocessing.
- **Credit History** is a **binary feature** with values `0` and `1` — critical predictor for loan approval.
- **Gender** and **Education** are **categorical variables with two categories each**.
- The **frequency of category 0 is higher** than category 1 for both `Gender` and `Education` features.
- This analysis helps identify **feature patterns and distributions** before proceeding with data preprocessing and model development.

---

## Bivariate Analysis

Bivariate analysis uses **count plots** to examine relationships between **pairs of variables**, revealing how one feature interacts with or influences another.

---

### 📊 Countplot — Visualising Two Columns Against Each Other

Three subplot pairs are plotted side by side to compare key feature combinations across the dataset.

```python
# visualising two columns against each other
plt.figure(figsize=(20, 5))

plt.subplot(131)
sns.countplot(data['Married'], hue=data['Gender'])

plt.subplot(132)
sns.countplot(data['Self_Employed'], hue=data['Education'])

plt.subplot(133)
sns.countplot(data['Property_Area'], hue=data['Loan_Amount_Term'])
```

---

### 🔍 Bivariate Insights

| Plot | X-Axis | Hue (Grouping) | Key Insight |
|---|---|---|---|
| **Subplot 1** | `Married` | `Gender` | Segmenting **gender against married status** reveals demographic patterns in loan applications — married males dominate applicants |
| **Subplot 2** | `Self_Employed` | `Education` | Segmenting **education against self-employment** shows that **educated applicants tend to be employed** — non-graduates are more likely to be self-employed |
| **Subplot 3** | `Property_Area` | `Loan_Amount_Term` | **Loan amount term distributions vary** based on the applicant's property area — Semiurban areas show a wider spread of loan terms |

---

### 📌 Summary of Observations

- **Gender × Married**: Married male applicants form the largest segment, indicating a strong demographic skew in the application pool.
- **Education × Self-Employed**: Graduate applicants are less likely to be self-employed, suggesting a correlation between formal education and salaried employment.
- **Property Area × Loan Amount Term**: The 360-month (30-year) term is the most common across all property areas, with Urban areas showing slightly more variation in term length.

---

## Multivariate Analysis

Multivariate analysis examines the **relationships between multiple features simultaneously**, revealing how combined variables interact to influence the target outcome. This project uses the **`swarmplot`** function from the Seaborn library.

---

### 🐝 Swarmplot — Gender, Income & Loan Status

The swarmplot visualises **three variables at once**:
- **X-axis**: `Gender` (categorical)
- **Y-axis**: `ApplicantIncome` (continuous)
- **Hue**: `Loan_Status` (target — Y / N)

```python
# visualized based on gender and income what would be the application status
sns.swarmplot(data['Gender'], data['ApplicantIncome'], hue=data['Loan_Status'])
```

---

### 🔍 Multivariate Insights

| Dimension | Variable | Role |
|---|---|---|
| X-Axis | `Gender` | Groups data points by applicant gender (Male / Female) |
| Y-Axis | `ApplicantIncome` | Shows the income distribution within each gender group |
| Hue (Color) | `Loan_Status` | Distinguishes approved (`Y`) vs rejected (`N`) applications |

---

### 📌 Key Observations

- **High-income applicants** (both male and female) are more likely to receive loan approval — `Loan_Status = Y` dots appear more frequently at higher income levels.
- **Male applicants** show a **wider income spread** compared to female applicants, reflecting income disparity in the dataset.
- **Female applicants** at lower income levels still receive approvals, indicating that **income alone is not the sole deciding factor** — credit history and other variables also play a role.
- The swarmplot makes it easy to identify **outliers** in income that may affect model training, especially for high-earning applicants with rejected loans.
- This three-dimensional view bridges the gap between individual feature analysis (univariate) and the full multivariate model, providing a clearer picture of the **combined influence of gender and income on loan decisions**.

---

## Data Pre-Processing

Before training machine learning models, the raw dataset undergoes a series of cleaning and transformation steps to ensure data quality and model compatibility.

---

### 🔡 Step 1 — Handling Categorical Values

Categorical features are converted into numerical values using **label encoding (mapping)** so machine learning algorithms can process them correctly.

```python
import jupyterthemes as jt
!jt -t onedork

# Encode categorical features to numeric
data['Gender']        = data['Gender'].map({'Female': 1, 'Male': 0})
data['Property_Area'] = data['Property_Area'].map({'Urban': 2, 'Semiurban': 1, 'Rural': 0})
data['Married']       = data['Married'].map({'Yes': 1, 'No': 0})
data['Education']     = data['Education'].map({'Graduate': 1, 'Not Graduate': 0})
data['Loan_Status']   = data['Loan_Status'].map({'Y': 1, 'N': 0})
```

**Encoding Mapping Reference:**

| Feature | Encoding |
|---|---|
| `Gender` | Female → `1`, Male → `0` |
| `Property_Area` | Urban → `2`, Semiurban → `1`, Rural → `0` |
| `Married` | Yes → `1`, No → `0` |
| `Education` | Graduate → `1`, Not Graduate → `0` |
| `Loan_Status` | Y (Approved) → `1`, N (Rejected) → `0` |

---

### 🩹 Step 2 — Handling Missing Values

The dataset is inspected for null values and missing entries are filled using appropriate strategies.

```python
# finding the sum of null values in each column
data.isnull().sum()

# Fill categorical columns with mode (most frequent value)
data['Gender']        = data['Gender'].fillna(data['Gender'].mode()[0])
data['Married']       = data['Married'].fillna(data['Married'].mode()[0])

# replacing '+' with space for filling the NaN values in Dependents
data['Dependents']    = data['Dependents'].str.replace('+', '')
data['Dependents']    = data['Dependents'].fillna(data['Dependents'].mode()[0])

data['Self_Employed'] = data['Self_Employed'].fillna(data['Self_Employed'].mode()[0])
data['LoanAmount']    = data['LoanAmount'].fillna(data['LoanAmount'].mode()[0])
```

**Missing Value Strategy:**

| Column | Strategy | Reason |
|---|---|---|
| `Gender` | Mode fill | Categorical — most frequent value preserves distribution |
| `Married` | Mode fill | Categorical — binary feature |
| `Dependents` | Mode fill + strip `+` | String `3+` cleaned before imputation |
| `Self_Employed` | Mode fill | Categorical — binary feature |
| `LoanAmount` | Mode fill | Numerical — mode used to avoid mean skew from outliers |

---

### 🔢 Step 3 — Data Inspection & Type Conversion

After encoding and imputation, the dataset is verified and all float columns are cast to `int64` for consistency.

```python
# getting the total info of the data after performing categorical to numerical and replacing missing values
data.info()
data.isnull().sum()

# changing the dtype of each float column to int
data['Gender']             = data['Gender'].astype('int64')
data['Married']            = data['Married'].astype('int64')
data['Dependents']         = data['Dependents'].astype('int64')
data['Self_Employed']      = data['Self_Employed'].astype('int64')
data['CoapplicantIncome']  = data['CoapplicantIncome'].astype('int64')
data['LoanAmount']         = data['LoanAmount'].astype('int64')
data['Loan_Amount_Term']   = data['Loan_Amount_Term'].astype('int64')
data['Credit_History']     = data['Credit_History'].astype('int64')

data.info()
```

**Result:** All columns are now clean integer or numeric types — ready for model training with no missing values.

---

## Data Balancing — SMOTE

Data balancing is a critical step for classification models. Training on an **imbalanced dataset** leads to biased predictions, where the model predominantly predicts the **majority class** and ignores the minority class.

---

### ⚖️ Why Balancing is Needed

In the loan prediction dataset, loan approvals (`Loan_Status = 1`) significantly outnumber rejections (`Loan_Status = 0`), creating a class imbalance that biases the model towards always predicting approval.

```
Before Balancing:
  Loan_Status = 1 (Approved)  →  ~422 samples  (majority)
  Loan_Status = 0 (Rejected)  →  ~190 samples  (minority)
```

---

### 🧬 SMOTE — Synthetic Minority Over-sampling Technique

This project applies **SMOTE** from the `imblearn` library to address class imbalance. SMOTE generates **synthetic data points** for the minority class using the **K-Nearest Neighbors (KNN)** method — it does not simply duplicate existing samples but creates new, realistic in-between points.

```python
from imblearn.over_sampling import SMOTE

# Separate features and target
x = data.drop('Loan_Status', axis=1)
y = data['Loan_Status']

# Apply SMOTE to generate synthetic minority class samples
smote = SMOTE()

# creating a new x and y variables for the balanced set
x_bal, y_bal = smote.fit_resample(x, y)

# printing the values of y before balancing the data and after
print(y.value_counts())
print(y_bal.value_counts())

names = x_bal.columns
```

---

### 📊 Before vs After Balancing

| Class | Label | Before SMOTE | After SMOTE |
|---|---|---|---|
| Approved | `1` | ~422 samples | ~422 samples |
| Rejected | `0` | ~190 samples | ~422 samples ✅ |
| **Total** | | **~612** | **~844** |

> After applying SMOTE, the **minority class size is increased to match the majority class**, resulting in a **balanced dataset** that enables unbiased model training.

---

### 🔑 How SMOTE Works

```
1. For each minority class sample:
   └── Find its K nearest neighbours (also minority class)
   └── Randomly select one neighbour
   └── Generate a synthetic point along the line between them
2. Repeat until minority class matches majority class size
```

---

## Feature Scaling

Feature scaling is an important preprocessing step because features measured on different scales (e.g., income in thousands vs. dependents in single digits) can mislead the model's predictions.

---

### 📏 Why Feature Scaling is Important

- **Distance-Based Models**: Algorithms like **K-Nearest Neighbors (KNN)** and **Support Vector Machines (SVM)** rely on distance calculations between data points. Features with larger numeric ranges would dominate the distance calculation if not scaled.
- **Optimization Algorithms**: Models using gradient descent optimization (like Logistic Regression or Neural Networks) converge much faster when features are scaled to a similar range.
- **Target Exclusion**: Scaling is applied **only to the input features (X)**, not to the target/output variable (y).

---

### 💻 Code Implementation

The project uses `StandardScaler` from Scikit-Learn, which standardizes features by removing the mean and scaling to unit variance ($z = (x - \mu) / \sigma$). After fitting and transforming, the resulting NumPy array is converted back into a Pandas DataFrame.

```python
# performing feature Scaling operation using standard scaler on X part of the dataset because
# there different type of values in the columns
sc = StandardScaler()
x_bal = sc.fit_transform(x_bal)

# Converting the scaled array back to a DataFrame with original column names
x_bal = pd.DataFrame(x_bal, columns=names)
```

---

## Train-Test Split

To evaluate the predictive performance of the machine learning models, the dataset is split into a **training set** (used to train the model) and a **testing set** (used to evaluate performance on unseen data).

---

### ✂️ Split Strategy & Parameters

The `train_test_split()` function from `scikit-learn` is used to split the balanced, scaled features (`x_bal`) and the balanced target variable (`y_bal`) using the following parameters:

- **Features (X)**: Input features containing demographic, financial, and credit history variables.
- **Target (y)**: Binary loan approval status (`0` or `1`).
- **`test_size=0.33`**: Allocates **33%** of the dataset for testing (~279 samples) and **67%** for training (~565 samples).
- **`random_state=42`**: Sets a seed value to ensure the random split is identical every time the notebook is run, ensuring reproducibility of the model results.

```python
# splitting the dataset in train and test on balanced dataset
X_train, X_test, y_train, y_test = train_test_split(
    x_bal, y_bal, test_size=0.33, random_state=42
)

# Inspect dataset shapes
X_train.shape
X_test.shape
```

---

### 📊 Dataset Partitions

| Partition | Description | Percentage | Sample Count | Shape |
|---|---|---|---|---|
| **Training Set (`X_train`, `y_train`)** | Used to fit model parameters | 67% | ~565 | `(565, 12)` |
| **Testing Set (`X_test`, `y_test`)** | Used to test model generalization | 33% | ~279 | `(279, 12)` |

---

## Model Building

To predict loan eligibility, several machine learning classifiers are trained, evaluated, and compared. 

---

### 🌳 1. Decision Tree Classifier

A Decision Tree model is built to establish a baseline classification performance. A function named `decisionTree()` is defined to streamline initialization, training, and evaluation.

- **Model Setup**: Initializes `DecisionTreeClassifier` with default hyperparameters.
- **Training**: Fits the model on the balanced training data (`X_train`, `y_train`).
- **Prediction**: Predicts labels for both the training and testing datasets to inspect overfitting/generalization.
- **Evaluation**: The accuracy score is printed, and model performance is further evaluated using a confusion matrix and a classification report.

```python
# importing and building the Decision tree model
def decisionTree(X_train, X_test, y_train, y_test):
    model = DecisionTreeClassifier()
    model.fit(X_train, y_train)
    
    # Predict and evaluate on training set
    y_tr = model.predict(X_train)
    print("Training Accuracy:", accuracy_score(y_tr, y_train))
    
    # Predict and evaluate on testing set
    yPred = model.predict(X_test)
    print("Testing Accuracy:", accuracy_score(yPred, y_test))

# printing the train accuracy and test accuracy respectively
decisionTree(X_train, X_test, y_train, y_test)
```

### 🌲 2. Random Forest Classifier

An ensemble-based Random Forest model is built to improve predictive performance. A function named `RandomForest()` is defined with the same structure as `decisionTree()`.

- **Model Setup**: Initializes `RandomForestClassifier` (an ensemble of decision trees) to reduce overfitting and variance.
- **Training**: Trains on the training dataset (`X_train`, `y_train`).
- **Evaluation**: Computes training and testing accuracies, and evaluates predictions via the confusion matrix and classification report.

```python
# importing and building the random forest model
def RandomForest(X_tarin, X_test, y_train, y_test):
    model = RandomForestClassifier()
    model.fit(X_train, y_train)
    
    # Predict and evaluate on training set
    y_tr = model.predict(X_train)
    print("Training Accuracy:", accuracy_score(y_tr, y_train))
    
    # Predict and evaluate on testing set
    yPred = model.predict(X_test)
    print("Testing Accuracy:", accuracy_score(yPred, y_test))

# printing the train accuracy and test accuracy respectively
RandomForest(X_train, X_test, y_train, y_test)
```

> 📝 **Note**: The parameter signature in the notebook screenshot includes a minor typo `X_tarin` but references the correct `X_train` variable within the scope.

### 👥 3. K-Nearest Neighbors (KNN) Classifier

A distance-based K-Nearest Neighbors classifier is built. A function named `KNN()` is defined using the same standard structure.

- **Model Setup**: Initializes `KNeighborsClassifier` with default parameters. Note that since KNN relies on Euclidean distance calculations, this model relies heavily on the **Feature Scaling** preprocessing step completed earlier.
- **Training**: Fits the model on the standardized training data (`X_train`, `y_train`).
- **Evaluation**: Computes accuracy scores and evaluates classification metrics using confusion matrices and classification reports.

```python
# importing and building the KNN model
def KNN(X_train, X_test, y_train, y_test):
    model = KNeighborsClassifier()
    model.fit(X_train, y_train)
    
    # Predict and evaluate on training set
    y_tr = model.predict(X_train)
    print("Training Accuracy:", accuracy_score(y_tr, y_train))
    
    # Predict and evaluate on testing set
    yPred = model.predict(X_test)
    print("Testing Accuracy:", accuracy_score(yPred, y_test))

# printing the train accuracy and test accuracy respectively
KNN(X_train, X_test, y_train, y_test)
```

### ⚡ 4. Gradient Boosting (XGB) Classifier

A Gradient Boosting classifier (referred to as XGB in the notebook) is built. A function named `XGB()` is created to train and test the model.

- **Model Setup**: Initializes `GradientBoostingClassifier` from Scikit-Learn. This ensemble method builds trees sequentially, where each tree attempts to correct the errors of the previous tree.
- **Training**: Fits the model on the balanced training data (`X_train`, `y_train`).
- **Evaluation**: Computes accuracy scores and evaluates classifications using confusion matrices and classification reports.

```python
# importing and building the Xg boost model
def XGB(X_train, X_test, y_train, y_test):
    model = GradientBoostingClassifier()
    model.fit(X_train, y_train)
    
    # Predict and evaluate on training set
    y_tr = model.predict(X_train)
    print("Training Accuracy:", accuracy_score(y_tr, y_train))
    
    # Predict and evaluate on testing set
    yPred = model.predict(X_test)
    print("Testing Accuracy:", accuracy_score(yPred, y_test))

# printing the train accuracy and test accuracy respectively
XGB(X_train, X_test, y_train, y_test)
```

> 📝 **Note**: Although the function and comments reference "Xg boost", the implementation initializes Scikit-Learn's `GradientBoostingClassifier`.

### 🔍 5. Model Validation & Saving

To ensure that the models generalize well to unseen data, **Cross-Validation** is performed, and the best-performing model is serialized for integration with the web application.

---

#### 🔄 5-Fold Cross-Validation

Cross-validation is applied using `cross_val_score` from `scikit-learn` with **5-fold cross-validation (`cv=5`)**. This split strategy divides the data into 5 subsets, training on 4 and testing on the remaining 1 iteratively, which helps:
- Verify consistent model performance across different data splits.
- Minimize potential bias introduced by a single train-test split.
- Ensure the model's robustness and protect against overfitting.

> For an in-depth explanation of how cross-validation evaluates estimators, refer to the [Towards Data Science Cross-Validation Guide](https://towardsdatascience.com/cross-validation-explained-evaluating-estimator-performance-e51e5430ff85).

---

#### 💾 Saving the Best Model

Once the model with the highest generalization score is selected, it is saved using Python's built-in `pickle` module. This process serializes the model object into a binary format file (`rdf.pkl`), allowing it to be instantly reloaded by the web server without needing retraining.

```python
# saving the model by using pickle function
pickle.dump(model, open('rdf.pkl', 'wb'))
```

- **File Output**: `rdf.pkl` (placed in the Flask application directory).
- **Flask Integration**: The backend application loads this model at startup via `pickle.load(open('rdf.pkl', 'rb'))` to process real-time loan prediction requests submitted from the web dashboard interface.

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
