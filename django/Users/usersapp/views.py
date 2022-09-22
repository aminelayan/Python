from django.shortcuts import render, redirect
from .models import User

def index(request):
    context={
        "all_users" : User.objects.all()
    }
    return render(request, "index.html", context)

def showusers(request):
    first_name=request.POST['firstname']
    last_name=request.POST['lastname']
    email=request.POST['email']
    age=int(request.POST['age'])
    User.objects.create(first_name=first_name,last_name=last_name,email=email,age=age)

    return redirect('/')