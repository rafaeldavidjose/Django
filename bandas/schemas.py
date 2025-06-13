from ninja import Schema
from typing import Optional
from datetime import timedelta

class ErrorSchema(Schema):
    detail: str


class BandaIn(Schema):
    nome: str
    ano_criacao: int
    nacionalidade: str
    descricao: Optional[str] = None
    foto_banda: Optional[str] = None

class BandaOut(BandaIn):
    id: int

class AlbumIn(Schema):
    nome: str
    banda_id: int
    ano_lancamento: int
    capa: Optional[str] = None

class AlbumOut(AlbumIn):
    id: int

class MusicaIn(Schema):
    nome: str
    banda_id: int
    album_id: int
    duracao: timedelta
    link: Optional[str] = None
    letra: Optional[str] = None

class MusicaOut(MusicaIn):
    id: int
    
class BandaComAlbuns(BandaOut):
    albuns: list[AlbumOut]
    
class AlbumComMusicas(AlbumOut):
    musicas: list[MusicaOut]
    
class MusicaComBandaEAlbum(MusicaOut):
    banda: BandaOut
    album: AlbumOut