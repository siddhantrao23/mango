from typing import Any
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Album, Artist, Song, UserAlbumRating


# Create your views here.
def index(request):
    num_albums = Album.objects.all().count()
    num_artists = Artist.objects.all().count()
    num_songs = Song.objects.all().count()

    context = {
        "num_albums": num_albums,
        "num_artists": num_artists,
        "num_songs": num_songs,
    }

    return render(request, "index.html", context)


def submit_ratings(request):
    if request.method == "POST":
        form = request.POST.dict()
        album = get_object_or_404(Album, pk=form["album"])
        user_rating = int(form["rating"]) * 10 / album.song_set.count()
        user_album_rating = UserAlbumRating.objects.create(
            user_id=form["user"], album_id=form["album"], rating=user_rating
        )
        album.num_ratings += 1

        if not album.rating:
            album.rating = 0
        currRating = float(album.rating)
        newRating = currRating + (user_rating - currRating) / album.num_ratings
        album.rating = round(newRating, 2)
        album.save()
        user_album_rating.save()
        return HttpResponseRedirect(
            reverse("album-detail", kwargs={"pk": form["album"]})
        )


class AlbumListView(ListView):
    model = Album


class AlbumDetailView(DetailView):
    model = Album


class ArtistListView(ListView):
    model = Artist


class ArtistDetailView(DetailView):
    model = Artist


class SongDetailView(DetailView):
    model = Song


class AlbumRatingView(LoginRequiredMixin, DetailView):
    model = Album
    template_name = "rating/user_album_rating.html"
