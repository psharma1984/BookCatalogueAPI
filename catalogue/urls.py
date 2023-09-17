from django.urls import path
from catalogue import views

urlpatterns = [
    path("catalogue/books/<int:pk>", views.BookList.as_view()),
    path("catalogue/authors/<int:pk>", views.AuthorList.as_view()),
    path("catalogue/genres/<int:pk>", views.GenreList.as_view()),
]
