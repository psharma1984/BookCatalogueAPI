from rest_framework import serializers
from catalogue.models import Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ["name", "price", "description"]
