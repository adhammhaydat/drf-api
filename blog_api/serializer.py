from rest_framework import serializers
from .models import Blog_Api

class Blog_serializer(serializers.ModelSerializer):

    class Meta:
        model = Blog_Api
        fields = ('title','auther','body','created_at','updated_at')