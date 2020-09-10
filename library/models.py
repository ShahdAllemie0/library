from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Book(models.Model):
   bookName=models.CharField(max_length=120)
   author=models.CharField(max_length=120)
   year=models.IntegerField()
   ISBN=models.CharField(max_length=20)
   genre=models.CharField(max_length=50)
   image = models.ImageField(null=True,blank=True)
   borrow=models.BooleanField(default=False)




class Membership(models.Model):
      member = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
      book = models.ManyToManyField(Book)




class Library(models.Model):
       librarian = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
       books = models.ManyToManyField(Book)
       membership = models.ManyToManyField(Membership)

# class Borrow(models.Model):
#     borrowed_from_date = models.DateField()
#     borrowed_to_date = models.DateField()
#     actual_return_date = models.DateField()
#     borrowed_by = models.ForeignKey(Membership,null=True,blank=True ,on_delete=models.CASCADE)
#     book = models.ForeignKey(Book,null=True,blank=True ,on_delete=models.SET_NULL)

    #
    # def __str__(self):
    #     return self.id
