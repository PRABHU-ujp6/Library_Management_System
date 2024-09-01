# import pytest
from library import Library, Book


# @pytest.fixture
# def library():
#     return Library()
# @pytest.fixture
# def sample_books():
    
#     book1 = Book(1234, "To Kill a Mockingbird", "Harper Lee", 1960),
#     book2 = Book(1234567890, "The Great Gatsby", "F. Scott Fitzgerald", 1925)
    
#     return [book1, book2]
    
# def test_add_book_success(library, sample_books):
#     for book in sample_books:
#         library.add_books(book)
#     assert len(library.books) == 2
#     for book in sample_books:
#         assert library.books[book.isbn] == book

# def test_add_book():
#     library = Library()
#     book1 = Book(123, "The Hitchhiker's Guide to the Galaxy", "Douglas Adams", 1979)
#     library.add_books(book1)
#     assert len(library.books) == 1