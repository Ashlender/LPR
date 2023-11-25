class VinylRecord:
    def __init__(self, album_name, artist, year, condition="Excellent"):
        self.album_name = album_name
        self.artist = artist
        self.year = year
        self.condition = condition

    def display_info(self):
        print(f"Album: {self.album_name}\nArtist: {self.artist}\nYear: {self.year}\nCondition: {self.condition}")

    def play(self):
        print(f"Now playing: {self.album_name} by {self.artist}")

vinyl = VinylRecord(album_name="The Dark Side of the Moon", artist="Pink Floyd", year=1973, condition="Good")
vinyl.display_info()
vinyl.play()
