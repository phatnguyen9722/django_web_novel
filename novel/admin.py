from django.contrib import admin
from .models import Author, User, Novel, Chapter, Category

admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Chapter)
admin.site.register(Novel)
admin.site.register(User)
