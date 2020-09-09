from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Book(models.Model):
   bookName=models.CharField(max_length=120)
   author=models.CharField(max_length=120)
   year=models.IntegerField()
   ISBN=models.CharField(max_length=20)
   genre=models.CharField(max_length=50)
   borrow=models.BooleanField(default=False)


class Membership(models.Model):
      user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)


class Library(models.Model):
       librarian = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
       books = models.ManyToManyField(Book)
       membership = models.ManyToManyField(Membership)
