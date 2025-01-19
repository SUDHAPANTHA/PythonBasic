from django.urls import path
from book_app import views

urlpatterns = [
    path("", views.book_list, name="book-list"),  # Listing all books
    path("create/", views.book_create, name="create-book"),  # Creating a new book
    path("delete/<int:pk>/", views.delete_book, name="delete-book"),  # Deleting a book
    path("update/<int:id>/", views.update_book, name="update-book"),  # Updating a book
]
