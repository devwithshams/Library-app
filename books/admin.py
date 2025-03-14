# Django imports
from django.contrib import admin
# Local imports
from .models import Book


# Register the Book model with the admin site
# This will make the Book model available in the Django admin interface
# and allow you to create, view, update, and delete Book objects
# from the admin interface
admin.site.register(Book)
