from django.shortcuts import render, get_object_or_404
from .models import Book
from .forms import BookForm
from django.template.loader import render_to_string
from django.http import JsonResponse


# Create your views here.
def index(request):
    books = Book.objects.all()
    return render(request, 'bookcrud/index.html', {'books': books})


def save_book_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            books = Book.objects.all()
            data['html_book_list'] = render_to_string('bookcrud/includes/partial-book-list.html',
                                                      {'books': books})
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)


def create_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
    else:
        form = BookForm()
    return save_book_form(request, form, 'bookcrud/includes/partial-book-create.html')


def update_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
    else:
        form = BookForm(instance=book)
    return save_book_form(request, form, 'bookcrud/includes/partial-book-update.html')


def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    data = dict()
    if request.method == 'POST':
        book.delete()
        data['form_is_valid'] = True # This is just to play along with the existing code
        books = Book.objects.all()
        data['html_book_list'] = render_to_string('bookcrud/includes/partial-book-list.html', {
            'books': books
        })
    else:
        context = {'book': book}
        data['html_form'] = render_to_string('bookcrud/includes/partial-book-delete.html',
                                             context,
                                             request=request,
                                             )
    return JsonResponse(data)
