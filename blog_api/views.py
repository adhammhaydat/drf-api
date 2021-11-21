from django.db.models.query import QuerySet
from django.shortcuts import render
from .models import Blog_Api
from .serializer import Blog_Serializer
from rest_framework.generics import ListCreateAPIView , RetrieveUpdateDestroyAPIView
# Create your views here.

class ApiListView(ListCreateAPIView):
    queryset = Blog_Api.objects.all()
    serializer_class = Blog_Serializer


class BlogDetail(RetrieveUpdateDestroyAPIView):
    queryset= Blog_Api.objects.all()
        
