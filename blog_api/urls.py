from django.urls import path
from .views import ApiListView,BlogDetail

urlpatterns = [
    path('',ApiListView.as_view(),name='blog_list'),
    path('<int:pk>/',BlogDetail.as_view(),name='detail'),

]