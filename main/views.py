from django.shortcuts import render, get_object_or_404
from .models import Property

def buy(request):
    properties = Property.objects.all
    context = {'properties':properties}
    return render(request, 'Buy_Page.html', context)

def home(request):
    return render(request, 'home.html')

def sell(request):
    return render(request, 'Sell_Page.html')

def rent(request):
    return render(request, 'Rent_Page.html')

def details(request, property_id):
    property = get_object_or_404(Property, id=property_id)
    return render(request, 'details.html', {'property': property})

# Create your views here.
