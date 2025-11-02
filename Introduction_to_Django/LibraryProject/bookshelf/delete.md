##steps to delete books
on the terminal on your project folder run python manage.py shell
Import the Book class from the models by running  from bookshelf.models import Book
create a book variable e.g book and initialize it with your book details
        `book = Book.objects.create(title="1984", author="George Orwell", published_year=1949)`
book.delete()
