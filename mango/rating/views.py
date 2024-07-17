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
        rating = int(form["rating"])
        user_album_rating = UserAlbumRating.objects.create(
            user_id=form["user"], album_id=form["album"], rating=rating
        )

        # update running average score of album
        if not album.rating:
            album.rating = 0

        n = album.num_ratings + 1
        currRating = album.num_ratings
        print(form, n, currRating)
        newRating = currRating + (rating - currRating) / n
        album.num_ratings = n
        album.rating = newRating
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
