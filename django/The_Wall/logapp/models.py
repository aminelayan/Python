
from django.db import models
import re

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

