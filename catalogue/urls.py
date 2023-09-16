from django.urls import path
from catalogue import views

urlpatterns = [
    path("catalogue/", views.BookList),
]
