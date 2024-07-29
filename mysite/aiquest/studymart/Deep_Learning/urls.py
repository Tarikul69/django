from . import views
from django.urls import path


urlpatterns = [
    path('', views.deep_learning),
]