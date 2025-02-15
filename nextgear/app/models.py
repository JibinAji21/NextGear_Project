from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Product_category(models.Model):
    name = models.TextField()
    image = models.FileField()

    def __str__(self):
        return self.name
    

class Product(models.Model):
    product_id=models.TextField()
    product_name=models.TextField()
    price=models.IntegerField()
    offer_price=models.IntegerField()
    img=models.FileField()
    dis=models.TextField()
    category=models.ForeignKey(Product_category,on_delete=models.CASCADE,related_name="products")