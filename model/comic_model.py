class ComicModel:
    def __init__(self, name: str, number: int, initial_final: str, launch: str, description: str, creators: list, image: str):
        self.name = name
        self.number = number
        self.initial_final = initial_final
        self.launch = launch
        self.description = description
        self.creators = creators
        self.image = image
