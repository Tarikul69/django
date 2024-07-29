from . import views
from django.urls import path


urlpatterns = [
    path('ml/', views.machine_learning),
   
]