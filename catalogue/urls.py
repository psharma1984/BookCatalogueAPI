from django.urls import path
from catalogue import views

urlpatterns = [
    path("catalogue/books/<int:pk>", views.BookView.as_view(), name="book-detail"),
    path("catalogue/authors/<int:pk>", views.AuthorView.as_view(), name="author-detail"),
    path("catalogue/genres/<int:pk>", views.GenreView.as_view(), name="genre-detail"),
    path("catalogue/genres/", views.GenreList.as_view(), name="genre-list"),
    path("catalogue/books/", views.BookList.as_view(), name="book-list"),
    path("catalogue/authors/", views.AuthorList.as_view(), name="author-list"),
]
