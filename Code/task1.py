class VinylRecord:
    def __init__(self, album_name, artist, year):
        self.album_name = album_name
        self.artist = artist
        self.year = year

    def display_info(self):
        print(f"Album: {self.album_name}\nArtist: {self.artist}\nYear: {self.year}")

vinyl = VinylRecord(album_name="The Dark Side of the Moon", artist="Pink Floyd", year=1973)
vinyl.display_info()
