import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib
import os

# Load dataset
data_path = os.path.join("data", "Medicaldataset.csv")
df = pd.read_csv(data_path)
df = df.rename(columns={
    "Heart rate": "heart_rate",
    "Systolic blood pressure": "sbp",
    "Diastolic blood pressure": "dbp",
    "Blood sugar": "blood_sugar",
    "CK-MB": "ck_mb",
    "Troponin": "troponin",
    "Gender": "gender",
    "Age": "age"
})


print("✅ Dataset loaded")
print("Columns:", df.columns)

# 🎯 Target column
TARGET_COLUMN = "Result"

# Features & target
X = df.drop(TARGET_COLUMN, axis=1)
y = df[TARGET_COLUMN]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)
model.fit(X_train, y_train)

# Save model
os.makedirs("app/model", exist_ok=True)
joblib.dump(model, "app/model/heart_model.pkl")

print("✅ Model trained & saved as heart_model.pkl")
