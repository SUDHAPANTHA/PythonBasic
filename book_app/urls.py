
from django.urls import path
from book_app import views

urlpatterns = [
    path("", views.book_list),
    path("add-book/", views.add_book, name="add-book"),
    path("delete/<int:pk>/", views.delete_book, name="delete-book"),
    path("update/<int:id>/", views.update_book, name="update-book"),

]