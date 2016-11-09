from django.forms import ModelForm

from .models import BookStore

class BookForm(ModelForm):
    """
    Form for Adding Books 
    It will contain title, author and category

    """
    class Meta:
        model = BookStore
        fields = ['title', 'author', 'category',]