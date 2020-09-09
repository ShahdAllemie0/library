from django.contrib import admin
from .models import  Book,Membership,Library
# Register your models here.


admin.site.register(Membership)
admin.site.register(Book)
admin.site.register(Library)
