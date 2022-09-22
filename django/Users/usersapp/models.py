from django.db import models


class User(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email=models.EmailField(max_length=254)
    age= models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# def list_of_all_users():s
#     return User.objects.all()

# def create_user(info):
#     #info = request.POST
#     User.objects.create(first_name=info['first_name'], last_name=info['last_name'], email=info['email'],age=info['age'])

# User.objects.create(first_name='Sura', last_name='Qalawla', email='sura.qalawla@gmail.com',age='26')
