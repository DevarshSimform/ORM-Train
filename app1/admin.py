from django.contrib import admin
from .models import Author, Publisher, Books, User

# Register your models here.
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['firstname', 'lastname', 'address', 'zipcode', 'telephone', 'recommendedby', 'joindate', 'popularity_score']

@admin.register(Books)
class BooksAdmin(admin.ModelAdmin):
    list_display = ['title', 'genre', 'price', 'published_date', 'author', 'publisher']

@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    list_display = ['firstname', 'lastname', 'recommendedby', 'joindate', 'popularity_score']

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email']
