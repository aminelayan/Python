from django.db import models
import re
import bcrypt


class UserManger(models.Manager):
    def registration_validator(self, postData):
        errors = {}
        if len(postData['first_name']) < 2:
            errors["first_name"] = "User first name should be at least 2 characters"
        if len(postData['last_name']) < 2:
            errors["last_name"] = "User last name should be at least 2 characters"
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = "Invalid email address!"
        if len(postData['password']) < 8:
            errors["password"] = "User password should be at least 8 characters"
        if postData['password'] != postData['confirm']:
            errors["confirm"] = "Password and confirmation Password don't match"
        return errors

    def login_validator(self, postData):
        email = User.objects.filter(email=postData['email'])
        errors = {}
        if not len(check_e):
            errors['email'] = "email doesn't exist"
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = "Invalid email address or Password !"
        if len(postData['password']) < 8:
            errors["password"] = "User password should be at least 8 characters"
        if len(email) and not bcrypt.checkpw(postData['password'].encode(), email[0].password.encode()):
            errors["password"] = "Wrong Password!"
        return errors


class User(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    objects = UserManger()
