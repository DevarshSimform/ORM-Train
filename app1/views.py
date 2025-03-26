from django.shortcuts import render, redirect, HttpResponse
from .models import *
from django.contrib.auth.models import Permission
from django.contrib.auth import login, logout, authenticate
from .forms import UserRegistrationForm

# Create your views here.
def home(request):
    # user = user.request
    # permission = Permission.objects.get(codename='add_books')
    # user.user_permissions.add(permission)
    # print(request.user.has_perm('app1.add_books'))

    # ------Forward relation query without select_related-------
    # book = Books.objects.get(title='Deep Learning')
    # print(book.author)


    # ------Backward relation query without select_related-------
    # author = Author.objects.get(firstname='Alex')
    # books = author.books.all()
    # for book in books:
    #     print(book.id)

   
    # ------Forward relation query with select_related-------
    # book = Books.objects.select_related('author').get(title='Deep Learning')
    # print(book.author)
    # books = Books.objects.select_related('author').all()
    # for book in books:
    #     print(book)


    # ------Backward relation query with prefetch_related-------
    # author = Author.objects.prefetch_related('books').get(firstname='Alex')
    # books = author.books.all()
    # for book in books:
    #     print(book.id)

    # author_name = Author.objects.filter(books__title='Deep Learning')
    # print(author_name)


    return render(request, 'app1/base.html')


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            login(request, user)
            return redirect('home1')
    else:
        form = UserRegistrationForm()
    return render(request, 'app1/register.html', {'form': form})


def role(request):
    return HttpResponse('<h1> Done </h1>')