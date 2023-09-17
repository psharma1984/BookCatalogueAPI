from django.urls import path
from catalogue import views

urlpatterns = [
    path("catalogue/books/<int:pk>", views.BookView.as_view()),
    path("catalogue/authors/<int:pk>", views.AuthorView.as_view()),
    path("catalogue/genres/<int:pk>", views.GenreView.as_view()),
    path("catalogue/genres/", views.GenreList.as_view()),
    path("catalogue/books/", views.BookList.as_view()),
    path("catalogue/authors/", views.AuthorList.as_view()),
]
