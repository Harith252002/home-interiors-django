from django.db import models
from app.models import *
# Create your models here.
class Cateogries(models.Model):
    name=models.CharField(max_length=20)
    pic=models.ImageField(upload_to='kitchen/1')
    dimensions=models.CharField(max_length=20)
    price=models.IntegerField()
    desc=models.CharField(max_length=450)
    category=models.ForeignKey(HomeInteriors,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
class Business_Cateogries(models.Model):
    name=models.CharField(max_length=20)
    pic=models.ImageField(upload_to='kitchen/1')
    dimensions=models.CharField(max_length=20)
    price=models.IntegerField()
    desc=models.CharField(max_length=450)
    category=models.ForeignKey(Business,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name