import imghdr
from math import degrees
from django.db import models

# Create your models here.
class Item(models.Model):
    def __str__(self):
        return self.item_name




    item_name = models.CharField(max_length=200)
    item_desc = models.CharField(max_length=200)
    item_price = models.IntegerField(default=0)
    item_image = models.CharField(max_length=500,default="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSEbN6-Gy6xenhzrJmZkQHarZEt40XL_PJu4w&usqp=CAU")


