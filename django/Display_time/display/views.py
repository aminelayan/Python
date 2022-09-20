from django.shortcuts import render, HttpResponse
from time import gmtime, strftime
    
def root(request):
    return HttpResponse("@app.route")

def index(request):
    context = {
        "time": strftime("%Y-%m-%d-%A \n %H:%M:%S %p %Z", gmtime())
    }
    return render(request,'index.html', context)

