from rest_framework import routers
from .viewsets import ProductViewSet,CategoryViewSet
from django.urls import path
router = routers.SimpleRouter()
router.register('products',ProductViewSet,basename='Products')
router.register('category',CategoryViewSet,basename='Category')

urlpatterns= router.urls
urlpatterns += [
    path('products/by-category/<int:pk>/', ProductViewSet.as_view({"get": "product_by_category"}))
]