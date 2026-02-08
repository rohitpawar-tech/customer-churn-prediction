from flask import Flask, render_template, request
from joblib import load
import numpy as np

app = Flask(__name__)

# Load trained model
model = load("model/churn_model.pkl")

# Mappings for categorical features
geography_mapping = {"France": 0, "Germany": 1, "Spain": 2}
gender_mapping = {"Male": 1, "Female": 0}

@app.route('/')
def home():
    # Render the form with example values
    example_data = {
        "CreditScore": 650,
        "Geography": "France",
        "Gender": "Male",
        "Age": 40,
        "Tenure": 12,
        "Balance": 50000,
        "NumOfProducts": 2,
        "HasCrCard": 1,
        "IsActiveMember": 1,
        "EstimatedSalary": 60000
    }
    return render_template("index.html", data=example_data)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Collect all features from form
        CreditScore = float(request.form['CreditScore'])
        Geography = request.form['Geography']
        Gender = request.form['Gender']
        Age = float(request.form['Age'])
        Tenure = float(request.form['Tenure'])
        Balance = float(request.form['Balance'])
        NumOfProducts = float(request.form['NumOfProducts'])
        HasCrCard = float(request.form['HasCrCard'])
        IsActiveMember = float(request.form['IsActiveMember'])
        EstimatedSalary = float(request.form['EstimatedSalary'])

        # Encode categorical features
        Geography_encoded = geography_mapping.get(Geography, 0)
        Gender_encoded = gender_mapping.get(Gender, 0)

        # Create feature array
        features = np.array([[CreditScore, Geography_encoded, Gender_encoded, Age, Tenure,
                              Balance, NumOfProducts, HasCrCard, IsActiveMember, EstimatedSalary]])

        # Make prediction
        prediction = model.predict(features)[0]

        if prediction == 1:
            result = "Customer Will Churn"
        else:
            result = "Customer Will Stay"

        return render_template("result.html", result=result)

    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
    app.run(debug=True)
