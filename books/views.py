from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Book

# Create your views here.
# Define a view for the home page
# This view will display a list of all Book objects
# in the database
# The view extends the ListView class provided by Django
# The ListView class provides a simple way to display a list of objects
# in a template
# The ListView class requires two attributes:
# model: The model class to use for the list of objects
# template_name: The name of the template to use to render the list of objects
# The ListView class will automatically query the database for all objects
# of the specified model class and pass them to the template for rendering
# The ListView class will also automatically create a context variable
# containing the list of objects, which can be accessed in the template
# using the name 'object_list'
# In this case, the view is defined for the Book model
# The template used to render the list of books is 'books/book_list.html'
# The view is defined as a class-based view, which is a more powerful
# and flexible way to define views in Django
# The view is defined as a subclass of the ListView class
# The view is named 'BookListView'
# The view is defined in the 'books/views.py' file
# The view is imported in the 'books/urls.py' file
# The view is included in the URL patterns in the 'library/urls.py' file    


class BookListView(ListView):
    model = Book
    template_name = 'books/book_list.html'

# Define a view for the book detail page
# This view will display the details of a single Book object
# The view extends the DetailView class provided by Django
# The DetailView class provides a simple way to display the details of a single object
# in a template
# The DetailView class requires two attributes:
# model: The model class to use for the object
# template_name: The name of the template to use to render the object
# The DetailView class will automatically query the database for the object
# of the specified model class with the specified primary key and pass it to
# the template for rendering
# The DetailView class will also automatically create a context variable
# containing the object, which can be accessed in the template
# using the name 'object'
# In this case, the view is defined for the Book model
# The template used to render the book details is 'books/book_detail.html'
# The view is defined as a class-based view, which is a more powerful
# and flexible way to define views in Django
# The view is defined as a subclass of the DetailView class
# The view is named 'BookDetailView'
# The view is defined in the 'books/views.py' file
# The view is imported in the 'books/urls.py' file
# The view is included in the URL patterns in the 'library/urls.py' file

class BookDetailView(DetailView):
    model = Book
    template_name = 'books/book_detail.html'