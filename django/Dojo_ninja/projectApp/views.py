
from django.shortcuts import render, redirect
from .models import Ninja, Dojo
    
def index(request):
    context = {"dojos": Dojo.objects.all()}		
    return render(request,'index.html',context)

def add_dojo(request):
    name=request.POST['name']
    city=request.POST['city']
    State=request.POST['State']
    Dojo.objects.create(name=name,city=city,State=State)
    return redirect('/')
    

def add_ninja(request):
    first_name=request.POST['first_name']
    last_name=request.POST['last_name']
    dojos=Dojo.objects.get(id=int(request.POST['dojos']))
    Ninja.objects.create(first_name=first_name,last_name=last_name,dojo=dojos)
    print(dojos)
    return redirect('/')