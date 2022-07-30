from rest_framework import routers
from .viewsets import ProductViewSet

router = routers.SimpleRouter()
router.register('products',ProductViewSet,basename='Products')
urlpatterns= router.urls