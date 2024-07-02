from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.template import loader
from .models import Category, Author, Novel


class Index(View):
    def get(self, req):
        categories = Category.objects.all().values()
        template = loader.get_template("index.html")
        context = {"categories": categories}
        return HttpResponse(template.render(context=context, request=req))


class AuthorPage(View):
    def get(self, req):
        authors = Author.objects.all().values()
        template = loader.get_template("author.html")
        context = {"authors": authors}
        return HttpResponse(template.render(context=context, request=req))


class NovelPage(View):
    def get(self, req):
        novels = Novel.objects.all().values()
        template = loader.get_template("novel.html")
        context = {"novels": novels}

        return HttpResponse(template.render(context=context, request=req))
