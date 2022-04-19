from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from user.models import Location
from user.serializers import LocationSerializer


class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer


from django.shortcuts import render

# Create your views here.
