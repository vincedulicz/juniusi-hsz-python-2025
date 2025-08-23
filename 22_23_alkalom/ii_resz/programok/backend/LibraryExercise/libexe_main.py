def main():
    library = Library('data/books.json')

    new_book = Book('Hamvas Béla', 'A láthatatlan történet', 1988, '9630549085')
    library.add_book(new_book)

    another_book = Book('C.G. Jung', 'Emlékek, álmok, gondolatok', 1987, '9630743132')
    library.add_book(another_book)

    library.list_books()
    print("end list\n")

    library.sort_books_by_year()
    library.list_books()
    print("end sorting\n")

    books_by_author = library.get_books_by_author('Hamvas Béla')
    for book in books_by_author:
        print(f'{book.title} by {book.author}')

    print("end books by author\n")


main()
