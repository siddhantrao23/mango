from django.db import models
from django.urls import reverse
from django.db.models.functions import Lower
from django.db.models import UniqueConstraint


# Create your models here.


class Album(models.Model):
    title = models.CharField(max_length=200, help_text="Enter the album name")
    artist = models.ForeignKey("Artist", on_delete=models.RESTRICT)
    genre = models.ManyToManyField(
        "Genre", blank=True, help_text="Select a genre for this album"
    )
    release_date = models.DateField()
    rating = models.SmallIntegerField(blank=True, null=True)
    album_cover = models.ImageField()

    def __str__(self):
        return self.title - self.artist

    def get_absolute_url(self):
        return reverse("album-detail", kwargs={"pk": self.pk})

    class Meta:
        ordering = ["title"]


class Song(models.Model):
    title = models.CharField(max_length=200, help_text="Enter the song name")
    duration = models.DurationField()
    album = models.ForeignKey("Album", on_delete=models.RESTRICT)

    def __str__(self) -> str:
        return self.title - self.duration

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
    title = models.CharField(
        max_length=200,
        unique=True,
        help_text="Enter a song genre (eg. Electronic, Indie, Pop)",
    )

    def __str__(self) -> str:
        return self.title

    def get_absolute_url(self):
        return reverse("genre-detail", kwargs={"pk": self.pk})

    class Meta:
        constraints = [
            UniqueConstraint(
                Lower("title"),
                name="genre_name_case_insensitive_unique",
                violation_error_message="Genre already exists (case insensitive match)",
            )
        ]
        ordering = ["title"]
