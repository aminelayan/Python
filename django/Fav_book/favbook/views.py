from multiprocessing import context
from django.shortcuts import render ,redirect
import bcrypt
from favbook.models import *
from django.contrib import messages



def root (request):
    return render(request,'login.html')


def registration (request):
    errors=User.objects.basic_validator(request.POST)

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
    logged_user= User.objects.filter(email=request.POST['email'])
    if logged_user:
        logged_user=logged_user[0]
    print(logged_user)
    if bcrypt.checkpw(request.POST['password'].encode(), logged_user.password.encode()):
        request.session['first_name']=logged_user.first_name
        request.session['id']=logged_user.id
        request.session['last_name']=logged_user.last_name
        return redirect('/books')
    redirect('/')

def logout(request):
    request.session.delete()
    return redirect('/')

def books(request):
        context={
            'allbooks':Book.objects.all(),
            'user':User.objects.get(id=request.session['id'])

        }   
        return render(request,'book.html',context)

def add_book(request):
    errors = Book.objects.add_book_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/books')

    uploader= User.objects.get(id=request.session['id'])
    b_title=request.POST['title']
    b_desc=request.POST['desc']
    Book.objects.create(title=b_title,desc=b_desc,uploaded_by=uploader)
    
    last=Book.objects.last()
    last.users_who_like.add(uploader)

    return redirect('/books')

def addfav(request,id):
    book=Book.objects.get(id=id)
    user=User.objects.get(id=request.session['id'])
    print(book)
    print(user)
    book.users_who_like.add(user)
    return redirect('/books')

def favbooks(request,id):
    user=User.objects.get(id=request.session['id'])
    book=Book.objects.get(id=id)
    context = {
        'book':book,
        'likebook':book.users_who_like.all(),
        'user':user
    }
    return render(request,'book_id.html',context)

def update(request,id):
    if request.POST['up'] == 'Update':
        book=Book.objects.get(id=id)
        book.title=request.POST['title']
        book.desc=request.POST['desc']
        book.save()
        messages.success(request,"Update Complete !")
        return redirect(f'/books/{id}')

    elif request.POST['up'] == 'Delete':
        book=Book.objects.get(id=id)
        book.delete()
        return redirect('/books')

def unfav(request,id):
    book=Book.objects.get(id=id)
    user=User.objects.get(id=request.session['id'])
    print(book)
    print(user)
    book.users_who_like.remove(user)
    return redirect(f'/books/{id}')

def addfav2(request,id):
    book=Book.objects.get(id=id)
    user=User.objects.get(id=request.session['id'])
    book.users_who_like.add(user)
    return redirect(f'/books/{id}')
