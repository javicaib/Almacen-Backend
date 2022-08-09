from rest_framework import serializers
from .models import Product,Category


class ProductSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Product
        exclude = ('state','created_at','update_at')    
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        exclude = ('state','created_at','update_at')       