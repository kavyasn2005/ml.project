from django.shortcuts import render
import joblib
import numpy as np

# Load the trained machine learning model from the 'model.pkl' file
# This model is a scikit-learn LinearRegression trained to predict sales based on quantity
model = joblib.load('model.pkl')

def predict_sales(request):
    """
    View function to handle both GET and POST requests for sales prediction.

    GET request: Displays the form for user input.
    POST request: Processes the form data, makes a prediction using the ML model,
                  and displays the result.

    Args:
        request: Django HttpRequest object containing request data.

    Returns:
        HttpResponse: Rendered HTML template with form and optional prediction.
    """
    prediction = None  # Initialize prediction as None (for GET requests)

    if request.method == 'POST':
        # Handle form submission (POST request)
        # Get the quantity value from the form input
        quantity_str = request.POST.get('quantity')

        # Convert the quantity to a float (since form inputs are strings)
        quantity = float(quantity_str)

        # Prepare the input for the model (needs to be a 2D array for sklearn)
        input_data = np.array([[quantity]])

        # Use the loaded model to predict sales
        prediction = model.predict(input_data)[0]

        # prediction is now a float value representing predicted sales

    # Render the template with the prediction (None for GET, float for POST)
    # The template will show the form and display prediction if it exists
    return render(request, 'ml_app/predict.html', {'prediction': prediction})
