from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Album, Artist, Song


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


class AlbumListView(ListView):
    model = Album


class AlbumDetailView(DetailView):
    model = Album
