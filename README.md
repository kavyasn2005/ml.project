# Ecommerce Sales Prediction Model

## Project Description

This is a Django-based web application that uses a machine learning model to predict ecommerce sales based on the quantity of items. The application provides a simple web interface where users can input a quantity value, and the model will predict the corresponding sales amount.

The machine learning model is a Linear Regression model trained on ecommerce sales data, implemented using scikit-learn. The trained model is saved in a pickle file (`model.pkl`) and loaded into the Django application for making predictions.

## Features

- **Sales Prediction**: Input a quantity value to get a predicted sales amount.
- **Web Interface**: Simple HTML form for user input and displaying results.
- **Django Framework**: Built using Django for robust web development.
- **Machine Learning Integration**: Utilizes scikit-learn for the prediction model.

## Installation

1. **Clone the Repository**:
   ```
   git clone <repository-url>
   cd ecommerce_ml_project
   ```

2. **Install Dependencies**:
   Make sure you have Python installed (version 3.8 or higher recommended).
   ```
   pip install django scikit-learn joblib numpy
   ```

3. **Run Migrations** (if needed):
   ```
   python manage.py migrate
   ```

4. **Start the Development Server**:
   ```
   python manage.py runserver
   ```

5. **Access the Application**:
   Open your web browser and go to `http://127.0.0.1:8000/` to use the sales prediction feature.

## Usage

1. Navigate to the application URL.
2. Enter a quantity value in the input field.
3. Click the "Predict Sales" button.
4. The predicted sales amount will be displayed below the form.

## Model Details

- **Algorithm**: Linear Regression (from scikit-learn)
- **Input**: Quantity (numeric value)
- **Output**: Predicted Sales (numeric value)
- **Model File**: `model.pkl` (pickle file containing the trained model)
- **Training Data**: Ecommerce sales data (refer to the Jupyter notebook `ecommerce_sales_data.ipynb` for details on data preparation and model training)

The model was trained to find a linear relationship between the quantity of items and the sales amount. The prediction is made using the formula: `sales = coefficient * quantity + intercept`.

## Dependencies

- Django 6.0.2
- scikit-learn
- joblib
- numpy

## Project Structure

```
ecommerce_ml_project/
├── ecommerce_ml_project/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── __pycache__/
├── ml_app/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   ├── views.py
│   ├── migrations/
│   └── templates/
│       └── ml_app/
│           └── predict.html
├── model.pkl
├── db.sqlite3
├── manage.py
└── README.md
```

## Contributing

Feel free to fork the repository and submit pull requests for improvements or bug fixes.

## License

This project is open-source. Please check the license file for more details.
