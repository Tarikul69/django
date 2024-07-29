from . import views
from django.urls import path


urlpatterns = [
    path('', views.machine_learning),
    path('random_forest/', views.random_forest),
    path('knn/', views.knn),
    path('dt/', views.dt),
   
]