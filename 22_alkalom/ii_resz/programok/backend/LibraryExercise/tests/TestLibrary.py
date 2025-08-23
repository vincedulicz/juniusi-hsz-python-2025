import unittest
import os
import json
from unittest.mock import patch
from Book.Book import Book
from Library.Library import Library


class TestLibrary(unittest.TestCase):
    def setUp(self):
        """Create a temporary file and initialize a Library instance."""
        self.test_file = 'test_books.json'
        with open(self.test_file, 'w') as file:
            json.dump([], file)
        self.library = Library(self.test_file)

    def tearDown(self):
        """Remove the temporary file after each test."""
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_load_books_empty_file(self):
        """Test loading books from an empty file."""
        self.assertEqual(len(self.library.books), 0)

    def test_add_book(self):
        """Test adding a book to the library."""
        book = Book(title="Test Book", author="Author", year=2025, isbn="1234567890")
        self.library.add_book(book)
        self.assertEqual(len(self.library.books), 1)
        self.assertEqual(self.library.books[0].title, "Test Book")

    def test_remove_book(self):
        """Test removing a book from the library by ISBN."""
        book = Book(title="Test Book", author="Author", year=2025, isbn="1234567890")
        self.library.add_book(book)
        self.library.remove_book("1234567890")
        self.assertEqual(len(self.library.books), 0)

    def test_list_books(self):
        """Test listing books in the library."""
        book = Book(title="Test Book", author="Author", year=2025, isbn="1234567890")
        self.library.add_book(book)

        # with self.assertLogs() as captured:
        #    self.library.list_books()
        # self.assertIn("Test Book by Author (2025)", captured.output[0])

        with patch('builtins.print') as mocked_print:
            self.library.list_books()
            mocked_print.assert_called_once_with("Test Book by Author (2025)")

    def test_sort_books_by_year(self):
        """Test sorting books by year."""
        book1 = Book(title="Book One", author="Author", year=2021, isbn="111")
        book2 = Book(title="Book Two", author="Author", year=2020, isbn="222")
        self.library.add_book(book1)
        self.library.add_book(book2)
        self.library.sort_books_by_year()
        self.assertEqual(self.library.books[0].year, 2020)

    def test_get_books_by_author(self):
        """Test getting books by a specific author."""
        book1 = Book(title="Book One", author="Author A", year=2021, isbn="111")
        book2 = Book(title="Book Two", author="Author B", year=2020, isbn="222")
        self.library.add_book(book1)
        self.library.add_book(book2)
        books_by_author_a = self.library.get_books_by_author("Author A")
        self.assertEqual(len(books_by_author_a), 1)
        self.assertEqual(books_by_author_a[0].author, "Author A")


if __name__ == "__main__":
    unittest.main()
