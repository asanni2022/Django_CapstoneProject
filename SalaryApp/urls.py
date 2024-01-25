from django.urls import path
from .views import home_salaryapp_view

urlpatterns = [
    path('', home_salaryapp_view, name='home'), # Forwarding the home page from project level urls.py to app level urls.py
]