from rest_framework import serializers 
from .models import Product , Coupon

class productserializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
    
class couponserializer(serializers.ModelSerializer):
    class Meta():
        models = Coupon
        feilds = "__all__"

