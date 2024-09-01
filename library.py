class Book:
    
    def __init__(self, isbn, title, author, publication_year:int):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.publicaition_year = publication_year
        self.available = True
        

class Library:
    
    def __init__(self):
        
        self.books = {}
        
    def add_books(self, book): 
         
        if book.isbn in self.books:
            raise Exception("Book already exists..")
        else:
            self.books[book.isbn] = book
            print("book added successfully.")       
        
    def borrow_books(self, isbn):
        
        if isbn not in self.books:
            raise ValueError(f"Book with ISBN {isbn} not found")
        book = self.books[isbn]
        if not book.available:
            raise ValueError("Book is already borrowed")
        
        book.available = False
        print("Book borrowed successfully")
   
    def return_books(self, isbn):
        
        if isbn in self.books and not self.books[isbn].available:
            self.books[isbn].available = True
        elif isbn not in self.books:
            raise ValueError("Invalid ISBN : Book not Found.")
        else:
            raise Exception("Book was not borrowed")
    
#     def available_books(self):
        
#         return [book for book in self.books.values() if book.available]
    
#     def view_available_books(self):
        
#         available_books = self.available_books()
#         if available_books:
#             print("Available books in the library:")
#             for book in available_books:
#                 print(f"Book is {book.title} by {book.author} and ISBN: {book.isbn}")
#         else:
#             print("No books are available.")
    
# library = Library()

# book1 = Book(1234, "Two states", "Chetan Bhagat", "2010")

# library.add_books(book1)
# library.view_available_books()
# library.available_books()

            
        
        