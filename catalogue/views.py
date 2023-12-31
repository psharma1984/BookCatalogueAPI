from rest_framework.response import Response
from rest_framework.views import APIView
from catalogue.models import Book, Author, Genre
from catalogue.BookSerializer import BookSerializer, AuthorSerializer, GenreSerializer
from rest_framework import status


# Create your views here.
class BookList(APIView):
    def get(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, context={"request": request}, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = BookSerializer(data=request.data, context={"request": request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BookView(APIView):
    def get(self, request, **kwargs):
        book = Book.objects.get(id=kwargs["pk"])
        serializer = BookSerializer(book, context={"request": request})
        return Response(serializer.data)

    def put(self, request, **kwargs):
        book = Book.objects.get(id=kwargs["pk"])
        serializer = BookSerializer(book, data=request.data, context={"request": request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, **kwargs):
        book = Book.objects.get(id=kwargs["pk"])
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class AuthorList(APIView):
    def get(self, request):
        authors = Author.objects.all()
        serializer = AuthorSerializer(authors, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AuthorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AuthorView(APIView):
    def get(self, request, **kwargs):
        author = Author.objects.get(id=kwargs["pk"])
        serializer = AuthorSerializer(author, context={"request": request})
        return Response(serializer.data)

    def put(self, request, **kwargs):
        author = Author.objects.get(id=kwargs["pk"])
        serializer = AuthorSerializer(author, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, **kwargs):
        author = Author.objects.get(id=kwargs["pk"])
        author.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class GenreList(APIView):
    def get(self, request):
        genres = Genre.objects.all()
        serializer = GenreSerializer(genres, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = GenreSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GenreView(APIView):
    def get(self, request, **kwargs):
        genre = Genre.objects.get(id=kwargs["pk"])
        serializer = GenreSerializer(genre, context={"request": request})
        return Response(serializer.data)

    def put(self, request, **kwargs):
        genre = Genre.objects.get(id=kwargs["pk"])
        serializer = GenreSerializer(genre, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, **kwargs):
        genre = Genre.objects.get(id=kwargs["pk"])
        genre.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
