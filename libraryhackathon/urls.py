"""libraryhackathon URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from library import views
from django.conf import settings
from django.conf.urls.static import static
# from .views import  sendmail



urlpatterns = [
    path('sendmail', views.sendmail, name='sendmail'),
    path('admin/', admin.site.urls),
    path('',views.Book_list ,name='Book-list'),
    path('create/membership/',views.create_membership ,name='create-membership'),
    path('signup/',views.signup ,name='signup'),
    path('signin/',views.signin ,name='signin'),
    path('signout/',views.signout ,name='signout'),
    path('noaccess/',views.Noaccess ,name='noaccess'),
    path('addbook/',views.Add_Book ,name='add-books'),
    path('updatebook/<int:book_id>/',views.Update_Book ,name='update-book'),
    path('bookdetail/<int:book_id>/',views.Book_detail ,name='book-detail'),
    path('deletebook/<int:book_id>/',views.delete_Book ,name='delete-book'),
    path('borrowbook/<int:book_id>/',views.borrow_Book ,name='borrow-book'),
    path('unborrowbook/<int:book_id>/',views.unborrow_Book ,name='unborrow-book'),





]

urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
