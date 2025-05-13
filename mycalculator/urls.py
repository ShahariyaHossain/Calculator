from django.urls import path
# Import the views module from the calculator app
from . import views
# URL configuration for the calculator app
urlpatterns = [
    path('', views.home, name="home"),  # Home page
    path('normal/', views.normal_cal, name="normal"),  # Include URLs from the calculator app
    # Add other app URLs here if needed
]
