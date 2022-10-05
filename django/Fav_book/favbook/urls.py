from importlib.resources import path
from django.urls import path
from . import views

urlpatterns = [
    path('', views.root),
    path('registration', views.registration),
    path('login', views.login),
    path('books', views.books),
    path('logout',views.logout),
    path('add',views.add_book),
    path('books/logout',views.logout),
    path('addfav/<int:id>',views.addfav),
    path('books/<int:id>',views.favbooks),
    path('update/<int:id>',views.update),
    path('unfav/<int:id>',views.unfav),
    path('addfav2/<int:id>',views.addfav2),
]