from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def machine_learning(request):
    return render(request, 'machine_learning/machine_learning.html')

def random_forest(request):
  return render(request,'machine_learning/randomforest.html')

def knn(request):
  return render(request,'machine_learning/knn.html')

def dt(request):
  return render(request,'machine_learning/dt.html')