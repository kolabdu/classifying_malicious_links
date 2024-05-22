from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('predict/', views.predict_category, name='predict_category'),  # Add this line
    # Other app-specific URL patterns go here
]
