from rest_framework import viewsets
from .models import Product
from .serializer import ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.filter(state=True)
    serializer_class = ProductSerializer
    