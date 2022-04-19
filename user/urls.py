from django.urls import path, include
from rest_framework.routers import SimpleRouter

from user.views import LocationViewSet, EmployeeViewSet, JobViewSet, ManagerViewSet

router = SimpleRouter()
router.register('loc', LocationViewSet, basename='loc')
router.register('emp', EmployeeViewSet, basename='em')
router.register('job', JobViewSet, basename='job')
router.register('manager', ManagerViewSet, basename='job')



urlpatterns = [

path('',include(router.urls))
]