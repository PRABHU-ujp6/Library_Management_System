import pytest
from library import Library, Book


def test_add_book():
    library = Library()
    book1 = Book(123, "The Hitchhiker's Guide to the Galaxy", "Douglas Adams", 1979)
    library.add_books(book1)
    assert len(library.books) == 1

def test_already_added():
    library = Library()
    book1 = Book(123, "The Hitchhiker's Guide to the Galaxy", "Douglas Adams", 1979)
    library.add_books(book1)
    book2 = Book(123, "My Will", "Louis Mark", 1980)
    with pytest.raises(Exception, match="Book already exists.."):
        library.add_books(book2)
    
    
def test_add_book_missing_info():
    with pytest.raises(TypeError):
        Book(846, "Anonymous Book", "Author UJP")


def test_add_multiple_books():
    library = Library()
    book1 = Book("1234567890", "The Great Gatsby", "F. Scott Fitzgerald", 1925)
    book2 = Book("0987654321", "To Kill a Mockingbird", "Harper Lee", 1960)
    book3 = Book("1122334455", "1984", "George Orwell", 1949)
    library.add_books(book1)
    library.add_books(book2)
    library.add_books(book3)
    
    assert len(library.books) == 3
    
    assert library.books["1234567890"].title == "The Great Gatsby"
    assert library.books["0987654321"].title == "To Kill a Mockingbird"
    assert library.books["1122334455"].title == "1984"
    
# @pytest.mark.parametrize("isbn, title, author, publication_year", [
#     ("1111111111", "Book One", "Author A", 2000),
#     ("2222222222", "Book Two", "Author B", 2010),
#     ("3333333333", "Book Three", "Author C", 2020),
# ])
# def test_add_multiple_unique_books(isbn, title, author, publication_year):
#     library = Library()
#     book = Book(isbn, title, author, publication_year)
#     library.add_books(book)
#     assert library.books[isbn] == book

# def test_borrow_book():
#     library = Library()
#     book1 = Book(1234, "Two states", "Chetan Bhagat", "2010")
#     library.add_books(book1)
#     library.borrow_books(book1.isbn)
#     assert not library.books[book1.isbn].available
   
# def test_borrow_book_not_available():
#     library = Library()
#     book1 = Book(1234, "Two states", "Chetan Bhagat", "2010")
#     library.add_books(book1)
#     library.borrow_books(book1.isbn)
#     with pytest.raises(Exception):
#         library.borrow_books("XYZ Books") 

# def test_borrow_nonexistent_book():
#     library = Library()
    
#     with pytest.raises(Exception):
#         library.borrow_books("XYZ Books") 
        

# def test_borrow_invalid_isbn():
#     library = Library()
#     book1 = Book(1234, "Two states", "Chetan Bhagat", "2010")
#     library.add_books(book1)
    
#     with pytest.raises(ValueError):
#         library.borrow_books("XYZ books")
        
# def test_borrow_book_multiple_times():
#     library = Library()
#     book = Book("1234567890", "The Hitchhiker's Guide to the Galaxy", "Douglas Adams", 1979)
#     library.add_books(book)
#     library.borrow_books(book.isbn)
#     with pytest.raises(ValueError):
#         library.borrow_books(book.isbn)
    
# def test_return_book():
#     library = Library()
#     book1 = Book(1234, "Two states", "Chetan Bhagat", "2010")
#     library.add_books(book1)
#     library.borrow_books(book1.isbn)
#     library.return_books(book1.isbn)
#     assert library.books[book1.isbn].available

# def test_return_book_not_borrowed():
#     library = Library()
#     book1 = Book(1234, "Two states", "Chetan Bhagat", "2010")
#     library.add_books(book1)
#     with pytest.raises(Exception):
#         library.return_books(book1.isbn)
#     assert "was not borrowed"
    
# def test_return_nonexistent_book():
#     library = Library()
    
#     with pytest.raises(Exception):
#         library.return_books("XYZ Books")
#     assert "Not exists"
    
# def test_return_invalid_isbn():
#     library = Library()
    
#     with pytest.raises(ValueError, match="Invalid ISBN : Book not Found."):
#         library.return_books("Invalid ISBN")

# def test_available_books_empty():
#     library = Library()
    
#     available = library.available_books()
#     assert available == []
    
# def test_all_available_books():
#     library = Library()
#     book1 = Book(1234, "Two States", "Chetan Bhagat", 2010)
#     book2 = Book(987654321, "To Kill a Mockingbird", "Harper Lee", 1960)
#     book3 = Book(1122334455, "1984", "George Orwell", 1949)
#     library.add_books(book1)
#     library.add_books(book2)
#     library.add_books(book3)
#     book2.available = False
#     all_available_books = library.available_books()
#     assert book1 in all_available_books
#     assert book3 in all_available_books
#     assert book2 not in all_available_books
    
# def test_view_available_books_borrowed():
#     library = Library()
#     book1 = Book("1234567890", "The Hitchhiker's Guide to the Galaxy", "Douglas Adams", 1979)
#     book2 = Book("9876543210", "The Lord of the Rings", "J.R.R. Tolkien", 1954)
#     library.add_books(book1)
#     library.add_books(book2)
#     library.borrow_books(book1.isbn)
#     all_available_books = library.available_books()
#     assert len(all_available_books) == 1
#     assert book2 in all_available_books

# def test_view_available_books_output(capfd):
#     library = Library()
#     book1 = Book(1234, "Two States", "Chetan Bhagat", 2010)
#     book2 = Book(9876, "The Lord of the Rings", "J.R.R. Tolkien", 1954)
#     library.add_books(book1)
#     library.add_books(book2)
#     library.view_available_books()
#     out, err = capfd.readouterr()
#     print("Captured output before borrowing:", out)
#     assert "Available books in the library" in out
#     assert f"{book1.title} by {book1.author} and ISBN: {book1.isbn}" in out
#     assert f"{book2.title} by {book2.author} and ISBN: {book2.isbn}" in out 
#     library.borrow_books(1234)
#     assert not library.books[1234].available, "Book should be marked as borrowed"
#     library.view_available_books()
#     out, err = capfd.readouterr()
#     print("Captured output after borrowing:", out)
#     assert f"{book1.title} by {book1.author} and ISBN: {book1.isbn}" in out
#     assert f"{book2.title} by {book2.author} and ISBN: {book2.isbn}" in out
    
# def test_borrow_and_return_multiple_books():
#     library = Library()
#     book1 = Book("1234567890", "The Great Gatsby", "F. Scott Fitzgerald", 1925)
#     book2 = Book("0987654321", "To Kill a Mockingbird", "Harper Lee", 1960)
#     book3 = Book("1122334455", "1984", "George Orwell", 1949)
#     library.add_books(book1)
#     library.add_books(book2)
#     library.add_books(book3)
#     library.borrow_books("1234567890")
#     library.borrow_books("0987654321")
#     available = library.available_books()
#     assert len(available) == 1
#     assert available[0].isbn == "1122334455"
#     library.return_books("1234567890")
#     available = library.available_books()
#     assert len(available) == 2
#     isbns_available = [book.isbn for book in available]
#     assert "1234567890" in isbns_available
#     assert "1122334455" in isbns_available
    
