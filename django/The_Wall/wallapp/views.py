from django.shortcuts import render,redirect
from .models import Message,Comment,User


def wall(request):
    if 'id' in request.session:
        users_all=User.objects.all()
        comments_all=Comment.objects.all().order_by("created_at")
        message_all=Message.objects.all().order_by("created_at")
        context={
            'users_a':users_all,
            'messages_a':message_all,
            'comments_a':comments_all,
        }
        return render(request,'wall.html',context)
    return redirect('/')

def add_message(request):
    user_id=request.session['id']
    message_user=User.objects.get(id=user_id)
    text=request.POST['post_message']
    Message.objects.create(message = text, user = message_user)
    return redirect ('/wall')

def add_comment(request):
    user_id=request.session['id']
    comment_user=User.objects.get(id=user_id)
    comment_text=request.POST['post_comment']
    this_message=Message.objects.get(id=request.POST['message_id'])
    Comment.objects.create(comment=comment_text ,user= comment_user,message= this_message)
    return redirect('/wall')

def delete_this(request):
    comment_to_delete = request.POST['commentid']
    Comment.objects.get(comment_to_delete)
    comment_to_delete.delete()
    return redirect('/wall')