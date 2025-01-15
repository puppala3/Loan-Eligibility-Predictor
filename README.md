# Loan-Eligibility-Predictor
This project implements a machine learning model to predict loan eligibility based on various applicant features. It includes data preprocessing, model training, evaluation, and a web application for making predictions
# Features
- Data preprocessing and feature engineering
- Implementation of multiple classification algorithms
   - Logistic Regression
   - K-Nearest Neighbor (KNN)
   - Gaussian Naïve Bayes
   - Linear Discriminant Analysis
   - Quadratic Discriminant Analysis
   - Decision Tree
   - Random Forest
   - Support Vector Machine (SVM)
- Model evaluation using various metrics (Accuracy, TPR, TNR)
- Web application for real-time predictions using Flask
# Project Structure
- 'code.ipynb:' Jupyter notebook containing data analysis and model training code
- 'app.py:' Flask application for the web interface
- 'index.html:' HTML template for the web application
- 'loanpred.pkl:' Pickle file containing the trained SVM model
# Usage
- To run the web application:
```bash
  python app.py
```
- Open a web browser and go to http://localhost:5000
- Enter the applicant's details in the form and click "Predict" to get the loan eligibility prediction

#  Model Performance
The SVM (linear) model achieved the highest accuracy of 82.08% and was selected for deployment.





