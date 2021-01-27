from django.urls import path
from . import views

urlpatterns = [
    path('', views.detect, name='detect'),
    path('webcam_feed', views.webcam_feed, name='webcam_feed'),
]
