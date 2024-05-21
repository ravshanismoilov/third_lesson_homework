from django.contrib import admin
from .models import Category, Author, Language, Book


admin.site.register(Category)
admin.site.register(Author)
admin.site.register(Language)
admin.site.register(Book)
