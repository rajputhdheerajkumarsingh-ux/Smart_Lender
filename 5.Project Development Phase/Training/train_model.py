import os
import pickle
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score
import xgboost as xgb
import sqlite3
import datetime

def generate_synthetic_data(num_samples=1000, random_state=42):
    np.random.seed(random_state)
    
    # 1. Gender (80% Male, 20% Female)
    gender = np.random.choice(["Male", "Female"], size=num_samples, p=[0.8, 0.2])
    
    # 2. Married (65% Yes, 35% No)
    married = np.random.choice(["Yes", "No"], size=num_samples, p=[0.65, 0.35])
    
    # 3. Dependents (57% 0, 17% 1, 17% 2, 9% 3+)
    dependents = np.random.choice([0, 1, 2, 3], size=num_samples, p=[0.57, 0.17, 0.17, 0.09])
    
    # 4. Education (78% Graduate, 22% Not Graduate)
    education = np.random.choice(["Graduate", "Not Graduate"], size=num_samples, p=[0.78, 0.22])
    
    # 5. Self_Employed (15% Yes, 85% No)
    self_employed = np.random.choice(["Yes", "No"], size=num_samples, p=[0.15, 0.85])
    
    # 6. ApplicantIncome (log-normal distribution)
    applicant_income = np.random.lognormal(mean=8.4, sigma=0.6, size=num_samples).astype(float)
    # Clip applicant income to realistic bounds ($1,500 to $80,000)
    applicant_income = np.clip(applicant_income, 1500, 80000)
    
    # 7. CoapplicantIncome
    has_coapplicant = np.random.choice([True, False], size=num_samples, p=[0.5, 0.5])
    coapplicant_income = np.zeros(num_samples)
    coapplicant_income[has_coapplicant] = np.random.lognormal(mean=7.2, sigma=0.8, size=sum(has_coapplicant)).astype(float)
    coapplicant_income = np.clip(coapplicant_income, 0, 40000)
    
    # 8. LoanAmount (log-normal, correlated with Total Income)
    total_income = applicant_income + coapplicant_income
    loan_amount = (total_income * np.random.normal(0.25, 0.05, size=num_samples)).astype(float)
    # Convert to thousands, clip to reasonable bounds ($9k to $700k)
    loan_amount = np.clip(loan_amount / 10, 9, 700)
    
    # 9. Loan_Amount_Term (mostly 360 days/months)
    loan_term = np.random.choice([12, 36, 60, 84, 120, 180, 240, 300, 360, 480], size=num_samples, p=[0.01, 0.01, 0.01, 0.01, 0.01, 0.08, 0.01, 0.01, 0.84, 0.01])
    
    # 10. Credit_History (84% 1.0, 16% 0.0)
    credit_history = np.random.choice([1.0, 0.0], size=num_samples, p=[0.84, 0.16])
    
    # 11. Property_Area
    property_area = np.random.choice(["Urban", "Semiurban", "Rural"], size=num_samples, p=[0.33, 0.34, 0.33])
    
    # Calculate target variable: Loan_Status (Approved: 1, Rejected: 0)
    # The probability of loan approval depends heavily on Credit_History, Total Income vs Loan Amount, and Education
    p_approval = np.zeros(num_samples)
    for i in range(num_samples):
        prob = 0.05  # Base probability of approval
        
        # Credit history is the main factor
        if credit_history[i] == 1.0:
            prob += 0.65
        else:
            prob -= 0.1
            
        # Debt to income check (Loan Amount vs Total Income)
        # Total Income is monthly, Loan Amount is in thousands.
        # If LoanAmount * 1000 / (Total Income * Term) is high, it's risky
        monthly_repayment = (loan_amount[i] * 1000) / loan_term[i]
        debt_to_income = monthly_repayment / (total_income[i] / 12)
        if debt_to_income > 0.4:
            prob -= 0.25
        elif debt_to_income < 0.2:
            prob += 0.15
            
        # Education bonus
        if education[i] == "Graduate":
            prob += 0.05
            
        # Property area bonus (Semiurban is preferred in standard datasets)
        if property_area[i] == "Semiurban":
            prob += 0.05
            
        # Dependents impact
        if dependents[i] > 2:
            prob -= 0.05
            
        p_approval[i] = np.clip(prob, 0.01, 0.99)
        
    loan_status = np.random.binomial(1, p_approval)
    
    # Create DataFrame
    df = pd.DataFrame({
        "gender": gender,
        "married": married,
        "dependents": dependents,
        "education": education,
        "self_employed": self_employed,
        "applicant_income": applicant_income,
        "coapplicant_income": coapplicant_income,
        "loan_amount": loan_amount,
        "loan_term": loan_term,
        "credit_history": credit_history,
        "property_area": property_area,
        "loan_status": loan_status
    })
    
    return df

