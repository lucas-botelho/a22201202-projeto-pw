
from django.urls import path
from . import views

app_name = 'bandas'

urlpatterns = [
    path('', views.band_list_view, name='index'),
    path('band/<int:band_id>/', views.band_detail_view, name='band_detail'),
    path('album/<int:album_id>/', views.album_view, name='album_detail'),
    path('song/<int:song_id>/', views.song_details, name='song_detail'),
    path('song/create/', views.createSong, name='create_song'),
    path('band/create/', views.createBand, name='create_band'),
    path('album/create/', views.createAlbum, name='create_album'),
    path('album/<int:album_id>/edit/', views.edit_album, name='edit_album'),
    path('band/<int:band_id>/edit/', views.edit_band, name='edit_band'),
    path('song/<int:song_id>/edit/', views.edit_song, name='edit_song'),
    path('song/<int:song_id>/delete/', views.delete_song, name='delete_song'),
    path('band/<int:band_id>/delete/', views.delete_band, name='delete_band'),
    path('album/<int:album_id>/delete/', views.delete_album, name='delete_album'),

]
