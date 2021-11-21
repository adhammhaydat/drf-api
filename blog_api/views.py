from django.db.models.query import QuerySet
from django.shortcuts import render
from .models import BlogApi
from .serializer import BlogSerializer
from rest_framework.generics import ListCreateAPIView , RetrieveUpdateDestroyAPIView
# Create your views here.

class ApiListView(ListCreateAPIView):
    queryset = BlogApi.objects.all()
    serializer_class = BlogSerializer


class BlogDetail(RetrieveUpdateDestroyAPIView):
    queryset= BlogApi.objects.all()
    serializer_class = BlogSerializer    