def train_and_save_model():
    print("Generating synthetic loan applicant dataset...")
    df = generate_synthetic_data(1200)
    
    X = df.drop(columns=["loan_status"])
    y = df["loan_status"]
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
    
    # Define categorical and numerical features
    categorical_features = ["gender", "married", "education", "self_employed", "property_area"]
    numerical_features = ["dependents", "applicant_income", "coapplicant_income", "loan_amount", "loan_term", "credit_history"]
    
    # Preprocessing pipelines
    categorical_transformer = OneHotEncoder(drop="first", handle_unknown="ignore")
    numerical_transformer = StandardScaler()
    
    preprocessor = ColumnTransformer(
        transformers=[
            ("num", numerical_transformer, numerical_features),
            ("cat", categorical_transformer, categorical_features)
        ]
    )
    
    # Create full pipeline with XGBoost
    print("Training XGBoost Classifier...")
    model_pipeline = Pipeline(
        steps=[
            ("preprocessor", preprocessor),
            ("classifier", xgb.XGBClassifier(
                n_estimators=100,
                max_depth=4,
                learning_rate=0.1,
                random_state=42,
                use_label_encoder=False,
                eval_metric="logloss"
            ))
        ]
    )
    
    model_pipeline.fit(X_train, y_train)
    
    # Evaluate
    train_preds = model_pipeline.predict(X_train)
    test_preds = model_pipeline.predict(X_test)
    
    train_acc = float(accuracy_score(y_train, train_preds))
    test_acc = float(accuracy_score(y_test, test_preds))
    
    print(f"Training Accuracy: {train_acc:.4f}")
    print(f"Testing Accuracy: {test_acc:.4f}")
    
    # Save model pipeline
    os.makedirs("app/models", exist_ok=True)
    model_path = "app/models/xgboost_loan_model.pkl"
    with open(model_path, "wb") as f:
        pickle.dump(model_pipeline, f)
    print(f"Model saved successfully to {model_path}")
    
    # Insert metadata into SQLite DB
    db_path = "loans.db"
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # Create models table if it does not exist (FastAPI will also create it, but let's make sure)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS models (
            model_id INTEGER PRIMARY KEY AUTOINCREMENT,
            model_name TEXT NOT NULL,
            model_nm TEXT,
            algorithm TEXT NOT NULL,
            training_accuracy REAL,
            testing_accuracy REAL,
            file_path TEXT NOT NULL
        )
    """)
    
    # Check if this model is already registered
    cursor.execute("SELECT model_id FROM models WHERE model_nm = 'xgboost_v1'")
    existing = cursor.fetchone()
    
    if existing:
        cursor.execute("""
            UPDATE models 
            SET training_accuracy = ?, testing_accuracy = ?, file_path = ?
            WHERE model_id = ?
        """, (train_acc, test_acc, model_path, existing[0]))
        print(f"Updated existing model record in database with ID: {existing[0]}")
    else:
        cursor.execute("""
            INSERT INTO models (model_name, model_nm, algorithm, training_accuracy, testing_accuracy, file_path)
            VALUES (?, ?, ?, ?, ?, ?)
        """, ("XGBoost Loan Predictor v1", "xgboost_v1", "XGBoost Classifier", train_acc, test_acc, model_path))
        print(f"Registered new model in database.")
        
    conn.commit()
    conn.close()

if __name__ == "__main__":
    train_and_save_model()
