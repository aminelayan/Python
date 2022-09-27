from django.urls import path 
from . import views

urlpatterns = [
    path('', views.root),
    path('add_books',views.add_books),
    path('authors',views.authors),
    path('add_author',views.add_author),
    path('books/<int:bookid>',views.show_book),
    path('authors/<int:authorid>',views.show_author),
    path('add_to_author',views.add_author_to_book),
    path('add_to_book',views.add_book_author)
]
