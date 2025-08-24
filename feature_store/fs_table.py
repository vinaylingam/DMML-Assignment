import sqlite3

# Connect (or create) database
conn = sqlite3.connect("feature_store.db")
cursor = conn.cursor()

# Create the table
cursor.execute("""
CREATE TABLE IF NOT EXISTS feature_store (
    customerID TEXT PRIMARY KEY,
    gender TEXT,
    SeniorCitizen INTEGER,
    Partner INTEGER,
    Dependents INTEGER,
    tenure INTEGER,
    PhoneService INTEGER,
    MonthlyCharges REAL,
    TotalCharges REAL,
    Churn INTEGER,

    InternetService_DSL INTEGER,
    InternetService_Fiber_optic INTEGER,
    InternetService_No INTEGER,

    MultipleLines_No INTEGER,
    MultipleLines_No_phone_service INTEGER,
    MultipleLines_Yes INTEGER,

    OnlineSecurity_No INTEGER,
    OnlineSecurity_No_internet_service INTEGER,
    OnlineSecurity_Yes INTEGER,

    OnlineBackup_No INTEGER,
    OnlineBackup_No_internet_service INTEGER,
    OnlineBackup_Yes INTEGER,

    source_huggingface INTEGER,
    source_kaggle INTEGER,

    PaperlessBilling_0 INTEGER,
    PaperlessBilling_1 INTEGER,

    DeviceProtection_No INTEGER,
    DeviceProtection_No_internet_service INTEGER,
    DeviceProtection_Yes INTEGER,

    TechSupport_No INTEGER,
    TechSupport_No_internet_service INTEGER,
    TechSupport_Yes INTEGER,

    StreamingTV_No INTEGER,
    StreamingTV_No_internet_service INTEGER,
    StreamingTV_Yes INTEGER,

    StreamingMovies_No INTEGER,
    StreamingMovies_No_internet_service INTEGER,
    StreamingMovies_Yes INTEGER,

    Contract_Month-to-month INTEGER,
    Contract_One_year INTEGER,
    Contract_Two_year INTEGER,

    PaymentMethod_Bank_transfer_automatic INTEGER,
    PaymentMethod_Credit_card_automatic INTEGER,
    PaymentMethod_Electronic_check INTEGER,
    PaymentMethod_Mailed_check INTEGER
);
""")

print("✅ Feature store table created successfully.")

# Commit & close
conn.commit()
conn.close()
