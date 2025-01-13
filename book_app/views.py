from django.http import HttpResponseRedirect
from django.shortcuts import render
from book_app.models import Book

def book_list(request):
    books = Book.objects.all()
    return render(request,"book_list.html",{"books": books})
def todo_add_book(request):
    if request.method == "GET":
        return render(request,"todo_add_book.html")
    else:
        title = request.POST["title"]
        book = Book(title=title)
        book.save
        return HttpResponseRedirect("/")
def update_book(request, id):
            book = Book.objects.get(id=id)
            if request.method == "GET": 
                return render(request, "update_book.html", {"book": book},) 
            else:
                book.title = request.POST["title"]
                book.save()
                return HttpResponseRedirect("/")
def delete_book(request, pk):
    book = Book.objects.get(id=pk)
    book.delete()
    return HttpResponseRedirect("/")    


# Create your views here.

