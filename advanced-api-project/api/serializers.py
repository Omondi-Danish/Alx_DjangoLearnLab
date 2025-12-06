from rest_framework import serializers
from .models import Book, Author
import datetime

class BookSerializer(serializers.ModelSerializer):
    """
    Serializes Book model fields.
    Includes custom validation to ensure publication year is not in the future
    """
    class Meta:
        model = Book
        fields = '__all__'
        
        
    def validate_publication_year(self, value):
        current_year = datetime.date.today().year
        
        if value.year > current_year:
            raise serializers.ValidationError("Publication cannot be in the future")
        return value
        
class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)
    
    class Meta:
        model = Author
        fields = ["id", "name", "books"]