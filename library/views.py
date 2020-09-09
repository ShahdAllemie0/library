from django.shortcuts import render, redirect
from .models import  Book,Library
from .forms import BookForm, SignupForm, SigninForm
from django.contrib.auth import login, authenticate, logout
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
            return redirect("Book-list")
    context = {
        "form":form,
    }
    return render(request, 'create_membership.html', context)


  # """"""""Books functions""""""""

  # 1- Book's list
def Book_list(request):
    if  request.user.is_staff:
        context = {
                 "books":Book.objects.all(),}
    else:
        context = {
                 "books":Book.objects.filter(borrow=False)
               }
    return render(request, 'book_list.html', context)

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
        form = BookForm(request.POST,  instance=book_obj)
        if form.is_valid():
            form.save()
            return redirect("Book-list")
    context = {
        "book_obj": book_obj,
        "form":form,
    }
    return render(request, 'update_book.html', context)



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
