from django.shortcuts import render
from .models import *
from django.http import HttpResponse
# Create your views here.
def sia(request):
    post=rara.objects.all()
    return render (request,'puta rara.html',{'post':post})
def am(request):
    if request.method == 'POST':
        Actor=request.POST['Actor']
        Director=request.POST['Director']
        k=rara(Actor=Actor,Director=Director)
        k.save()
    return render(request,'unstopbable.html')