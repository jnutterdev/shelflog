from django.views.generic import ListView

from .models import Album, Book, Film

# Create your views here.


class BookView(ListView):
    model = Book
    context_object_name = "books"


class FilmView(ListView):
    model = Film
    context_object_name = "films"


class AlbumView(ListView):
    model = Album
    context_object_name = "albums"
