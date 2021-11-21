from rest_framework import serializers
from .models import BlogApi

class BlogSerializer(serializers.ModelSerializer):

    class Meta:
        model = BlogApi
        fields = ('id','title','auther','body','created_at','updated_at')