

### **GitHub Repository Name:**
:

```
customer-churn-prediction
```

---

### **GitHub Repository Description:**

```
Web-based machine learning application to predict customer churn using Gradient Boosting and Flask.
```

---

### **README.md**

# Customer Churn Prediction

This project is a **web-based machine learning application** that predicts whether a customer will churn using a **Gradient Boosting Classifier**. The application is built with **Python**, **Flask**, and **HTML/CSS**, and allows users to input customer data via a web form for real-time prediction.

## Features

- Trains a **Gradient Boosting Classifier** on customer churn data.
- Web interface built using **Flask** with 50 input features.
- **Internal CSS** styling with animations and responsive design.
- Handles both **numerical and categorical features**.
- Saves the trained model using **Joblib** for deployment.
- Scrollable, interactive form with a loading spinner for prediction.

## Project Structure
With All Independencis
```

customer-churn-prediction/
│
├─ model/
│   └─ churn_model.pkl           # Trained ML model
├─ templates/
|-- login.html
│   ├─ index.html                # Main input form
│   └─ result.html               # Prediction result page
├─ trainModel.py                 # Script to train the model
├─ app.py                        # Flask application
├─ requirements.txt              # Python dependencies
└─ README.md                     # Project documentation

````

## Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/customer-churn-prediction.git
cd customer-churn-prediction
````

2. Create a virtual environment and activate it:

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

## Usage

1. Train the model (optional if `churn_model.pkl` is already provided):

```bash
python trainModel.py
```

2. Run the Flask application:

```bash
python app.py
```

3. Open your browser and go to:

```
http://127.0.0.1:5000/
```

4. Fill in the customer data form and click **Run Prediction** to see the result.

## Dependencies

* Python 3.10+
* Flask
* Pandas
* NumPy
* scikit-learn
* Joblib

Install all dependencies with:

```bash
pip install flask pandas numpy scikit-learn joblib
```

## License

This project is licensed under the MIT License.

```

Do you want me to do that next?
```



