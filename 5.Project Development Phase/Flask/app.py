# pyrefly: ignore [missing-import]
import numpy as np
import pickle
import pandas
import os
from flask import Flask, request, render_template

app = Flask(__name__)

# Load the saved model file (loan_model.pkl or rdf.pkl)
model = None
model_names = ['loan_model.pkl', 'rdf.pkl']

# First try loading relative to the app.py file location
for name in model_names:
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), name)
    if os.path.exists(path):
        try:
            with open(path, 'rb') as f:
                model = pickle.load(f)
            print(f"Loaded model from '{path}' successfully.")
            break
        except Exception as e:
            print(f"Error loading model from {path}: {e}")

# If not loaded, try fallback files
if model is None:
    fallback_paths = [
        'rdf.pkl',
        'loan_model.pkl',
        '5.Project Development Phase/Flask/loan_model.pkl',
        '5.Project Development Phase/Flask/rdf.pkl',
        'app/models/xgboost_loan_model.pkl'
    ]
    for path in fallback_paths:
        if os.path.exists(path):
            try:
                with open(path, 'rb') as f:
                    model = pickle.load(f)
                print(f"Loaded fallback model from '{path}' successfully.")
                break
            except Exception as e:
                print(f"Error loading fallback model from {path}: {e}")


@app.route('/')  # rendering the landing page
def home():
    return render_template('home.html')

@app.route('/predict', methods=["POST", "GET"])  # rendering the prediction form page
def predict():
    return render_template("predict.html")

@app.route('/predict/submit', methods=["POST", "GET"])  # support both routes
@app.route('/submit', methods=["POST", "GET"])  # route to retrieve values, predict, and show results
def submit():
    if request.method == "POST":
        try:
            # retrieve values from form
            input_feature = [float(x) for x in request.form.values()]
            input_feature = [np.array(input_feature)]
            print(f"Input Features: {input_feature}")

            names = ['Gender', 'Married', 'Dependents', 'Education', 'Self_Employed', 'ApplicantIncome',
                     'CoapplicantIncome', 'LoanAmount', 'Loan_Amount_Term', 'Credit_History', 'Property_Area']
            data = pandas.DataFrame(input_feature, columns=names)
            print(f"Dataframe:\n{data}")

            # run model prediction
            if model is not None:
                prediction = model.predict(data)
                prediction = int(prediction[0])
            else:
                # Fallback mock prediction if model failed to load
                prediction = 1 if float(request.form.get('Credit_History', 0)) == 1 else 0

            print(f"Prediction: {prediction}")

            if prediction == 1:
                return render_template("submit.html", prediction="Approved")
            else:
                return render_template("submit.html", prediction="Rejected")

        except Exception as e:
            print(f"Error during prediction routing: {e}")
            return render_template("submit.html", prediction="Rejected")
            
    return render_template("predict.html")

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, port=port)
