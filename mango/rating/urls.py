from django.urls import path
from .views import (
    AlbumListView,
    AlbumDetailView,
    AlbumRatingView,
    ArtistDetailView,
    ArtistListView,
    SongDetailView,
    index,
    submit_ratings,
)

urlpatterns = [
    path("", index, name="index"),
    path("albums/", AlbumListView.as_view(), name="albums"),
    path("albums/<int:pk>", AlbumDetailView.as_view(), name="album-detail"),
    path("albums/<int:pk>/rate", AlbumRatingView.as_view(), name="album-rating"),
    path("artists/", ArtistListView.as_view(), name="artists"),
    path("artists/<int:pk>", ArtistDetailView.as_view(), name="artist-detail"),
    path("songs/<int:pk>", SongDetailView.as_view(), name="songs-detail"),
    path("submit-ratings/", submit_ratings, name="submit-ratings"),
]
