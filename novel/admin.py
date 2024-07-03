from django.contrib import admin
from .models import Author, User, Novel, Chapter, Category


class NovelAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name"]
    list_filter = ["name"]
    search_fields = ["name"]


class ChapterAdmin(admin.ModelAdmin):
    list_display = ["novel"]
    list_filter = ["novel"]
    search_fields = ["novel"]


admin.site.register(Author)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Chapter, ChapterAdmin)
admin.site.register(Novel, NovelAdmin)
admin.site.register(User)
