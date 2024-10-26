from django.urls import path, include
from . import views
from  user import  views as user_vies

urlpatterns = [
    path('', views.home, name='home'),
    path('buy/', views.buy, name='buy'),
    path('sell/', views.sell, name='sell'),
    path('rent/', views.rent, name='rent'),
    path('property/<int:property_id>/', views.details, name='details'),
    path('about/', views.about, name='about'),
    path('terms/', views.terms, name='terms'),
    path('contact-us/', views.contactUs, name='contactUs'),
    path('cookies/', views.contactUs, name='cookies'),
    path('privacy-policy/', views.privacyPolicy, name='privacy'),
    path('search/', views.search, name='search'),
    path('property/<int:property_id>/toggle-favorite/', views.toggle_favorite, name='toggle-favorite'),
    path('favorites/', views.favorite_properties, name='favorite-properties'),
    path('realtors/', include('realtors.urls', namespace='realtors')),
]