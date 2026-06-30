# Smart Lender - Loan Approval Prediction System

A full-stack machine learning application built with **FastAPI**, **SQLite + SQLAlchemy**, **XGBoost Classifier**, and a premium **Glassmorphism Web Dashboard** to automate credit risk assessment and predict loan eligibility.

## Features
- **Database Schema**: Follows the ER diagram normalized structure (Users, Applicant Profiles, Credit Histories, Loan Requests, Model Engines, and Prediction Logs).
- **Machine Learning**: Features an XGBoost Classifier trained on a simulated dataset representing real-world credit guidelines, including CIBIL credit scores, income, loan amount, and applicant profiles.
- **Glassmorphism UI**: High-end dark theme dashboard with responsive form wizards, evaluation animations, interactive tables, and analytical charts.
- **REST API Endpoints**: Full CRUD endpoints for applicant profile management, loan applications, and predictions.

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
