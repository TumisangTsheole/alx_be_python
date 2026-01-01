class Book:
    """Represents a book with a title, author, and availability status."""
    def __init__(self, title, author):
        self.title = title
        self.author = author
        # Private attribute to track availability
        self._is_checked_out = False

    def check_out(self):
        """Marks the book as checked out."""
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False

    def return_book(self):
        """Marks the book as available."""
        self._is_checked_out = False

class Library:
    """Manages a collection of Book instances."""
    def __init__(self):
        # Private list to store Book objects
        self._books = []

    def add_book(self, book):
        """Adds a Book instance to the library."""
        self._books.append(book)

    def check_out_book(self, title):
        """Finds a book by title and checks it out."""
        for book in self._books:
            if book.title == title and not book._is_checked_out:
                book.check_out()
                return
        print(f"Sorry, '{title}' is not available.")

    def return_book(self, title):
        """Finds a book by title and returns it."""
        for book in self._books:
            if book.title == title:
                book.return_book()
                return

    def list_available_books(self):
        """Prints all books that are not currently checked out."""
        available_books = [book for book in self._books if not book._is_checked_out]
        if not available_books:
            print("No books available.")
        else:
            for book in available_books:
                print(f"{book.title} by {book.author}")
