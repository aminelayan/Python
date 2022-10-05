from django.db import models
import re
# User model
class UserManger(models.Manager):
    

    def basic_validator(self,postData):
        errors={}
        if len(postData['first_name'])<2:
            errors['first_name']="First Name Should Be At Least 2 Characters, Try Again !"
        if len(postData['last_name'])<2:
            errors['last_name']="Last Name Should Be At Least 2 Characters, Try Again !"
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not  EMAIL_REGEX.match(postData['email']):
            errors['email']="Email Is Invalid , Try Again !"
        if len(postData['password'])<8:
            errors['password']="Passwod Should Be At Least 8 Charaters, Try Again!"
        if postData['password'] != postData['confirm']:
            errors['confirm']="Passwrod and Confirm Password Does Not Match"
        return errors


class User(models.Model):
    first_name=models.CharField(max_length=255)
    last_name=models.CharField(max_length=255)
    email=models.CharField(max_length=255)
    password=models.CharField(max_length=255)
    create_at=models.DateField(auto_now_add=True)
    update_at=models.DateField(auto_now=True)
    objects=UserManger()


# Book model

class BookManager(models.Manager):
    def add_book_validator(self,postData):
        errors={}
        if postData['title']== "":
            errors['title']="Please Enter a Title For The Book"
        if len(postData['desc'])<5:
            errors['desc']="Please Enter a Valid Description Of The Book"
        return errors


class Book(models.Model):
    title=models.CharField(max_length=255,null=False)
    desc=models.TextField(null=False)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateField(auto_now=True)
    uploaded_by=models.ForeignKey(User, related_name="uploaded_books",on_delete=models.CASCADE)
    users_who_like =models.ManyToManyField(User, related_name="liked_books")
    objects=BookManager()

