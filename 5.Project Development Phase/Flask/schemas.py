from pydantic import BaseModel, EmailStr
from typing import Optional, List
from datetime import datetime

# --- USER ---
class UserBase(BaseModel):
    name: str
    email: EmailStr
    role: str

class UserCreate(UserBase):
    pass

class UserResponse(UserBase):
    user_id: int
    created_at: datetime

    class Config:
        from_attributes = True

# --- APPLICANT PROFILE ---
class ApplicantProfileBase(BaseModel):
    user_id: Optional[int] = None
    gender: str
    married: str
    education: str
    self_employed: str
    dependents: int
    property_area: str

class ApplicantProfileCreate(ApplicantProfileBase):
    pass

class ApplicantProfileResponse(ApplicantProfileBase):
    applicant_id: int

    class Config:
        from_attributes = True

# --- CREDIT HISTORY ---
class CreditHistoryBase(BaseModel):
    applicant_id: int
    credit_score: float
    credit_history_status: int

class CreditHistoryCreate(CreditHistoryBase):
    pass

class CreditHistoryResponse(CreditHistoryBase):
    credit_id: int

    class Config:
        from_attributes = True

# --- LOAN APPLICATION ---
class LoanApplicationBase(BaseModel):
    applicant_id: int
    income: float
    coapplicant_income: float
    loan_amount: float
    loan_term: int

class LoanApplicationCreate(LoanApplicationBase):
    pass

class LoanApplicationResponse(LoanApplicationBase):
    loan_id: int
    application_date: datetime

    class Config:
        from_attributes = True

# --- MODEL ---
class ModelBase(BaseModel):
    model_name: str
    model_nm: Optional[str] = None
    algorithm: str
    training_accuracy: Optional[float] = None
    testing_accuracy: Optional[float] = None
    file_path: str

class ModelCreate(ModelBase):
    pass

class ModelResponse(ModelBase):
    model_id: int

    class Config:
        from_attributes = True

# --- PREDICTION RESULT ---
class PredictionResultBase(BaseModel):
    loan_id: int
    model_id: int
    prediction_status: str
    probability_score: float

class PredictionResultCreate(PredictionResultBase):
    pass

class PredictionResultResponse(PredictionResultBase):
    prediction_id: int
    prediction_time: datetime

    class Config:
        from_attributes = True

# --- RUN PREDICTION ---
class LoanPredictionRequest(BaseModel):
    loan_id: int
    model_id: int
