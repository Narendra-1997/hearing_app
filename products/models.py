from django.db import models

class Product(models.Model):
    name = models.CharField( max_length= 200)
    sku = models.CharField(unique=True,max_length=100)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    quantity_in_stock = models.IntegerField()

    def __str__(self):
        return self.name
    
class Coupon(models.Model):
    code = models.CharField(max_length=50,unique=True)
    valid_from = models.DateTimeField()
    valid_to = models.DateTimeField()
    discount = models.IntegerField(default='%')
    active = models.BooleanField()