from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_blogs, name='blogs'),
    path('<slug:slug>', views.blog_detail, name='blog_detail'),
]
