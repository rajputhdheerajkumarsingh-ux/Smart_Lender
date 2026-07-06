import sys
# Clean path to prevent circular import conflicts on user's machine
sys.path = [p for p in sys.path if not (p.endswith("Python313") or p.endswith("Python313\\"))]

import os
import pickle
import pandas as pd
from sqlalchemy.orm import Session
from app import crud, models

MODEL_PATH = "app/models/xgboost_loan_model.pkl"

def get_prediction_model():
    if not os.path.exists(MODEL_PATH):
        return None
    with open(MODEL_PATH, "rb") as f:
        model = pickle.load(f)
    return model

def predict_loan_approval(db: Session, loan_id: int, model_id: int):
    # 1. Fetch Loan Application
    loan = crud.get_loan_application(db, loan_id)
    if not loan:
        raise ValueError(f"Loan application with ID {loan_id} not found")
        
    # 2. Fetch Applicant Profile
    profile = crud.get_applicant_profile(db, loan.applicant_id)
    if not profile:
        raise ValueError(f"Applicant profile with ID {loan.applicant_id} not found")
        
    # 3. Fetch Credit History
    credit = crud.get_credit_history_by_applicant(db, loan.applicant_id)
    credit_status = 1.0 if (credit and credit.credit_history_status == 1) else 0.0
    
    # 4. Load model metadata and file
    db_model = crud.get_model(db, model_id)
    if not db_model:
        raise ValueError(f"Model record with ID {model_id} not found")
        
    model_pipeline = get_prediction_model()
    if not model_pipeline:
        raise ValueError(f"Model binary file not found at {MODEL_PATH}. Please run the training script.")
        
    # 5. Build features dataframe matching the columns used in scripts/train_model.py
    data = {
        "gender": [profile.gender],
        "married": [profile.married],
        "dependents": [profile.dependents],
        "education": [profile.education],
        "self_employed": [profile.self_employed],
        "applicant_income": [loan.income],
        "coapplicant_income": [loan.coapplicant_income],
        "loan_amount": [loan.loan_amount],
        "loan_term": [loan.loan_term],
        "credit_history": [credit_status],
        "property_area": [profile.property_area]
    }
    
    df = pd.DataFrame(data)
    
    # 6. Run prediction
    prediction_prob = model_pipeline.predict_proba(df)[0][1] # Probability of approval (class 1)
    prediction_class = model_pipeline.predict(df)[0] # 1 or 0
    
    prediction_status = "Approved" if prediction_class == 1 else "Rejected"
    
    return prediction_status, float(prediction_prob)
