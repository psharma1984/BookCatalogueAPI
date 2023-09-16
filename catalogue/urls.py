from django.urls import path
from catalogue import views

urlpatterns = [
    path("catalogue/books", views.BookList.as_view()),
    path("catalogue/authors", views.AuthorList.as_view()),
    path("catalogue/genres", views.GenreList.as_view()),
]
