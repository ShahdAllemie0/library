from django.shortcuts import render, redirect
from .models import  Book,Membership,Library
from .forms import BookForm, SignupForm, SigninForm
from django.contrib.auth import login, authenticate, logout
from django.db.models import Q
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.core.mail import send_mail
from django.http import HttpResponse


# Create your views here.

     # """""""""""librarian actions"""""""""""

# 1-create membership
def create_membership(request):
    if not request.user.is_staff:
        return redirect("noaccess")
    form = SignupForm()
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(user.password)
            user.save()
            send_mail(
                 'Shahd Library',
                 'You just addedd as membership in our library',
                   'from@shahdlibrary.com',
                   [user.email],
                   fail_silently=False,
)
            return redirect("Book-list")
    context = {
        "form":form,
    }
    return render(request, 'create_membership.html', context)


  # """"""""Books functions""""""""

  # 1- Book's list
def Book_list(request):
    if  request.user.is_staff:
        books = Book.objects.all()
        query = request.GET.get('q')
        if query:
            books = books.filter(
                 Q(bookName__icontains=query)|
                 Q(ISBN__icontains=query)|
                 Q(genre__icontains=query)
                     ).distinct()
        context = {
                "books":books,}
    # elif request.user.is_authenticated:
    #     books = Book.objects.filter(id=request.user)
    #     if  request.user.is_staff:
    #         books = Book.objects.all()
    #         query = request.GET.get('q')
    #
    #     context = {"books":books,}
    else:
        books = Book.objects.filter(borrow=False)
        query = request.GET.get('q')
        if query:
            books = books.filter(
                     Q(bookName__icontains=query)|
                     Q(ISBN__icontains=query)|
                     Q(genre__icontains=query)
                         ).distinct()
        context = {
                    "books":books,}


    return render(request, 'book_list.html', context)
    # context = {
    #          "books":books
    #         }
    #
    # books = Book.objects.all()
    # members= Membership.objects.get(member=request.user)
    # borrows = Borrow.objects.filter(borrowed_by=members).filter(book=books)
    # context ={
    #     	"books": books,
    #         "borrows":borrows}

        # books = Book.objects.all()
        # query = request.GET.get('q')
        # if query:
        #     books = books.filter(
        #              Q(bookName__icontains=query)|
        #              Q(ISBN__icontains=query)|
        #              Q(genre__icontains=query)
        #                  ).distinct()
        #
        # context = {
        #          "books":books
        #         }


 # 2- add books to the list
def Add_Book(request):
    form = BookForm()
    if not request.user.is_staff:
        return redirect("noaccess")
    elif request.method == "POST":
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("Book-list")
    context = {
        "form":form,
    }
    return render(request, 'add_book.html', context)


 #3- update the book
def Update_Book(request, book_id):
    book_obj = Book.objects.get(id=book_id)
    if not request.user.is_staff:
        return redirect("noaccess")
    form = BookForm(instance=book_obj)
    if request.method == "POST":
        form = BookForm(request.POST,request.FILES,  instance=book_obj)
        if form.is_valid():
            form.save()
            return redirect("Book-list")
    context = {
        "book_obj": book_obj,
        "form":form,
    }
    return render(request, 'update_book.html', context)


 #4-  book's detail
def Book_detail(request, book_id):

    books = Book.objects.get(id=book_id)
    library = Library.objects.filter(books=books)
    context = {
        "books": books,

    }
    return render(request, 'book-detail.html', context)


    #5- borrow book
def borrow_Book(request, book_id):
    book_obj=Book.objects.filter(id=book_id).update(borrow=True)
    return redirect("book-detail",book_id)



    #5- Unborrow book
def unborrow_Book(request, book_id):
    book_obj=Book.objects.filter(id=book_id).update(borrow=False)
    return redirect("book-detail",book_id)


    # 6- delete book
def delete_Book(request, book_id):
    book_obj=Book.objects.filter(id=book_id)
    if not (request.user.is_staff):
        return redirect("noaccess")
    book_obj.delete()
    return redirect("Book-list")



    # """"""""Auth""""""""

 # 1-Signup
def signup(request):
    form = SignupForm()
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)

            user.set_password(user.password)
            user.save()

            login(request, user)
            return redirect("Book-list")
    context = {
        "form":form,
    }
    return render(request, 'signup.html', context)

#2-Signin
def signin(request):
    form = SigninForm()
    if request.method == 'POST':
        form = SigninForm(request.POST)
        if form.is_valid():

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            auth_user = authenticate(username=username, password=password)
            if auth_user is not None:
                login(request, auth_user)
                return redirect('Book-list')
    context = {
        "form":form
    }
    return render(request, 'signin.html', context)

#3-Signout
def signout(request):
    logout(request)
    return redirect("signin")



# """""NOTE: No access page  """""
def Noaccess(request):
    return render(request, 'noaccess.html')




    # """"""email""""""
def sendmail(request):

    send_mail(
        'Librart',
        'You just added as membership',
        'shahdallemie@gmail.com',
        [request.email],
        fail_silently=False,
    )

    return HttpResponse('Mail successfully sent')
