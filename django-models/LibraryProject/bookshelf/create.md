## Step by step of Book instance creation via terminal python shell
on the terminal on your project folder run python manage.py shell
Import the Book class from the models by running from from your_app_name.models import Book
create a book variable e.g book and initialize it with your book details
        `book = Book.objects.create(title="1984", author="George Orwell", published_year=1949)`
Then save by running book.save()
