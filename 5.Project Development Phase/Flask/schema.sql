-- Smart Lender Database Schema
-- SQLite DDL for all ORM-mapped tables

CREATE TABLE IF NOT EXISTS users (
    user_id   INTEGER PRIMARY KEY AUTOINCREMENT,
    name      TEXT    NOT NULL,
    email     TEXT    NOT NULL UNIQUE,
    role      TEXT    NOT NULL,           -- 'Credit Officer' or 'Applicant'
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS applicant_profiles (
    applicant_id  INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id       INTEGER REFERENCES users(user_id),
    gender        TEXT    NOT NULL,       -- 'Male', 'Female'
    married       TEXT    NOT NULL,       -- 'Yes', 'No'
    education     TEXT    NOT NULL,       -- 'Graduate', 'Not Graduate'
    self_employed TEXT    NOT NULL,       -- 'Yes', 'No'
    dependents    INTEGER DEFAULT 0,
    property_area TEXT    NOT NULL        -- 'Urban', 'Semiurban', 'Rural'
);

CREATE TABLE IF NOT EXISTS credit_histories (
    credit_id             INTEGER PRIMARY KEY AUTOINCREMENT,
    applicant_id          INTEGER NOT NULL REFERENCES applicant_profiles(applicant_id),
    credit_score          REAL    NOT NULL,
    credit_history_status INTEGER NOT NULL  -- 1 (good), 0 (bad)
);

CREATE TABLE IF NOT EXISTS loan_applications (
    loan_id              INTEGER PRIMARY KEY AUTOINCREMENT,
    applicant_id         INTEGER NOT NULL REFERENCES applicant_profiles(applicant_id),
    income               REAL    NOT NULL,
    coapplicant_income   REAL    NOT NULL,
    loan_amount          REAL    NOT NULL,  -- in thousands
    loan_term            INTEGER NOT NULL,  -- in months
    application_date     DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS models (
    model_id          INTEGER PRIMARY KEY AUTOINCREMENT,
    model_name        TEXT    NOT NULL,
    model_nm          TEXT,               -- version / code name
    algorithm         TEXT    NOT NULL,   -- e.g. 'XGBoost Classifier'
    training_accuracy REAL,
    testing_accuracy  REAL,
    file_path         TEXT    NOT NULL
);

CREATE TABLE IF NOT EXISTS prediction_results (
    prediction_id     INTEGER PRIMARY KEY AUTOINCREMENT,
    loan_id           INTEGER NOT NULL REFERENCES loan_applications(loan_id),
    model_id          INTEGER NOT NULL REFERENCES models(model_id),
    prediction_status TEXT    NOT NULL,   -- 'Approved' or 'Rejected'
    probability_score REAL    NOT NULL,
    prediction_time   DATETIME DEFAULT CURRENT_TIMESTAMP
);
