from django.shortcuts import render, redirect
from .models import Book
from .models import Library
from django.views.generic.detail import DetailView
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import user_passes_test

# Create your views here.

def list_books(request):
    books = Book.objects.all()
    return render(request, "relationship_app/list_books.html", {"books": books})

class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"
    context_object_name = "library"
    
# Function-based view for login

def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user) # Log the user in
            return redirect("list_books") # Redirect after log in
    else:
        form = AuthenticationForm()
    return render(request, "relationship_app/login.html", {"form": form})

# Function-based view for logout

def user_logout(request):
    logout(request)
    return render(request, "relationship_app/logout.html")

# Function-based view for registration

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user) # Log in immediately after registration
            return redirect("list_books")
    
    else:
        form = UserCreationForm()
    return render(request, "relationship_app/register.html", {"form": form})

def is_admin(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile == 'Admin'

def is_librarian(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Librarian'

def is_member(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Member'

@user_passes_test(is_admin, login_url='login')
def admin_view(request):
    return render(request, "relationship_app/admin_view.html")

@user_passes_test(is_librarian, login_url='login')
def librarian_view(request):
    return render(request, "relationship/librarian_view.html")

@user_passes_test(is_member, login_url='login')
def member_view(request):
    return render (request, "relationship_app/member_view.html")
