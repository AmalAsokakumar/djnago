from django.db import models

# Create your models here.

class destination(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    desc = models.TextField()
    price = models.IntegerField()
    offers = models.BooleanField(default=False)
    
    
# import string
# from django.db import models

# # Create your models here.
# class destination:
#     id : int
#     name : str
#     img : str
#     desc : str
#     price : int 
    
# we are gonna create an object of the above class in views.py 


