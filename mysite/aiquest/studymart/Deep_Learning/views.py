from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def deep_learning(request):
    return HttpResponse('<p>Deep Learning App</p>');