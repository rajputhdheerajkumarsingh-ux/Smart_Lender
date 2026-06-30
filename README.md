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

## Project Structure
- `app/`
  - `main.py`: FastAPI server configuration, routing, and database initialization.
  - `database.py`: SQLAlchemy session and SQLite connection configurations.
  - `models.py`: Database models mapping the ER diagram.
  - `schemas.py`: Pydantic request/response models.
  - `crud.py`: Database queries and creation transactions.
  - `ml.py`: Loads the model binary and evaluates applications.
  - `static/`: Premium Glassmorphism web dashboard.
- `scripts/`
  - `train_model.py`: Generates synthetic data, trains the XGBoost Classifier, and registers it in the SQLite DB.
- `requirements.txt`: Python package specifications.

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
