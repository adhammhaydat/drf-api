from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
# Create your models here.

class BlogApi(models.Model):
    title = models.CharField(max_length=250)
    auther= models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now=True)


    