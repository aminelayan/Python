from django.db import models

# Create your models here.
class Book(models.Model): 
    title = models.CharField(max_length=255)
    description = models.TextField(null=True)   
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



class Author(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    books = models.ManyToManyField(Book, related_name="authors")
    notes = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

def select_author(bookid,authorid):
    this_book=Book.objects.get(id=bookid)
    this_author=Author.objects.get(id=authorid)
    this_book.authors.add(this_author)

def select_book(authorid,bookid):
    this_book=Book.objects.get(id=bookid)
    this_author=Author.objects.get(id=authorid)
    this_author.books.add(this_book)

    