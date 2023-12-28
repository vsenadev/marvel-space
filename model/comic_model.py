class ComicModel:
    def __init__(self, title: str, issue_number: int, publication_date: str, characters: list, writers: list):
        self.title = title
        self.issue_number = issue_number
        self.publication_date = publication_date
        self.characters = characters
        self.writers = writers
