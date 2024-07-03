from django.shortcuts import render, get_object_or_404
from django.views import View
from django.http import HttpResponse
from django.template import loader
from .models import Category, Author, Novel, Chapter


class Index(View):
    """
    This class is used for Home page
    """

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


def chapter_detail(request, novel_slug, chapter_no):
    novel = get_object_or_404(Novel, slug=novel_slug)
    chapter = get_object_or_404(Chapter, novel=novel, chapter_no=chapter_no)
    return render(request, "chapter_detail.html", {"chapter": chapter})
