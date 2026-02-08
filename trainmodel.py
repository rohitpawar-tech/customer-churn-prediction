import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingClassifier
from joblib import dump
import os

# Create model folder
os.makedirs("model", exist_ok=True)

# ✅ Correct Excel file name
df = pd.read_csv("archive/Churn_Modelling.xls.csv")


# Drop unnecessary columns
df.drop(['RowNumber', 'CustomerId', 'Surname'], axis=1, inplace=True)

# Encode categorical columns
le = LabelEncoder()
for col in df.select_dtypes(include='object'):
    df[col] = le.fit_transform(df[col])

# Features and target
X = df.drop("Exited", axis=1)
y = df["Exited"]

# Feature scaling
scaler = StandardScaler()
X = scaler.fit_transform(X)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = GradientBoostingClassifier()
model.fit(X_train, y_train)

# Save model
dump(model, "model/churn_model.pkl")

print("✅ Model trained & saved successfully!")
