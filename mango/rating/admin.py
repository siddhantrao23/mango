from django.contrib import admin
from .models import Album, Song, Artist, Genre, Ratings

# Register your models here.
admin.site.register(Song)
admin.site.register(Genre)
admin.site.register(Ratings)


class SongInline(admin.TabularInline):
    model = Song
    extra = 0


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "artist",
        "display_genre",
        "release_date",
        "rating",
        "album_cover",
    )

    list_filter = ("artist", "genre", "rating")

    inlines = [SongInline]


class AlbumInline(admin.TabularInline):
    model = Album
    extra = 0


@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "bio",
    )

    inlines = [AlbumInline]
