
from django.urls import path
from book_app import views

urlpatterns = [
    path("", views.book_list),
    path("add-book/", views.add_book),
    path("delete/<int:pk>/", views.delete_book),
    path("update/<int:id>/", views.update_book),

]