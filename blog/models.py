from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
# Create your models here.

class Articles(models.Model):
    title=models.CharField(max_length=100)
    content=models.TextField()
    date_posted=models.DateField(default=timezone.now)
    author=models.ForeignKey(User,on_delete=models.CASCADE,db_constraint=False)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('blog.detail',kwargs={'pk':self.pk})
    

