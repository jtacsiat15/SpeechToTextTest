from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Speech

def index(request):
    #template = loader.get_template('speech/index.html')
    #return HttpResponse("Hello, world. You're at the speech index.")
    return render(request, 'index.html')