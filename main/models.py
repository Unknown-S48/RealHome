from django.db import models
from django.contrib.auth.models import User
from PIL import Image
import io
from django.core.files.base import ContentFile


# Create your models here.

class User(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name


class Property(models.Model):
    address = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=2, blank=True, null=True)
    zip_code = models.CharField(max_length=10, blank=True, null=True)
    price = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    bedrooms = models.IntegerField(blank=True, null=True)
    bathrooms = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)
    square_meters = models.IntegerField(blank=True, null=True)
    property_type = models.CharField(max_length=50, blank=True, null=True)
    year_built = models.IntegerField(blank=True, null=True)
    lot_size = models.CharField(max_length=50, blank=True, null=True)
    image = models.ImageField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.image:
            img = Image.open(self.image)
            img.thumbnail((800, 800))  # Resize image
            output = io.BytesIO()
            img.save(output, format='JPEG', quality=85)
            output.seek(0)
            self.image = ContentFile(output.read(), name=self.image.name)
        super().save(*args, **kwargs)

    