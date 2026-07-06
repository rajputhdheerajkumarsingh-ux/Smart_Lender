"""
init_db.py — Smart Lender Database Initialization & Seeding Script
Run this script once before starting the Flask/FastAPI server to create
all SQLite tables and insert a default ML model record.

Usage (from project root):
    python "5.Project Development Phase/Flask/init_db.py"

Or from inside the Flask/ directory:
    python init_db.py
"""

import sys
import os

# Ensure the project root is on the path so 'app' package is importable
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..')))

from app.database import engine, SessionLocal
from app import models

def create_tables():
    """Create all database tables defined in models.py."""
    models.Base.metadata.create_all(bind=engine)
    print("[OK] All tables created (or already exist).")

def seed_model_record():
    """Insert a default model record so /api/predictions/run works out-of-the-box."""
    db = SessionLocal()
    try:
        existing = db.query(models.Model).filter(models.Model.model_nm == "xgboost_v1").first()
        if not existing:
            default_model = models.Model(
                model_name="XGBoost Loan Predictor v1",
                model_nm="xgboost_v1",
                algorithm="XGBoost Classifier",
                training_accuracy=None,   # Updated after training
                testing_accuracy=None,
                file_path="app/models/xgboost_loan_model.pkl"
            )
            db.add(default_model)
            db.commit()
            print("[OK] Default model record seeded (model_id=1).")
        else:
            print("[INFO] Model record already exists — skipping seed.")
    finally:
        db.close()

if __name__ == "__main__":
    print("Initializing Smart Lender database...")
    create_tables()
    seed_model_record()
    print("Database initialization complete.")
    print("Next step: Run 'python scripts/train_model.py' to train and serialize the ML model.")
