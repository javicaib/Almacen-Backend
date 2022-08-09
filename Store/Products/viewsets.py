from itertools import product
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from .models import Category, Product
from .serializer import ProductSerializer, CategorySerializer
from django.shortcuts import get_object_or_404


class ProductViewSet(viewsets.ModelViewSet):

    #queryset = Product.objects.filter(state=True)
    serializer_class = ProductSerializer

    def get_queryset(self, pk=None):
        if pk is None:
            return Product.objects.filter(state=True)
        return Product.objects.filter(id=pk, state=True).first()

    def list(self, request):
        product_serializer = self.get_serializer(
            self.get_queryset(), many=True)
        return Response(product_serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Producto añadido correctamente'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):

        if pk == 'by-category':
            return Response({'error': 'Debe indicar un id valido'}, status=status.HTTP_400_BAD_REQUEST)
        
        product = self.get_queryset(pk)
        
        if product:
            serializer = self.serializer_class(product)

            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'No se encuentra el producto'}, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        if self.get_queryset(pk):
            serializer = self.serializer_class(
                self.get_queryset(pk), data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, resquest, pk=None):
        product = self.get_queryset().filter(id=pk).first()
        if product:
            product.state = False
            product.save()
            return Response({'message': 'Producto eliminado correctamente'}, status=status.HTTP_200_OK)
        return Response({'error': 'No se encuentra el producto'}, status=status.HTTP_400_BAD_REQUEST)

    def product_by_category(self, request, pk=None):
        queryset = Product.objects.filter(category=pk)
        serializer = self.get_serializer(queryset, many=True)
        if len(serializer.data) == 0:
            return Response({'error': 'No hay productos en con el id de la categoria proporcionada'}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CategoryViewSet(viewsets.ModelViewSet):

    serializer_class = CategorySerializer
    def get_queryset(self, pk=None):
        if pk is None:
            return Category.objects.filter(state=True)
        return Category.objects.filter(id=pk, state=True).first()