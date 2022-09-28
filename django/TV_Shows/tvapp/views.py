
from django.shortcuts import render , redirect
from .models import Show
from django.contrib import messages


def root(request):
    return redirect('/shows')

def index(request):
    context={
        'all_shows' : Show.objects.all()
    }
    return render(request,'shows.html',context)

def new_show(request):
    return render(request,'add_show.html')

def add_show(request):
    errors=Show.objects.basic_validator(request.POST)
    if len(errors)>0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/shows/new')
    else:
        title=request.POST['title']
        network=request.POST['network']
        release_date=request.POST['release_date']
        description=request.POST['description']
        this_show=Show.objects.create(title=title,network=network,release_date=release_date,description=description)
        return redirect('/shows/'+str(this_show.id))

def show(request,showid):
    context={
        'this_show':Show.objects.get(id=showid)
    }
    return render(request,'my_show.html',context)

def edit_show(request,showid):
    context={
        'this_show' : Show.objects.get(id=showid)
    }
    return render(request,'edit.html',context)

def update_show(request):
    my_show_id=request.POST['show_id']
    errors=Show.objects.basic_validator(request.POST)
    if len(errors)>0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/shows/'+str(my_show_id)+'/edit')
    else:
        show_to_update=Show.objects.get(id=my_show_id)
        show_to_update.title=request.POST['title']
        show_to_update.network=request.POST['network']
        show_to_update.release_date=request.POST['release_date']
        show_to_update.description=request.POST['description']
        show_to_update.save()
        return redirect('/shows/'+str(my_show_id))

def delete_show(request,showid):
    D_show=Show.objects.get(id=showid)
    D_show.delete()
    return redirect('/shows')