from flask import Flask, render_template, request
import pickle
from sklearn import svm
import os

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/predict", methods=["POST"])
def predict():
    if request.method == "POST":
            Gender = request.form["Gender"]
            Married = request.form["Married"]
            Dependents = request.form["Dependents"]
            Education = request.form["Education"]
            Self_Employed = request.form["Self_Employed"]
            Applicant_Income = request.form["Applicant_Income"]
            Coapplicant_Income = request.form["Coapplicant_Income"]
            Loan_Amount = request.form["Loan_Amount"]
            Loan_Amount_Term = request.form["Loan_Amount_Term"]
            Credit_History = request.form["Credit_History"]
            Property_Area = request.form["Property_Area"]

            data = [[int(Gender), int(Married), int(Dependents), int(Education), int(Self_Employed), float(Applicant_Income), float(Coapplicant_Income), float(Loan_Amount), float(Loan_Amount_Term), int(Credit_History), int(Property_Area)]]

            svm_classifier = pickle.load(open("C:\\Users\\ADMIN\\Documents\\CS 677\\Dump\\loanpred.pkl", "rb"))
            pred = svm_classifier.predict(data)[0]
    return render_template("index.html", prediction=int(pred))


if __name__ == "__main__":
    app.run()
