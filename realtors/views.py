from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.core.mail import send_mail
from .models import Contact
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.conf import settings
from main.models import Property
from realtors.models import Realtor
from django.db.models import Count

@login_required
def contact_agent(request):
    if request.method == 'POST':
        try:
            # Get form data
            property_id = request.POST.get('property_id')
            name = request.POST.get('name')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            message = request.POST.get('message')
            
            # Check if user has already contacted about this property
            existing_contact = Contact.objects.filter(
                property_id=property_id,
                user=request.user
            ).exists()
            
            if existing_contact:
                return JsonResponse({
                    'success': False,
                    'message': 'You have already contacted an agent about this property.'
                })
            
            # Create new contact
            contact = Contact.objects.create(
                property_id=property_id,
                user=request.user,
                name=name,
                email=email,
                phone=phone,
                message=message
            )
            
            # Send email notification
            try:
                property = contact.property
                send_mail(
                    subject=f'New Property Inquiry - {property.address}',
                    message=f'''
                    New inquiry from {name}
                    
                    Property: {property.address}
                    Email: {email}
                    Phone: {phone}
                    Message: {message}
                    ''',
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=[settings.ADMIN_EMAIL],
                    fail_silently=True,
                )
            except Exception as e:
                print(f"Error sending email: {str(e)}")
            
            return JsonResponse({
                'success': True,
                'message': 'Your message has been sent successfully!'
            })
            
        except Exception as e:
            return JsonResponse({
                'success': False,
                'message': 'An error occurred while sending your message.'
            })
            
    return JsonResponse({
        'success': False,
        'message': 'Invalid request method.'
    })

def realtor_profile(request, realtor_id):
    realtor = get_object_or_404(Realtor, id=realtor_id)
    
    # Get active listings for this realtor
    active_listings = Property.objects.filter(
        realtor=realtor, 
        is_active=True
    ).order_by('-created_at')
    
    # Get statistics
    total_listings = Property.objects.filter(realtor=realtor).count()
    sold_listings = Property.objects.filter(
        realtor=realtor, 
        status='sold'
    ).count()
    
    # Get listing types distribution
    listing_types = Property.objects.filter(realtor=realtor).values(
        'property_type'
    ).annotate(
        count=Count('property_type')
    )
    
    context = {
        'realtor': realtor,
        'active_listings': active_listings,
        'total_listings': total_listings,
        'sold_listings': sold_listings,
        'listing_types': listing_types,
    }
    
    return render(request, 'pages/realtor_profile.html', context)