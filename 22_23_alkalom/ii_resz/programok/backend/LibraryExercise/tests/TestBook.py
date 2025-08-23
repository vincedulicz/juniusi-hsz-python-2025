import unittest
from Book.Book import Book


class TestBook(unittest.TestCase):
    def test_book_initialization(self):
        """Test that a Book instance is correctly initialized."""
        book = Book(title="Test Title", author="Test Author", year=2025, isbn="1234567890")
        self.assertEqual(book.title, "Test Title")
        self.assertEqual(book.author, "Test Author")
        self.assertEqual(book.year, 2025)
        self.assertEqual(book.isbn, "1234567890")

    def test_to_dict(self):
        """Test that the to_dict method returns the correct dictionary."""
        book = Book(title="Test Title", author="Test Author", year=2025, isbn="1234567890")
        expected_dict = {
            'title': "Test Title",
            'author': "Test Author",
            'year': 2025,
            'isbn': "1234567890"
        }
        self.assertEqual(book.to_dict(), expected_dict)


if __name__ == "__main__":
    unittest.main()
