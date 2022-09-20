from django.urls import path 
from . import views

urlpatterns = [
    path('', views.root),
    path('blogs',views.index),
    path('blogs/news',views.new),
    path('blogs/create',views.create),
    path('blogs/<int:number>',views.show),
    path('blogs/<int:number>/edit',views.edit),
    path('blogs/<int:number>/delete',views.delete),
    path('blogs/json',views.ajson)
    ]
    
