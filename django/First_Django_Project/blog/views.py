from django.shortcuts import render, HttpResponse,redirect
from django.http import JsonResponse

# Create your views here.
def root(request):
    return HttpResponse("@app.route('/')")

def index(request):
    return HttpResponse("placeholder to later display a list of all blogs")

def new(request):
    return HttpResponse("placeholder to display a new form to create a new blogs")


def create(request):
    return redirect('/')


def show(request,number):
    return HttpResponse(f"placeholder to display blog number: {number}",number)


def edit(request,number):
    return HttpResponse(f"placeholder to edit blog:{number}",number)

def delete(request,number):
    return redirect('/blogs')

def ajson(request):
    return JsonResponse({"title":"My first blog","content":"lorem"})