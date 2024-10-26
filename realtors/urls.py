# realtors/urls.py
from django.urls import path
from . import views

app_name = 'realtors'

urlpatterns = [
    path('contact/', views.contact_agent, name='contact'),
]