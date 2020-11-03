from django.shortcuts import render
from rest_framework import generics
from adashi.models import *
from .serializers import *

# Create your views here.
class PositionList(generics.ListCreateAPIView):
    queryset = Position.objects.all()
    serializer_class = PositionSerializer

class PositionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Position.objects.all()
    serializer_class = PositionSerializer

class JoinList(generics.ListCreateAPIView):
    queryset = Join.objects.all()
    serializer_class = JoinSerializer

class JoinDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Join.objects.all()
    serializer_class = JoinSerializer
