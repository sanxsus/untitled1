from functools import wraps

from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import generics
from .models import Book
from .serializers import BookSerializer, BookbyidSerializer, BookDetailSerializer


class BookViewSet(viewsets.ViewSet):
    def list(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response({'books': serializer.data})

    def book_id(self, request, id):
        result = Book.objects.filter(id=id)
        serializer1 = BookbyidSerializer(result, many=True)
        return Response({"result": serializer1.data})

    def get(self, request, id):
        return self.book_id(self, id)


def index(request):
    return HttpResponse("Hello, world.")


class BookCreateView(generics.CreateAPIView):
    serializer_class = BookDetailSerializer


class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BookDetailSerializer
    queryset = Book.objects.all()
