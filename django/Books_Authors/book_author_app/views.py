
from django.shortcuts import render , redirect
from .models import Book,Author
from book_author_app import models

def root(request):
    context={
        'all_book' : Book.objects.all()
    }
    return render(request,'index.html',context)

def add_books(request):
    title=request.POST['title']
    description=request.POST['description']
    Book.objects.create(title=title,description=description)
    return redirect('/')

def authors(request):
    context={
        'authors' : Author.objects.all()
    }
    return render(request,'add_author.html',context)

def add_author(request):
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    notes= request.POST['notes']
    Author.objects.create(first_name=first_name,last_name=last_name,notes=notes)
    return redirect('/authors')



def show_book(request,bookid):
    selected_book=Book.objects.get(id=bookid)
    context={
        'this_book':Book.objects.get(id=bookid),
        'all_author' : Author.objects.all(),
        'all_authors_except':Author.objects.exclude(id__in=selected_book.authors.all())
    }
    return render(request,'books.html',context)


def show_author(request,authorid):
    selected_author = Author.objects.get(id=authorid) 
    context={
        'this_author' :Author.objects.get(id=authorid) ,
        'all_books': Book.objects.all(),
        'all_books_except': Book.objects.exclude(id__in=selected_author.books.all())
    }
    return render(request,'authors.html',context)

def add_book_author(request,):
    book=request.POST['booksid']
    author=request.POST['authors']
    models.select_author(book,author)
    return redirect('books/'+str(book))

def add_author_to_book(request):
    book=request.POST['books']
    author=request.POST['authorsid']
    models.select_book(author,book)
    return redirect('authors/'+str(author))

    