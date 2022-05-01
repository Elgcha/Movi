from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_robot),
    path('start/', views.start),
    path('end/', views.end),
]  