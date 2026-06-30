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
