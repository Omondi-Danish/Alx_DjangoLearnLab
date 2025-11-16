from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, permission_required
from django.db.models import Q
from .models import Book
from .forms import BookForm
from .forms import ExampleForm

@permission_required('bookshef.can_view', raise_exception=True)
def book_list(request):
    q = request.GET.get("q", "").strip()
    books = Book.objects.all()
    if q:
        books = books.filter(
            Q(title__icontains=q) | Q(author__icontains=q) | Q(publication_year__icontains=q)
        )
    return render(request, "bookshelf/book_list.html", {"books": books, "q": q})

@permission_required('bookshef.can_create', raise_exception=True)
@login_required
def book_create(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save(commit=False)
            book.owner = request.user
            book.save()
            return redirect("book_list")
    else:
        form = BookForm()
    return render(request, "bookshelf/form_example.html", {"form": form, "action": "Create"})

@permission_required('bookshef.can_edit', raise_exception=True)
@login_required
def book_edit(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect("book_list")
    else:
        form = BookForm(instance=book)
    return render(request, "bookshelf/form_example.html", {"form": form, "action": "Edit"})

@permission_required('bookshef.can_delete', raise_exception=True)
@login_required
def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        book.delete()
        return redirect("book_list")
    return render(request, "bookshelf/book_confirm_delete.html", {"book": book})

def example_form_view(request):
    if request.method == "POST":
        form = ExampleForm(request.POST)
        if form.is_valid():
            return render(request, "bookshelf/example_success.html", {"form": form})
    else:
        form = ExampleForm()
    return render(request, "bookshelf/example_form.html", {"form": form})
