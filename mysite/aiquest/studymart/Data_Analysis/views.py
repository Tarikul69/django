from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def data_analist(request):
    return render(request, 'data_analysis.html')
