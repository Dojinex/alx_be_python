class Book:
    """A class representing a book in the library."""

    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False  # Private attribute

    def check_out(self):
        """Mark the book as checked out."""
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False

    def return_book(self):
        """Mark the book as returned."""
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False

    def is_available(self):
        """Check if the book is available."""
        return not self._is_checked_out


class Library:
    """A class to manage a collection of books."""

    def __init__(self):
        self._books = []  # Private list of Book objects

    def add_book(self, book):
        """Add a new book to the library."""
        self._books.append(book)

    def check_out_book(self, title):
        """Check out a book by title."""
        for book in self._books:
            if book.title == title:
                if book.check_out():
                    return True
                else:
                    print(f"'{title}' is already checked out.")
                    return False
        print(f"No book found with title '{title}'.")
        return False

    def return_book(self, title):
        """Return a book by title."""
        for book in self._books:
            if book.title == title:
                if book.return_book():
                    return True
                else:
                    print(f"'{title}' was not checked out.")
                    return False
        print(f"No book found with title '{title}'.")
        return False

    def list_available_books(self):
        """Print all available books in the library."""
        available = [book for book in self._books if book.is_available()]

        if not available:
            print("No available books.")
            return

        for book in available:
            print(f"{book.title} by {book.author}")
