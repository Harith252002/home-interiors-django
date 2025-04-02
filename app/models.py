from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class HomeInteriors(models.Model):
    category_name=models.CharField(max_length=40)
    desc=models.CharField(max_length=100)
    pic=models.ImageField(upload_to='categories/1')
    def __str__(self):
        return self.category_name
class User(User):
    phone = models.CharField(max_length=10)
    
    def __str__(self):
        return self.username
class Business(models.Model):
    category_name=models.CharField(max_length=40)
    desc=models.CharField(max_length=100)
    pic=models.ImageField(upload_to='categories/2')
    def __str__(self):
        return self.category_name
from django.db import models

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
