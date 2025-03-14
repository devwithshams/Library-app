from django.urls import path
from .views import BookListView, BookDetailView

# Define the URL patterns for the books app
# The URL patterns map URL paths to views
# The views are defined in the 'books/views.py' file
# The URL patterns are included in the URL patterns in the 'library/urls.py' file

urlpatterns = [
    # Define the URL pattern for the home page
    # The URL pattern maps the empty path '' to the BookListView view
    # The name 'home' is used to identify the view
    # The name can be used to refer to the view in the template
    path('', BookListView.as_view(), name='home'),
    path('<int:pk>/', BookDetailView.as_view(), name='book'),
]