from LibraryExercise.Book import Book

class Library:
    def __init__(self, filename: str):
        self.filename = filename
        self.books = self.load_books()

    def load_books(self) -> List[Book]:
        """Load books from a JSON file."""
        try:
            with open(self.filename, 'r') as file:
                data = json.load(file)
                return [Book(**book) for book in data]
        except FileNotFoundError:
            return []

    def save_books(self):
        """Save books to a JSON file."""
        with open(self.filename, 'w') as file:
            json.dump([book.to_dict() for book in self.books], file, indent=4)

    def add_book(self, book: Book):
        """Add a new book to the library."""
        self.books.append(book)
        self.save_books()

    def remove_book(self, isbn: str):
        """Remove a book by ISBN."""
        self.books = [book for book in self.books if book.isbn != isbn]
        self.save_books()

    def list_books(self):
        """Print all books."""
        for book in self.books:
            print(f'{book.title} by {book.author} ({book.year})')

    def sort_books_by_year(self):
        """Sort books by year."""
        self.books.sort(key=lambda book: book.year)

    def get_books_by_author(self, author: str):
        """Get all books by a given author."""
        return [book for book in self.books if book.author == author]