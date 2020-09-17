from django.shortcuts import render
from rest_framework import generics
from adashi.models import *
from .serializers import *

# Create your views here.

class JoinList(generics.ListCreateAPIView):
    queryset = Join.objects.all()
    serializer_class = JoinSerializer


class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class JoinDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Join.objects.all()
    serializer_class = JoinSerializer

# @api_view(['GET', 'POST'])
# def join_list(request):
#     """
#     List all joins, or create a new join.
#     """
#     if request.method == 'GET':
#         joins = Join.objects.all()
#         serializer = JoinSerializer(joins, many=True)
#         return JsonResponse(serializer.data, safe=False)

#     elif request.method == 'POST':
#         data = JSONParser().parse(request)
#         serializer = JoinSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer.errors, status=400)