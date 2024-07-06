from django.db import models
from django.contrib.auth.models import User
from PIL import Image
# Create your models here.
class Profiles(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE) 
    img =models.ImageField(default='/meida/default.jpg',upload_to='meida/profile/')
    
    