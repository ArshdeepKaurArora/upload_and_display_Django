from django.db import models

# Create your models here.

class UserProfileModel(models.Model):
    """Create a model for user profile"""
    user_image = models.ImageField(upload_to='images')
