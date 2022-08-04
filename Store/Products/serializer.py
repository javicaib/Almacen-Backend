from rest_framework import serializers
from .models import Product,Category


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        exclude = ('state',)
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        exclude = ('state',)        