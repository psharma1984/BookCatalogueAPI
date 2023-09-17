from rest_framework import serializers
from catalogue.models import Book, Genre, Author


class BookSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        genres_data = validated_data.pop("genres", None)
        book = Book.objects.create(**validated_data)
        for genre_data in genres_data:
            book.genres.add(genre_data)
            book.save()
        return book

    class Meta:
        model = Book
        fields = ["name", "price", "description", "author", "genres"]


class GenreSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        return Genre.objects.create(**validated_data)

    class Meta:
        model = Genre
        fields = ["name", "id"]


class AuthorSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        return Author.objects.create(**validated_data)

    class Meta:
        model = Author
        fields = ["name", "age", "id"]
