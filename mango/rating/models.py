from django.db import models
from django.urls import reverse
from django.db.models.functions import Lower
from django.db.models import UniqueConstraint
from django.conf import settings


# Create your models here.


class Album(models.Model):
    title = models.CharField(max_length=200, help_text="Enter the album name")
    artist = models.ForeignKey("Artist", on_delete=models.RESTRICT)
    genre = models.ManyToManyField(
        "Genre", blank=True, help_text="Select a genre for this album"
    )
    release_date = models.DateField()
    rating = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    num_ratings = models.IntegerField(default=0)
    album_cover = models.ImageField(upload_to="images/")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("album-detail", kwargs={"pk": self.pk})

    def display_genre(self):
        return ", ".join(genre.name for genre in self.genre.all()[:3])

    display_genre.short_description = "Genre"

    class Meta:
        ordering = ["title"]


class Song(models.Model):
    title = models.CharField(max_length=200, help_text="Enter the song name")
    duration = models.DurationField()
    album = models.ForeignKey("Album", on_delete=models.RESTRICT)

    def __str__(self) -> str:
        return self.title

    def get_absolute_url(self):
        return reverse("song-detail", kwargs={"pk": self.pk})


class Artist(models.Model):
    name = models.CharField(max_length=200)
    bio = models.TextField(max_length=800, blank=True, null=True)

    def get_absolute_url(self):
        return reverse("artist-detail", kwargs={"pk": self.pk})

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(
        max_length=200,
        unique=True,
        help_text="Enter a song genre (eg. Electronic, Indie, Pop)",
    )

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self):
        return reverse("genre-detail", kwargs={"pk": self.pk})

    class Meta:
        constraints = [
            UniqueConstraint(
                Lower("name"),
                name="genre_name_case_insensitive_unique",
                violation_error_message="Genre already exists (case insensitive match)",
            )
        ]
        ordering = ["name"]


class Ratings(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.RESTRICT)
    album = models.ForeignKey("Album", on_delete=models.RESTRICT)
    rating = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)

    class Meta:
        constraints = [
            UniqueConstraint(fields=["user", "album"], name="unique_composite_key")
        ]
