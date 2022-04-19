
from django.urls import path,include
from rest_framework.routers import SimpleRouter

from product.views import ProductViewSet, CategoryViewSet

from product.views import ProductViewSet, CategoryViewSet, SupplierViewSet

router = SimpleRouter()
router.register('productviewset', ProductViewSet, basename='product')
router.register('categoryviewset', CategoryViewSet, basename='category')
router.register('supplierviewset', SupplierViewSet, basename='sup')


urlpatterns = [

path('',include(router.urls))
]