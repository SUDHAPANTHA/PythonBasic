from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect
from book_app.forms import BookForm
from book_app.models import Book

def book_list(request):
    books = Book.objects.all()
    return render(request,"book_list.html",{"books": books})
def book_create(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('book-list')  # Redirect to book list page
    else:
        form = BookForm()
    return render(request, 'book_app/book_form.html', {'form': form})
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


