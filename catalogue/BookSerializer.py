from rest_framework import serializers
from catalogue.models import Book, Genre, Author


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ["name", "price", "description", "author", "genres"]


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ["name", "id"]


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ["name", "age", "id"]
