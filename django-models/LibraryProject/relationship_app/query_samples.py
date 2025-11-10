import os
import django

# Setting up Django Environment

os.environ.setdefault("DJANGO_SETTING_MODULE", "LibraryProject.settings")
django.setup

from relationship_app.models import Author, Book, Library, Librarian

# Query all books by specific author

def books_by_author(author_name):
    try:
        author = Author.objects.get(name=author_name)
        return author.books.all()

    except Author.DoesNotExist:
        return []

# List all books in the Library

def books_in_library(library_name):
    try:
        library = Library.objects.get(library_name)
        return library.books.all()
    except Library.DoesNotExist:
        return []

# Retrieve the librarian for a library

def librarian_for_library(library_name):
    try:
        library = Library.objects.get(library_name)
        return library.librarian
    except Library.DoesNotExist:
        return None
    
if __name__ == "__main__":
    
    # Example usage
    print("Books by Author Sidney:", books_by_author("Sidney"))
    print("Books in Library Central:", books_in_library("Central"))
    print("Librarian for Library Central:", librarian_for_library("Central"))