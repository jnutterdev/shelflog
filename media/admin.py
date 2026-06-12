from django.contrib import admin

from media.models import Album, Book, Film

# Register your models here.
admin.site.register(Book)
admin.site.register(Film)
admin.site.register(Album)
