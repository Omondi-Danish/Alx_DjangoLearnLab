## Steps for retrieval

create an instance variable before retrieval
then initialize with retrieval command using id to uniquely identify the book
retrieved_bbook = Book.objects.get(id=book.id)
then print using book title
print(retrieved_book.title)

Done!
