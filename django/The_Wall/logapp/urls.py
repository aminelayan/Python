from django.urls import path 
from logapp import views

urlpatterns = [
    path('',views.root),
    path('registration',views.registration),
    path('login',views.login),
    path('logout',views.logout),

]