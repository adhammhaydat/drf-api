from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

class Blog_Api(models.Model):
    title = models.CharField(max_length=250)
    auther= models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now=True)


    def __init__(self):
        return self.title