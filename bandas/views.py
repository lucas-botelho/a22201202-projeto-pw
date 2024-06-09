from django.shortcuts import render, redirect
from .models import Band, Album, Song
from .forms import SongForm, BandForm, AlbumForm
from django.contrib.auth.decorators import login_required

def index_view(request):
    context = {}
    return render(request, 'bandas/index.html', context)

def band_list_view(request):
    bands = Band.objects.all()
    context = {'bands': bands}
    return render(request, 'bandas/bands.html', context)

def album_view(request, album_id):
    album = Album.objects.get(id=album_id)
    songs = Song.objects.filter(album=album)
    context = {'album': album, 'songs': songs}
    return render(request, 'bandas/album.html', context)

def song_details(request, song_id):
    song = Song.objects.get(id=song_id)
    album = Album.objects.get(song = song)
    context = {'song': song, 'album' : album}

    return render(request, 'bandas/song_details.html', context)

def band_detail_view(request, band_id):
    band = Band.objects.get(pk=band_id)
    albuns = Album.objects.filter(band=band)
    context = {'band': band, 'albums': albuns}
    return render(request, 'bandas/band_detail.html', context)

@login_required
def createSong(request):
    if request.method == 'POST':
        form = SongForm(request.POST)
        if form.is_valid():
            song = form.save(commit=False)
            song.save()
            return redirect('bandas:song_detail', song_id=song.id)
    else:
        form = SongForm()
    
    return render(request, 'bandas/create_song.html', {'form': form})

@login_required
def createBand(request):
    if request.method == 'POST':
        form = BandForm(request.POST, request.FILES)
        if form.is_valid():
            band = form.save(commit=False)
            band.save()
            return redirect('bandas:band_detail', band_id=band.id)
    else:
        form = BandForm()
    
    return render(request, 'bandas/create_band.html', {'form': form})

@login_required
def createAlbum(request):
    if request.method == 'POST':
        form = AlbumForm(request.POST, request.FILES)
        if form.is_valid():
            album = form.save(commit=False)
            album.save()
            return redirect('bandas:album_detail', album_id=album.id)
    else:
        form = AlbumForm()
    
    return render(request, 'bandas/create_album.html', {'form': form})

@login_required
def edit_song(request, song_id):
    song = Song.objects.get(id=song_id)
    if request.method == 'POST':
        form = SongForm(request.POST, instance=song)
        if form.is_valid():
            form.save()
            return redirect('bandas:song_detail', song_id=song.id)
    else:
        form = SongForm(instance=song)
    return render(request, 'bandas/edit_song.html', {'form': form})

@login_required
def edit_band(request, band_id):
    band = Band.objects.get(id=band_id)
    if request.method == 'POST':
        form = BandForm(request.POST, request.FILES, instance=band)
        if form.is_valid():
            form.save()
            return redirect('bandas:band_detail', band_id=band.id)
    else:
        form = BandForm(instance=band)
    return render(request, 'bandas/edit_band.html', {'form': form})

@login_required
def edit_album(request, album_id):
    album = Album.objects.get(id=album_id)
    if request.method == 'POST':
        form = AlbumForm(request.POST, request.FILES, instance=album)
        if form.is_valid():
            form.save()
            return redirect('bandas:album_detail', album_id=album.id)
    else:
        form = AlbumForm(instance=album)
    return render(request, 'bandas/edit_album.html', {'form': form})

@login_required
def delete_song(request, song_id):
    song = Song.objects.get(id=song_id)
    if request.method == 'POST':
        song.delete()
        return redirect('bandas:index')
    return render(request, 'bandas/delete_songs.html', {'song': song})

@login_required
def delete_band(request, band_id):
    band = Band.objects.get(id=band_id)
    if request.method == 'POST':
        band.delete()
        return redirect('bandas:index')
    return render(request, 'bandas/delete_band.html', {'band': band})

@login_required
def delete_album(request, album_id):
    album = Album.objects.get(id=album_id)
    if request.method == 'POST':
        album.delete()
        return redirect('bandas:index')
    return render(request, 'bandas/delete_album.html', {'album': album})
 


