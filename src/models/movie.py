

class Movie:
    def __init__(self, id: int, name: str, img: str):
        self.id = id
        self.name = name
        self.img = img
    
    def __eq__(self, other):
        if not isinstance(other, Movie):
            return NotImplemented
        
        return self.id == other.id and self.name == other.name and self.img == self.img