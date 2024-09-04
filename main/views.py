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

def contactUs(request):
    return render(request, 'Contact_us.html')

def privacyPolicy(request):
    return render(request, 'Privacy_Policy.html')

def terms(request):
    return render(request, 'Terms_&_Conditions.html')

def cookies(request):
    return render(request, 'Cookie_Policy.html')

def about(request):
    return render(request, 'About_us.html')

