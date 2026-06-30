from sqlalchemy.orm import Session
from app import models, schemas

# --- USER CRUD ---
def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.user_id == user_id).first()

def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()

def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(name=user.name, email=user.email, role=user.role)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# --- APPLICANT PROFILE CRUD ---
def get_applicant_profile(db: Session, applicant_id: int):
    return db.query(models.ApplicantProfile).filter(models.ApplicantProfile.applicant_id == applicant_id).first()

def get_applicant_profiles(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.ApplicantProfile).offset(skip).limit(limit).all()

def create_applicant_profile(db: Session, profile: schemas.ApplicantProfileCreate):
    db_profile = models.ApplicantProfile(**profile.dict())
    db.add(db_profile)
    db.commit()
    db.refresh(db_profile)
    return db_profile

# --- CREDIT HISTORY CRUD ---
def get_credit_history_by_applicant(db: Session, applicant_id: int):
    return db.query(models.CreditHistory).filter(models.CreditHistory.applicant_id == applicant_id).first()

def create_credit_history(db: Session, credit: schemas.CreditHistoryCreate):
    db_credit = models.CreditHistory(**credit.dict())
    db.add(db_credit)
    db.commit()
    db.refresh(db_credit)
    return db_credit

# --- LOAN APPLICATION CRUD ---
def get_loan_application(db: Session, loan_id: int):
    return db.query(models.LoanApplication).filter(models.LoanApplication.loan_id == loan_id).first()

def get_loan_applications(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.LoanApplication).offset(skip).limit(limit).all()

def create_loan_application(db: Session, application: schemas.LoanApplicationCreate):
    db_app = models.LoanApplication(**application.dict())
    db.add(db_app)
    db.commit()
    db.refresh(db_app)
    return db_app

# --- MODEL CRUD ---
def get_model(db: Session, model_id: int):
    return db.query(models.Model).filter(models.Model.model_id == model_id).first()

def get_models(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Model).offset(skip).limit(limit).all()

def create_model(db: Session, model: schemas.ModelCreate):
    db_model = models.Model(**model.dict())
    db.add(db_model)
    db.commit()
    db.refresh(db_model)
    return db_model

# --- PREDICTION RESULT CRUD ---
def get_prediction_result(db: Session, prediction_id: int):
    return db.query(models.PredictionResult).filter(models.PredictionResult.prediction_id == prediction_id).first()

def get_prediction_results(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.PredictionResult).offset(skip).limit(limit).all()

def create_prediction_result(db: Session, prediction: schemas.PredictionResultCreate):
    db_pred = models.PredictionResult(**prediction.dict())
    db.add(db_pred)
    db.commit()
    db.refresh(db_pred)
    return db_pred
