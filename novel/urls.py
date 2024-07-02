from django.urls import path
from .views import *


urlpatterns = [
    path("", Index.as_view(), name="index"),
    path("novels", NovelPage.as_view(), name="novel_page"),
    path("authors", AuthorPage.as_view(), name="author_page"),
    # path("home/", Index.as_view(), name="index"),
    # path("login/", Login.as_view(), name="login"),
    # path("register/", Register.as_view(), name="register"),
    # path("user-view/", ViewUser.as_view(), name="user_view"),
    # path("cart/", views.Cart),
    # path("checkout/", views.Checkout),
]
