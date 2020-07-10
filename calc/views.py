from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.
def home(request):
    return render(request,'index.html')
def naam(request):
    k=request.GET['buddy']
    return render(request,'abc.html',{'title':k})
def x(request):
    a=int(request.GET['text1'])
    b=int(request.GET['text2'])
    c=a+b
    return render(request,'out.html',{'result':c})
    
