import string
from django.db import models

# Create your models here.
class destination:
    id : int
    name : str
    img : str
    desc : str
    price : int 
    
# we are gonna create an object of the above class in views.py 