from rest_framework import serializers
from catalogue.models import Book, Genre, Author


class BookSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()
    genres = serializers.StringRelatedField(many=True)

    class Meta:
        model = Book
        fields = ["name", "price", "description", "author", "genres", "id"]

    def create(self, validated_data):
        genres_data = validated_data.pop("genres", None)
        book = Book.objects.create(**validated_data)
        for genre_data in genres_data:
            book.genres.add(genre_data)
            book.save()
        return book

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.price = validated_data.get("price", instance.price)
        instance.description = validated_data.get("description", instance.description)
        instance.save()
        return instance


class GenreSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        return Genre.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.save()
        return instance

    class Meta:
        model = Genre
        fields = ["name", "id"]


class AuthorSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        return Author.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.age = validated_data.get("age", instance.age)
        instance.save()
        return instance

    class Meta:
        model = Author
        fields = ["name", "age", "id"]
