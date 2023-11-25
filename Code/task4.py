class VinylRecord:
    def __init__(self, album_name, artist, year, condition="Excellent"):
        self.album_name = album_name
        self.artist = artist
        self.year = year
        self.__condition = condition

    def display_info(self):
        print(f"Album: {self.album_name}\nArtist: {self.artist}\nYear: {self.year}\nCondition: {self.get_condition()}")

    def play(self):
        print(f"Now playing: {self.album_name} by {self.artist}")

    def get_condition(self):
        return self.__condition

    def set_condition(self, condition):
        self.__condition = condition

class ColoredVinylRecord(VinylRecord):
    def __init__(self, album_name, artist, year, condition="Excellent", color="Black"):
        super().__init__(album_name, artist, year, condition)
        self.__color = color

    def display_info(self):
        print(f"Album: {self.album_name}\nArtist: {self.artist}\nYear: {self.year}\nCondition: {self.get_condition()}\nColor: {self.get_color()}")

    def get_color(self):
        return self.__color

    def set_color(self, color):
        self.__color = color

colored_vinyl = ColoredVinylRecord(album_name="Abbey Road", artist="The Beatles", year=1969, color="Blue")
colored_vinyl.display_info()
print("Original Condition:", colored_vinyl.get_condition())
colored_vinyl.set_condition("Good")
print("Updated Condition:", colored_vinyl.get_condition())
