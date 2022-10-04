
from django.db import models
from logapp.models import *

class Message(models.Model):
    user = models.ForeignKey(User, related_name="User_message", on_delete = models.CASCADE)
    message=models.TextField()
    created_at=models.DateField(auto_now_add=True)
    updated_at=models.DateField(auto_now=True)


class Comment(models.Model):
    message= models.ForeignKey(Message, related_name="message_comment", on_delete = models.CASCADE)
    user = models.ForeignKey(User, related_name="user_comment", on_delete = models.CASCADE)
    comment=models.TextField()
    created_at=models.DateField(auto_now_add=True)
    updated_at=models.DateField(auto_now=True)

    