

from django.shortcuts import render ,redirect
from logapp.models import User
import bcrypt

def root (request):
    return render(request,'login.html')


def registration (request):
    errors=User.objects.basic_validator(request.POST)
    print("asdasdas")

    if len(errors)>0:
        for key, value in errors.items():
            messages.error(request,value)
            return redirect('/')
    else:
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        email=request.POST['email']
        password=request.POST['password']
        pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode() 
        new_user=User.objects.create(first_name=first_name,last_name=last_name,email=email,password=pw_hash)
        request.session['first_name'] = new_user.first_name
        request.session['last_name'] = new_user.last_name
        request.session['id'] = new_user.id
        return redirect('/')

def login(request):
    logged_user = User.objects.filter(email=request.POST['email'])
    if logged_user:
        logged_user=logged_user[0]
    print(logged_user)
    if bcrypt.checkpw(request.POST['password'].encode(), logged_user.password.encode()):
        request.session['first_name']=logged_user.first_name
        request.session['id']=logged_user.id
        request.session['last_name']=logged_user.last_name
        return redirect('/wall')
    redirect('/')

def logout(request):
    request.session.delete()
    return redirect('/')

