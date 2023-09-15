class Song:
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}

    
    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        Song.add_song_to_count()
        Song.add_to_genres(genre)
        Song.add_to_artists(artist)
        Song.add_to_genre_count(genre)
        Song.add_to_artist_count(artist)

    @classmethod
    def add_song_to_count(cls):
        cls.count +=1

    @classmethod
    def add_to_genres(cls, genre):
        if genre not in cls.genres:
            cls.genres.append(genre)
            cls.genre_count[genre] = 0

    @classmethod
    def add_to_artists(cls, artist):
        if artist not in cls.artists:
            cls.artists.append(artist)
            cls.artist_count[artist] = 0

    @classmethod
    def add_to_genre_count(cls, genre):
        cls.genre_count[genre] += 1

    @classmethod
    def add_to_artist_count(cls, artist):
        cls.artist_count[artist] += 1

# song1 = Song("Song 1", "Artist 1", "Pop")
# song2 = Song("Song 2", "Artist 2", "Rock")
# song3 = Song("Song 3", "Artist 3", "Hip-Hop")
# song4 = Song("Song 4", "Artist 1", "Pop")
# song5 = Song("Song 5", "Artist 2", "Rock")
# import ipdb; ipdb.set_trace()