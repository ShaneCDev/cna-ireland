from django.urls import path
from . import views

urlpatterns = [
    path('', views.why_us, name='why_us'),
]
