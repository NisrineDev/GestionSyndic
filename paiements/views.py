from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Versement
from .serializers import VersementSerializer

class VersementsView(viewsets.ModelViewSet):
    queryset = Versement.objects.all()
    serializer_class = VersementSerializer