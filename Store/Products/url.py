from rest_framework import routers
from .viewsets import ProductViewSet,CategoryViewSet

router = routers.SimpleRouter()
router.register('products',ProductViewSet,basename='Products')
router.register('category',CategoryViewSet,basename='Category')

urlpatterns= router.urls