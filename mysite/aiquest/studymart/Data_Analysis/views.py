from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def data_analist(request):
    return HttpResponse('<p>Data Analist App</p>');
