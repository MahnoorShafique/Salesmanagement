from django.urls import path, include
from rest_framework.routers import SimpleRouter

from user.views import LocationViewSet



router = SimpleRouter()
router.register('loc', LocationViewSet, basename='loc')



urlpatterns = [

path('',include(router.urls))
]