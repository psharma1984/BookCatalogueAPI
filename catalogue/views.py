from rest_framework.response import Response
from rest_framework.views import APIView
from catalogue.models import Book
from catalogue.BookSerializer import BookSerializer

# Create your views here.


class BookList(APIView):
    def get(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)
