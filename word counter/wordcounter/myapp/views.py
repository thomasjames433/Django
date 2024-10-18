from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request,'index.html')

def counter(request):
    # text=request.GET['text'] Get method
    text= request.POST['text']
    no=len(text.split())
    return render(request,'counter.html', {'number': no})