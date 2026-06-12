from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


# Create your models here.
class MediaItem(models.Model):
    title = models.CharField(max_length=255)
    release_year = models.IntegerField(
        validators=[MinValueValidator(1000), MaxValueValidator(9999)]
    )
    rating = models.IntegerField(
        blank=True, null=True, validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    notes = models.TextField(
        blank=True,
        null=True,
    )

    class Meta:
        abstract = True

    def __str__(self):
        return str(self.title)


# Book (extends MediaItem)
# ├── status (want / reading / finished)
# ├── date_finished (optional)
# └── author

# Film (extends MediaItem)
# └── director

# Album (extends MediaItem)
# ├── artist
# └── label


class Book(MediaItem):
    STATUS_CHOICES = [
        ("want", "Want to Read"),
        ("reading", "Reading"),
        ("finished", "Finished"),
    ]

    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="want")
    date_finished = models.DateField(null=True, blank=True)
    author = models.CharField(max_length=255)


class Film(MediaItem):
    director = models.CharField(max_length=255)


class Album(MediaItem):
    artist = models.CharField(max_length=255)
    label = models.CharField(max_length=255, null=True, blank=True)
