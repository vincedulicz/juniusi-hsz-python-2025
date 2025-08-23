class Book:
    def __init__(self, title: str, author: str, year: int, isbn: str):
        # TODO: property (?)
        self.title = title
        self.author = author
        self.year = year
        self.isbn = isbn

    def to_dict(self):
        return {
            'title': self.title,
            'author': self.author,
            'year': self.year,
            'isbn': self.isbn
        }