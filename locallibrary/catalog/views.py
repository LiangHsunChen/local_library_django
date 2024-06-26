from django.shortcuts import render
from .models import Book, Author, BookInstance, Genre
from django.views import generic


class BookListView(generic.ListView):
    model = Book
    # your own name for the list as a template variable
    context_object_name = 'book_list'
    queryset = Book.objects.filter(title__icontains='book')[
        :5]  # Get 5 books containing the title war
    # Specify your own template name/location
    template_name = 'books/book_list.html'
    paginate_by = 2


class BookDetailView(generic.DetailView):
    model = Book


def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    # Available books (status = 'a')
    num_instances_available = BookInstance.objects.filter(
        status__exact='a').count()

    # The 'all()' is implied by default.
    num_authors = Author.objects.count()

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)
