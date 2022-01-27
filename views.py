from django.shortcuts import render

from .serializers import NiftySerializer
from rest_framework import viewsets      
from .models import NiftyModel

# Create your views here.
class NiftyView(viewsets.ModelViewSet):  
    serializer_class = NiftySerializer   
    queryset = NiftyModel.objects.all() 
