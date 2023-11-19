from django.urls import path
from . import views


urlpatterns = [
    path('subscribe-to-newsletter', views.subscribe_to_newsletter, name='subscribe_to_newsletter'),
    path('subscription-success', views.success, name='success'),
    path('subscription-error', views.error, name='error'),
]