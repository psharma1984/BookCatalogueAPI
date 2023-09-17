from django.db import models

# Create your models here.


class Author(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    id = models.AutoField(primary_key=True)

    class Meta:
        ordering = ["id"]


class Genre(models.Model):
    name = models.CharField(max_length=20)
    id = models.AutoField(primary_key=True)

    class Meta:
        ordering = ["id"]


class Book(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.TextField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="books")
    genres = models.ManyToManyField(Genre, related_name="books")

    class Meta:
        ordering = ["name"]
