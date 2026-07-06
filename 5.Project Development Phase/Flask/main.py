import sys
# Clean path to prevent circular import conflicts on user's machine
sys.path = [p for p in sys.path if not (p.endswith("Python313") or p.endswith("Python313\\"))]

from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session
from typing import List
import os

from app import models, schemas, crud, ml
from app.database import engine, get_db

# Create SQLite Database tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Smart Lender API", version="1.0.0")

# Enable CORS for local testing
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- USER ENDPOINTS ---
@app.post("/api/users", response_model=schemas.UserResponse)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)

@app.get("/api/users", response_model=List[schemas.UserResponse])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users

# --- APPLICANT PROFILE ENDPOINTS ---
@app.post("/api/profiles", response_model=schemas.ApplicantProfileResponse)
def create_profile(profile: schemas.ApplicantProfileCreate, db: Session = Depends(get_db)):
    if profile.user_id:
        db_user = crud.get_user(db, user_id=profile.user_id)
        if not db_user:
            raise HTTPException(status_code=404, detail="User not found")
    return crud.create_applicant_profile(db=db, profile=profile)

@app.get("/api/profiles", response_model=List[schemas.ApplicantProfileResponse])
def read_profiles(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_applicant_profiles(db, skip=skip, limit=limit)

# --- CREDIT HISTORY ENDPOINTS ---
@app.post("/api/credit-histories", response_model=schemas.CreditHistoryResponse)
def create_credit_history(credit: schemas.CreditHistoryCreate, db: Session = Depends(get_db)):
    profile = crud.get_applicant_profile(db, credit.applicant_id)
    if not profile:
        raise HTTPException(status_code=404, detail="Applicant profile not found")
    return crud.create_credit_history(db=db, credit=credit)

# --- LOAN APPLICATION ENDPOINTS ---
@app.post("/api/loans", response_model=schemas.LoanApplicationResponse)
def create_loan(loan: schemas.LoanApplicationCreate, db: Session = Depends(get_db)):
    profile = crud.get_applicant_profile(db, loan.applicant_id)
    if not profile:
        raise HTTPException(status_code=404, detail="Applicant profile not found")
    return crud.create_loan_application(db=db, application=loan)

@app.get("/api/loans", response_model=List[schemas.LoanApplicationResponse])
def read_loans(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_loan_applications(db, skip=skip, limit=limit)

# --- MODEL ENDPOINTS ---
@app.get("/api/models", response_model=List[schemas.ModelResponse])
def read_models(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_models(db, skip=skip, limit=limit)

# --- PREDICTION ENDPOINTS ---
@app.post("/api/predictions/run", response_model=schemas.PredictionResultResponse)
def run_prediction(req: schemas.LoanPredictionRequest, db: Session = Depends(get_db)):
    try:
        status_pred, prob_pred = ml.predict_loan_approval(db, req.loan_id, req.model_id)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
        
    prediction_in = schemas.PredictionResultCreate(
        loan_id=req.loan_id,
        model_id=req.model_id,
        prediction_status=status_pred,
        probability_score=prob_pred
    )
    return crud.create_prediction_result(db=db, prediction=prediction_in)

@app.get("/api/predictions", response_model=List[schemas.PredictionResultResponse])
def read_predictions(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_prediction_results(db, skip=skip, limit=limit)

# --- STATS ENDPOINT ---
@app.get("/api/dashboard/stats")
def get_dashboard_stats(db: Session = Depends(get_db)):
    total_apps = db.query(models.LoanApplication).count()
    total_users = db.query(models.User).count()
    total_profiles = db.query(models.ApplicantProfile).count()
    
    preds = db.query(models.PredictionResult).all()
    total_preds = len(preds)
    approved_count = sum(1 for p in preds if p.prediction_status == "Approved")
    rejected_count = sum(1 for p in preds if p.prediction_status == "Rejected")
    
    approval_rate = (approved_count / total_preds * 100) if total_preds > 0 else 0
    
    credit_scores = db.query(models.CreditHistory.credit_score).all()
    avg_credit_score = (sum(c[0] for c in credit_scores) / len(credit_scores)) if credit_scores else 0
    
    return {
        "total_applications": total_apps,
        "total_users": total_users,
        "total_profiles": total_profiles,
        "total_predictions": total_preds,
        "approved_predictions": approved_count,
        "rejected_predictions": rejected_count,
        "approval_rate": round(approval_rate, 2),
        "average_credit_score": round(avg_credit_score, 1)
    }

# Serving Dashboard Frontend
@app.get("/")
def get_dashboard():
    static_file = os.path.join("app", "static", "index.html")
    if os.path.exists(static_file):
        return FileResponse(static_file)
    return {"message": "Welcome to Smart Lender API. Please create index.html in app/static/"}

# Mount Static Directory last (fallback for other files)
if not os.path.exists("app/static"):
    os.makedirs("app/static", exist_ok=True)
app.mount("/", StaticFiles(directory="app/static"), name="static")
