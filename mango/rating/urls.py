from django.urls import path
from .views import (
    AlbumListView,
    AlbumDetailView,
    ArtistDetailView,
    ArtistListView,
    SongDetailView,
    index,
)

urlpatterns = [
    path("", index, name="index"),
    path("albums/", AlbumListView.as_view(), name="albums"),
    path("albums/<int:pk>", AlbumDetailView.as_view(), name="album-detail"),
    path("artists/", ArtistListView.as_view(), name="artists"),
    path("artists/<int:pk>", ArtistDetailView.as_view(), name="artist-detail"),
    path("songs/<int:pk>", SongDetailView.as_view(), name="songs-detail"),
]
