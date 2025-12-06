from django.shortcuts import render
from rest_framework import generics, permissions
from .models import Book, Author
from .serializers import BookSerializer, AuthorSerializer

# Create your views here.
class BookListView(generics.ListAPIView):
    """
    GET /books/
    Return a list of books
    Allow for anyone to see the list
    """
    
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_clases = [permissions.AllowAny]
    
class BookDetailView(generics.RetrieveAPIView):
    """
    GET /books/<id>/
    Return details of a single book by ID
    Accessible to everyone(read-only)
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_class = [permissions.AllowAny]
    
class BookCreateView(generics.CreateAPIView):
    """
    POST /books/create/
    create a single book
    Accessible to only authenticated users
    """
    
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_class = [permissions.IsAuthenticated]
    
    def perform_update(self, serializer):
        serializer.is_valid(raise_exception=True)
        serializer.save()
    
class BookUpdateView(generics.UpdateAPIView):
    """
    PUT/PATCH /books/<id>/update/
    Update a single book by ID
    Accessible to only authenticated users
    """
    
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_class = [permissions.IsAuthenticated]
    
    def perform_update(self, serializer):
        serializer.is_valid(raise_exception=True)
        serializer.save()
    
class BookDeleteView(generics.DestroyAPIView):
    """
    DELETE /books/<id>/delete
    delete a single book by ID
    accessible to only authenticated users
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_class = [permissions.IsAuthenticated]