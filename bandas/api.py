from ninja import NinjaAPI
from django.shortcuts import get_object_or_404
from .models import Banda, Album, Musica
from .schemas import BandaIn, BandaOut, ErrorSchema, AlbumIn, AlbumOut, MusicaIn, MusicaOut, BandaComAlbuns, AlbumComMusicas, MusicaComBandaEAlbum
from typing import List

api = NinjaAPI(
    title="App API",
    version="1.0.0",
    description="API for managing bands, albums, and songs."
)

@api.get("/bands",
         response={200: List[BandaComAlbuns]},
         tags=["Bands"],
         description="List all registered bands.")
def list_bands(request):
    return 200, Banda.objects.all()

@api.get("/bands/{band_id}",
         response={200: BandaComAlbuns, 404: ErrorSchema},
         tags=["Bands"],
         description="Retrieve a band by its ID.")
def get_band(request, band_id: int):
    try:
        return 200, Banda.objects.get(id=band_id)
    except Banda.DoesNotExist:
        return 404, {"detail": "Band not found"}

@api.post("/bands",
          response={201: BandaOut, 400: ErrorSchema},
          tags=["Bands"],
          description="Create a new band.")
def create_band(request, band: BandaIn):
    return 201, Banda.objects.create(**band.dict())

@api.put("/bands/{band_id}/",
         response={200: BandaOut, 404: ErrorSchema},
         tags=["Bands"],
         description="Update a band's information by ID.")
def update_band(request, band_id: int, band: BandaIn):
    obj = get_object_or_404(Banda, id=band_id)
    for attr, value in band.dict().items():
        setattr(obj, attr, value)
    obj.save()
    return 200, obj

@api.delete("/bands/{band_id}/",
            response={204: None, 404: ErrorSchema},
            tags=["Bands"],
            description="Delete a band by ID.")
def delete_band(request, band_id: int):
    obj = get_object_or_404(Banda, id=band_id)
    obj.delete()
    return 204, None

@api.get("/albums",
         response=List[AlbumComMusicas],
         tags=["Albums"],
         description="List all albums.")
def list_albums(request):
    return Album.objects.all()

@api.get("/albums/{album_id}",
         response={200: AlbumComMusicas, 404: ErrorSchema},
         tags=["Albums"],
         description="Retrieve an album by its ID.")
def get_album(request, album_id: int):
    album = get_object_or_404(Album, id=album_id)
    return 200, album

@api.post("/albums",
          response={201: AlbumOut},
          tags=["Albums"],
          description="Create a new album.")
def create_album(request, album: AlbumIn):
    return 201, Album.objects.create(**album.dict())

@api.put("/albums/{album_id}/",
         response={200: AlbumOut, 404: ErrorSchema},
         tags=["Albums"],
         description="Update an album's information by ID.")
def update_album(request, album_id: int, album: AlbumIn):
    obj = get_object_or_404(Album, id=album_id)
    for attr, value in album.dict().items():
        setattr(obj, attr, value)
    obj.save()
    return 200, obj

@api.delete("/albums/{album_id}/",
            response={204: None, 404: ErrorSchema},
            tags=["Albums"],
            description="Delete an album by ID.")
def delete_album(request, album_id: int):
    obj = get_object_or_404(Album, id=album_id)
    obj.delete()
    return 204, None

@api.get("/songs",
         response=List[MusicaComBandaEAlbum],
         tags=["Songs"],
         description="List all songs.")
def list_songs(request):
    return Musica.objects.all()

@api.get("/songs/{song_id}",
         response={200: MusicaComBandaEAlbum, 404: ErrorSchema},
         tags=["Songs"],
         description="Retrieve a song by its ID.")
def get_song(request, song_id: int):
    song = get_object_or_404(Musica, id=song_id)
    return 200, song

@api.post("/songs",
          response={201: MusicaOut},
          tags=["Songs"],
          description="Create a new song.")
def create_song(request, song: MusicaIn):
    return 201, Musica.objects.create(**song.dict())

@api.put("/songs/{song_id}/",
         response={200: MusicaOut, 404: ErrorSchema},
         tags=["Songs"],
         description="Update a song's information by ID.")
def update_song(request, song_id: int, song: MusicaIn):
    obj = get_object_or_404(Musica, id=song_id)
    for attr, value in song.dict().items():
        setattr(obj, attr, value)
    obj.save()
    return 200, obj

@api.delete("/songs/{song_id}/",
            response={204: None, 404: ErrorSchema},
            tags=["Songs"],
            description="Delete a song by ID.")
def delete_song(request, song_id: int):
    obj = get_object_or_404(Musica, id=song_id)
    obj.delete()
    return 204, None