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
