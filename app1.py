import sys
# Clean path to prevent circular import conflicts on user's machine
sys.path = [p for p in sys.path if not (p.endswith("Python313") or p.endswith("Python313\\"))]

import numpy as np
import pickle
import pandas
import os
from flask import Flask, request, render_template

app = Flask(__name__)

# Load the saved model file (rdf.pkl) with try-except fallback to the trained xgboost model
try:
    model = pickle.load(open('rdf.pkl', 'rb'))
    print("Loaded model from 'rdf.pkl' successfully.")
except FileNotFoundError:
    try:
        model = pickle.load(open('app/models/xgboost_loan_model.pkl', 'rb'))
        print("rdf.pkl not found. Loaded fallback model from 'app/models/xgboost_loan_model.pkl'.")
    except Exception as e:
        print(f"Error loading fallback model: {e}")
        model = None

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
