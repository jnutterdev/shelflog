from django.urls import path

from . import views

urlpatterns = [
    path("books/", views.BookView.as_view(), name="book-list"),
    path("albums/", views.AlbumView.as_view(), name="album-list"),
    path("films/", views.FilmView.as_view(), name="film-list"),
]
