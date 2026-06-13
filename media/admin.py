from django.contrib import admin

from media.models import Album, Book, Film


class BookAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        "author",
        "release_year",
    ]
    search_fields = [
        "title",
        "author",
        "release_year",
    ]


class FilmAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        "director",
        "release_year",
    ]
    search_fileds = [
        "title",
        "director",
        "release_year",
    ]


class AlbumAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        "artist",
        "release_year",
    ]
    search_fields = [
        "title",
        "artist",
        "release_year",
    ]


# Register your models here.
admin.site.register(Book, BookAdmin)
admin.site.register(Film, FilmAdmin)
admin.site.register(Album, AlbumAdmin)
