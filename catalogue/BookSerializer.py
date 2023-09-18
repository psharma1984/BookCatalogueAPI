from rest_framework import serializers
from catalogue.models import Book, Genre, Author


class RelatedAuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ["name", "url", "age"]


class RelatedGenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ["name", "url"]


class BookSerializer(serializers.ModelSerializer):
    author = RelatedAuthorSerializer()
    genres = RelatedGenreSerializer(many=True)

    class Meta:
        model = Book
        fields = ["name", "price", "description", "author", "genres", "id"]

    def create(self, validated_data):
        genres_data = validated_data.pop("genres", [])
        author_data = validated_data.pop("author", None)

        if author_data:
            author, created = Author.objects.get_or_create(**author_data)
        else:
            author = None
        book = Book.objects.create(author=author, **validated_data)

        for genre_data in genres_data:
            genre, created = Genre.objects.get_or_create(**genre_data)
            book.genres.add(genre)
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
