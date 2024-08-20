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
    from django.core.files.base import ContentFile
    title = models.CharField(max_length=200, null=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(null=True, blank=True)

    address = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if self.image:
            img = Image.open(self.image)
            img.thumbnail((800, 800))  # Resize image
            output = io.BytesIO()
            img.save(output, format='JPEG', quality=85)
            output.seek(0)
            self.image = ContentFile(output.read(), name=self.image.name)
        super().save(*args, **kwargs)

