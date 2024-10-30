from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.decorators.http import require_http_methods
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.contrib.auth.decorators import login_required
from django.db.models import Count
from .models import CustomUser
from django.urls import reverse
from main.models import Property, Favorite  
import logging
from django.contrib import messages
from realtors.models import Realtor

# Set up logger for debugging
logger = logging.getLogger(__name__)

# Home View
def home(request):
    return render(request, 'pages/home.html')

# Login View
@ensure_csrf_cookie
@require_http_methods(["GET", "POST"])
def login_view(request):
    if request.method == 'GET':
        return render(request, 'auth/login.html')

    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        logger.info(f"Login attempt for username: {username}")

        # Validate input
        if not username or not password:
            logger.warning("Login attempt with missing username or password")
            return JsonResponse({'success': False, 'message': 'Username and password are required.'}, status=400)

        # Authenticate user
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            logger.info(f"Successful login for username: {username}")
            return JsonResponse({'success': True, 'redirect_url': reverse('auth:dashboard')})
        else:
            logger.warning(f"Failed login attempt for username: {username}")
            return JsonResponse({'success': False, 'message': 'Invalid credentials'}, status=400)

    return JsonResponse({'success': False, 'message': 'Invalid request method'}, status=405)

# Register View
@ensure_csrf_cookie
@require_http_methods(["GET", "POST"])
def register_view(request):
    if request.method == 'GET':
        return render(request, 'auth/register.html')

    logger.info(f"Registration attempt with data: {request.POST}")
    
    try:
        # Extract form data
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        phone = request.POST.get('phone')
        user_type = request.POST.get('userType')
        license_number = request.POST.get('licenseNumber', '')

        # Validate required fields
        if not all([name, email, password, phone, user_type]):
            return JsonResponse({
                'success': False,
                'message': 'All fields are required.'
            }, status=400)

        # Validate realtor fields
        if user_type == 'realtor' and not license_number:
            return JsonResponse({
                'success': False,
                'message': 'License number is required for realtors.'
            }, status=400)

        # Check if email exists
        if CustomUser.objects.filter(email=email).exists():
            return JsonResponse({
                'success': False,
                'message': 'Email already exists.'
            }, status=400)

        try:
            # Start with user creation
            user = CustomUser.objects.create_user(
                username=email,
                email=email,
                password=password,
                first_name=name.split()[0],
                last_name=' '.join(name.split()[1:]) if len(name.split()) > 1 else '',
                phone=phone,
                user_type=user_type
            )

            # Create realtor profile if applicable
            if user_type == 'realtor':
                try:
                    Realtor.objects.create(
                        user=user,
                        name=name,
                        phone=phone,
                        email=email,
                        license_number=license_number,
                        description='',  # Set a default empty description
                    )
                except Exception as e:
                    logger.error(f"Error creating realtor profile: {str(e)}")
                    user.delete()  # Rollback user creation
                    raise

            # Log user in
            login(request, user)
            
            return JsonResponse({
                'success': True,
                'redirect_url': reverse('auth:dashboard')
            })

        except Exception as e:
            logger.error(f"Error creating user: {str(e)}")
            return JsonResponse({
                'success': False,
                'message': 'An error occurred while creating your account. Please try again.'
            }, status=400)

    except Exception as e:
        logger.error(f"Unexpected error in registration: {str(e)}")
        return JsonResponse({
            'success': False,
            'message': 'An unexpected error occurred.'
        }, status=400)

@login_required
def dashboard(request):
    user = request.user
    
    # Get user's properties
    user_properties = Property.objects.filter(owner=user)
    
    # Get favorite properties with all related property data
    favorite_properties = Favorite.objects.select_related('property').filter(
        user=user
    ).order_by('-created_at')
    
    context = {
        'user': user,
        'total_properties': user_properties.count(),
        'property_types': user_properties.values('property_type')
                         .annotate(count=Count('property_type')),
        'favorite_properties': favorite_properties[:5],
    }
    
    return render(request, 'pages/dashboard.html', context)

def logout_view(request):
    logout(request)
    messages.success(request, 'You have been successfully logged out.')
    return redirect('main:home')
