from django.contrib import admin
from bookapp.models  import Book, Author
admin.site.register(Author)
admin.site.register(Book)
# Register your models here.