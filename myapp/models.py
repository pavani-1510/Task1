from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    USER_TYPE_CHOICES = (
        (1, 'Patient'),
        (2, 'Doctor'),
    )
    user_type = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES)

class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    address_line1 = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    pincode = models.CharField(max_length=10)
    profile_picture = models.ImageField(upload_to='profile_pics/')
