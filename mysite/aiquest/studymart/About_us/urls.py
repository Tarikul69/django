from django.urls import path
from . import views



urlpatterns = [
    path('', views.about_us),
    path('t/', views.teachers_info),
]