from flask import Flask, render_template, request
import pickle
import pandas as pd

app = Flask(__name__)

# Load the Logistic Regression model
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

# Load the feature coefficients
with open('feature_coefficients.pkl', 'rb') as f:
    feature_coeffs = pickle.load(f)
    feature_names = list(feature_coeffs.keys())  # Extract feature names

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Extract data from form
    data = {
        'Age': [request.form['age']],
        'Sex': [request.form['sex']],
        'BP': [request.form['bp']],
        'Cholesterol': [request.form['cholesterol']],
        'Na_to_K': [request.form['na_to_k']]
    }

    input_data = pd.DataFrame(data)

    # Convert categorical variables using one-hot encoding
    input_data_encoded = pd.get_dummies(input_data)

    # Ensure all model features are present in the input data
    for feature in feature_names:
        if feature not in input_data_encoded:
            input_data_encoded[feature] = 0  # Add missing dummy variables as 0s

    # Reorder to match the training model's feature input
    input_data_final = input_data_encoded[feature_names]
    
    # Predict
    prediction = model.predict(input_data_final)
    return render_template('result.html', prediction=prediction[0])

if __name__ == "__main__":
    app.run(debug=True)
