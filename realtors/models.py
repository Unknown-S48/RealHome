from django.db import models
from datetime import datetime
from django.conf import settings

class Realtor(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='realtor_profile', blank=True, null=True)
    name = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    description = models.TextField(blank=True)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    license_number = models.CharField(max_length=50, blank=True, null=True)
    is_mvp = models.BooleanField(default=False)
    hire_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.name
    
    @property
    def active_listings_count(self):
        return self.properties.filter(is_active=True).count() if hasattr(self, 'properties') else 0

class Contact(models.Model):
    property = models.ForeignKey('main.Property', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    message = models.TextField(blank=True)
    contact_date = models.DateTimeField(default=datetime.now, blank=True)
    user = models.ForeignKey('user.CustomUser', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name

