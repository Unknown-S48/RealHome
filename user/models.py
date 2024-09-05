from django.db import models
from django.contrib.auth.models import User
from PIL import Image
import io
from django.core.files.base import ContentFile
# Create your models here.


class UserAccount(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    
    def __str__(self):
        return self.name