from django.shortcuts import render, redirect

def index(request):
    if 'counter' in request.session:
        request.session['counter']+=1
    else:
        request.session['counter']=0
    
    return render(request,'index.html')

def destroy_session(request):
    if 'counter' in request.session:
        del request.session['counter']
    return redirect('/')


def increase_counter_by_two(request):
    if 'counter' in request.session:
        request.session['counter']+=1
    else:
        request.session['counter']=0
    
    return redirect('/')


def increase_counter_by_fixed_number(request):
    if 'counter' in request.session:
        print(type(request.session['counter'])) #int
        request.session['counter']+=int(request.POST['numbertoadd'])
    else:
        request.session['counter']=0
    
    return redirect('/')