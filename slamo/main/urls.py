from django.urls import path
from . import views

urlpatterns = [
    path('', views.main),
    path('send-slam/', views.sendSlam),
]
