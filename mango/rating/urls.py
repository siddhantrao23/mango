from django.urls import path
from .views import AlbumListView, AlbumDetailView, index

urlpatterns = [
    path("", index, name="index"),
    path("albums/", AlbumListView.as_view(), name="albums"),
    path("albums/<int:pk>", AlbumDetailView.as_view(), name="album-detail"),
]
