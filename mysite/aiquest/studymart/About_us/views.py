from django.shortcuts import render
from django.http import HttpResponse

from About_us.models import Teachers

# Create your views here.
def about_us(request):
    return render(request, 'about/about.html')

def teachers_info(request):
    teach = Teachers.objects.all()
    return render(request, 'about/t.html', {'thr': teach}) 
