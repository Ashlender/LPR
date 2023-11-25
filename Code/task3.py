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

class ColoredVinylRecord(VinylRecord):
    def __init__(self, album_name, artist, year, condition="Excellent", color="Black"):
        super().__init__(album_name, artist, year, condition)
        self.color = color

    def display_info(self):
        print(f"Album: {self.album_name}\nArtist: {self.artist}\nYear: {self.year}\nCondition: {self.condition}\nColor: {self.color}")

colored_vinyl = ColoredVinylRecord(album_name="Abbey Road", artist="The Beatles", year=1969, color="Blue")
colored_vinyl.display_info()
colored_vinyl.play()
