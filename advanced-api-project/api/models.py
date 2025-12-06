from django.db import models

# Create your models here.
class Book(models.Model):
    """
    Adding Book model to be stored as tables in the database
    Each book is linked to an author with a foreign key
    """
    
    title = models.CharField(max_length=50)
    publication_year = models.DateField()
    author = models.ForeignKey('Author', on_delete=models.CASCADE, related_name="books")
    
    def __str__(self):
        return f"{self.title} ({self.publication_year})"
    
class Author(models.Model):
    """
    Author field
    One author has written many books(one to many relationships)
    """
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name