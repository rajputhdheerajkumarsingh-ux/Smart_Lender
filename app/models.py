from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
import datetime
from app.database import Base

class User(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    role = Column(String, nullable=False)  # "Credit Officer" or "Applicant"
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

    # Relationships
    profiles = relationship("ApplicantProfile", back_populates="user")

class ApplicantProfile(Base):
    __tablename__ = "applicant_profiles"

    applicant_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.user_id"), nullable=True)
    gender = Column(String, nullable=False)  # Male, Female
    married = Column(String, nullable=False)  # Yes, No
    education = Column(String, nullable=False)  # Graduate, Not Graduate
    self_employed = Column(String, nullable=False)  # Yes, No
    dependents = Column(Integer, default=0)
    property_area = Column(String, nullable=False)  # Urban, Semiurban, Rural

    # Relationships
    user = relationship("User", back_populates="profiles")
    credit_histories = relationship("CreditHistory", back_populates="applicant")
    loan_applications = relationship("LoanApplication", back_populates="applicant")

class CreditHistory(Base):
    __tablename__ = "credit_histories"

    credit_id = Column(Integer, primary_key=True, index=True)
    applicant_id = Column(Integer, ForeignKey("applicant_profiles.applicant_id"), nullable=False)
    credit_score = Column(Float, nullable=False)
    credit_history_status = Column(Integer, nullable=False)  # 1 (good), 0 (bad)

    # Relationships
    applicant = relationship("ApplicantProfile", back_populates="credit_histories")

class LoanApplication(Base):
    __tablename__ = "loan_applications"

    loan_id = Column(Integer, primary_key=True, index=True)
    applicant_id = Column(Integer, ForeignKey("applicant_profiles.applicant_id"), nullable=False)
    income = Column(Float, nullable=False)
    coapplicant_income = Column(Float, nullable=False)
    loan_amount = Column(Float, nullable=False)  # in thousands
    loan_term = Column(Integer, nullable=False)  # in days/months
    application_date = Column(DateTime, default=datetime.datetime.utcnow)

    # Relationships
    applicant = relationship("ApplicantProfile", back_populates="loan_applications")
    prediction_results = relationship("PredictionResult", back_populates="loan")

class Model(Base):
    __tablename__ = "models"

    model_id = Column(Integer, primary_key=True, index=True)
    model_name = Column(String, nullable=False)
    model_nm = Column(String, nullable=True)  # model version / name code
    algorithm = Column(String, nullable=False)  # XGBoost, RandomForest, etc.
    training_accuracy = Column(Float, nullable=True)
    testing_accuracy = Column(Float, nullable=True)
    file_path = Column(String, nullable=False)  # Saved binary file path

    # Relationships
    predictions = relationship("PredictionResult", back_populates="model")

class PredictionResult(Base):
    __tablename__ = "prediction_results"

    prediction_id = Column(Integer, primary_key=True, index=True)
    loan_id = Column(Integer, ForeignKey("loan_applications.loan_id"), nullable=False)
    model_id = Column(Integer, ForeignKey("models.model_id"), nullable=False)
    prediction_status = Column(String, nullable=False)  # Approved, Rejected
    probability_score = Column(Float, nullable=False)
    prediction_time = Column(DateTime, default=datetime.datetime.utcnow)

    # Relationships
    loan = relationship("LoanApplication", back_populates="prediction_results")
    model = relationship("Model", back_populates="predictions")
