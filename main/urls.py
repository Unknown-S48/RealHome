from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('buy/', views.buy, name='buy'),
    path('sell/', views.sell, name='sell'),
    path('rent/', views.rent, name='rent'),
    path('property/<int:property_id>/', views.details, name='details'),

]