from django.urls import path
from . import views

# URL patterns for the ml_app (machine learning application)
# This file defines the URL routing for the ml_app Django application
urlpatterns = [
    # Root URL ('') maps to the predict_sales view
    # This handles both GET (show form) and POST (process prediction) requests
    path('', views.predict_sales, name='predict_sales'),
]
