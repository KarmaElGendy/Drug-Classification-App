# Drug-Classification-App
This tool helps classify drugs based on patient attributes. 

![Prediction](https://github.com/KarmaElGendy/Drug-Classification-App/blob/main/images/Prediction.png)
![Result](https://github.com/KarmaElGendy/Drug-Classification-App/blob/main/images/Result.png)


## Overview

This Flask application predicts drug classification based on user input, such as age, sex, blood pressure, cholesterol levels, and sodium-to-potassium ratio. The prediction is made using a Logistic Regression model.

## Dataset

The dataset used for training the model is available on Kaggle: [Drug Classification Dataset](https://www.kaggle.com/datasets/prathamtripathi/drug-classification).

### Drug Information

- **Drug x** and **Drug y**: Prescribed based on the potassium ratio in the blood.
- **Drug c**: Used for patients with low blood pressure.
- **Drug a** and **Drug b**: Prescribed for high blood pressure. Drug a is for patients under 50 years old, while Drug b is for those over 50 years old.

## Features

- **Input Fields**: Age, Sex, BP, Cholesterol, Na_to_K
- **Machine Learning**: Logistic Regression model
- **Data Handling**: One-hot encoding for categorical variables
- **Prediction**: Classifies drugs into categories based on input data

## Project Structure

Drug-Classification-App/
├── images/
│   └── Prediction.png
├── static/
│   └── styles.css
├── templates/
│   ├── index.html
│   └── result.html
├── app.py
├── feature_coefficients.pkl
├── model.pkl
├── README.md
└── requirements.txt


## Usage

1. Clone the repository:

    ```bash
    git clone https://github.com/KarmaElGendy/Drug-Classification-App.git
    ```

2. Navigate to the project directory:

    ```bash
    cd Drug-Classification-App
    ```

3. Install the required Python packages:

    ```bash
    pip install -r requirements.txt
    ```

4. Run the Flask app:

    ```bash
    python app.py
    ```

5. Open your browser and go to `http://127.0.0.1:5000/` to use the application.

## How It Works

1. The user fills out the form with their age, sex, BP, cholesterol, and Na_to_K ratio.
2. The input data is processed and encoded to match the model's expected input format.
3. The Logistic Regression model predicts the drug classification based on the input.
4. The prediction result is displayed to the user on the results page.

## Contributing

Feel free to fork this repository, create a new branch, and submit a pull request for any improvements or bug fixes.


