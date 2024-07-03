from django.urls import path
from .views import *

urlpatterns = [
    path("", Index.as_view(), name="index"),
    path("home/", Index.as_view(), name="index"),
    path("novels", NovelPage.as_view(), name="novel_page"),
    path("authors", AuthorPage.as_view(), name="author_page"),
    path(
        "<slug:novel_slug>/chapter/<int:chapter_no>/",
        chapter_detail,
        name="chapter_detail",
    ),
    # path("login/", Login.as_view(), name="login"),
    # path("register/", Register.as_view(), name="register"),
    # path("user-view/", ViewUser.as_view(), name="user_view"),
    # path("cart/", views.Cart),
    # path("checkout/", views.Checkout),
]
