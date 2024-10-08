# LIBRARY MANAGEMENT SYSTEM

A simple library management system implemented in Python using Test-Driven Development (TDD). This project allows users to perform basic operations such as adding books, borrowing books, returning books, and viewing available books. 

## Features

- **Add books :** Users can add new books to the library with details like ISBN, title, author, and publication year.

- **Borrow Books :** Users can borrow books if they are available in the library.

- **Return Books :** Users can return borrowed books, making them available for others.

- **View Availability Books :** Users can view a list of all available books in the library.

## Requirements

- **Python 3.8+**
- **pip** (python package installer)
- **pytest** (for running test)

## Project Structure
```
Library_management_system
|
|__src/
|   |__library.py
|
|__test/
|   |__test_library.py
|
|__README.md
```
or 
you can make simple
```
Library_management_system
|
|___library.py
|
|___test_library.py
|
|__README.md
```

## Setup and Installation

### 1. Clone the Repository
```
git clone <repository-URL>
cd library_management_system
```
### 2. Create and Activate a Virtual Environment (Optional)
```
python3 -m venv venv
On Windows use `venv\Scripts\activate`
```
### 3. Install Dependencies
```
pip install pytest
```
### Running the TEST
This project follows the Test-Driven Development (TDD) approach. All functionality is thoroughly tested using pytest.

To run all the tests, execute the following command:
```
pytest
```
or to test specific case:

```
python -m pytest test_filename.py::test_specific_testcase_function
```
here test_filename.py = your test file   test_specific_testcase_function = your corresponding testcase function

## USAGE
You can interact with the library management system by importing the **Library** and **Book** classes from the src.library module. Below is a simple example:
```
from src.library import Library, Book

# Create a new library instance
library = Library()

# Add books to the library
book1 = Book("1234567890", "The Great Gatsby", "F. Scott Fitzgerald", 1925)
library.add_books(book1)

# Borrow a book
library.borrow_books("1234567890")

# Return a book
library.return_books("1234567890")

# View available books
available_books = library.available_books()
for book in available_books:
    print(f"{book.title} by {book.author}")
```
## Version Control and TDD Process
This project uses Git for version control. The development process follows Test-Driven Development (TDD), where tests are written before implementing the functionality. Each step in the development process is committed with meaningful commit messages, reflecting the progress of TDD.

### Example Git Commands

1. Create a new repository:
    ```
    git init
    ```
2. Add and commit changes:
    ```
    git add .
    git commit -m "Add feature or commit change..."
    ```
3. Push changes to remote repository:
    ```
    git branch -m main
    git remote add origin <repository-url>
    git push -u origin main

## Contribution
Contributions are welcome! Please ensure that any new features or changes are accompanied by corresponding tests and follow clean coding practices.

1. Fork the repository.  
2. Create a new branch (```git checkout -b feature/YourFeature```).  
3. Create a new branch (```git checkout -b feature/YourFeature```).  
4. Push to the branch (```git push origin feature/YourFeature```).  
5. Create a new Pull Request.

## TESTCASE REPORT

[Report PDF Here](ReportTestCase.pdf)
