from django.urls import path 
from wallapp import views

urlpatterns = [
path('',views.wall),
path('post_message',views.add_message),#adds a new message --> localhost:8000/wall/write
path('post_comment',views.add_comment),#adds a new comment
path('delete_comment',views.delete_this),
]