from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    title = forms.CharField(max_length=200, strip=True)
    author = forms.CharField(max_length=100, strip=True)
    publication_year = forms.IntegerField(min_value=0)

    class Meta:
        model = Book
        fields = ["title", "author", "publication_year"]


class ExampleForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)
