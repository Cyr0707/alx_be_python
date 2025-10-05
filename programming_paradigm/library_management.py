class Book:
    """Represents a book in the library with a title, author, and availability status."""
    def __init__(self, title: str, author: str):
        # Public attributes
        self.title = title
        self.author = author
        # Private attribute to track availability
        self._is_checked_out = False 

    def check_out(self) -> bool:
        """Marks the book as checked out if it's currently available."""
        if not self._is_checked_out:
            self._is_checked_out = True
            return True  # Successful checkout
        return False # Already checked out

    def return_book(self) -> bool:
        """Marks the book as returned if it's currently checked out."""
        if self._is_checked_out:
            self._is_checked_out = False
            return True # Successful return
        return False # Already available

    def is_available(self) -> bool:
        """Returns the current availability status of the book."""
        return not self._is_checked_out

    def __str__(self):
        """String representation for the Book object."""
        return f"{self.title} by {self.author}"

class Library:
    """Manages a collection of Book objects."""
    def __init__(self):
        # Private list to store Book instances
        self._books = []

    def add_book(self, book: Book):
        """Adds a Book object to the library's collection."""
        self._books.append(book)
        print(f"Added book: {book.title}")

    def _find_book(self, title: str) -> Book or None:
        """Helper method to find a book by its title."""
        # Note: This simple implementation assumes unique titles for simplicity.
        for book in self._books:
            if book.title == title:
                return book
        return None

    def check_out_book(self, title: str):
        """Attempts to check out a book by title and updates its availability."""
        book = self._find_book(title)
        if book:
            if book.check_out():
                print(f"Successfully checked out: {title}")
            else:
                print(f"'{title}' is already checked out.")
        else:
            print(f"Error: Book with title '{title}' not found.")

    def return_book(self, title: str):
        """Attempts to return a book by title and updates its availability."""
        book = self._find_book(title)
        if book:
            if book.return_book():
                print(f"Successfully returned: {title}")
            else:
                # This should ideally not happen if logic is correct, but handles a book 
                # being returned when it was never checked out (i.e., _is_checked_out is False).
                print(f"'{title}' was not checked out.") 
        else:
            print(f"Error: Book with title '{title}' not found.")

    def list_available_books(self):
        """Prints the title and author of all currently available books."""
        available_count = 0
        for book in self._books:
            if book.is_available():
                print(book)
                available_count += 1
        
        if available_count == 0:
            print("No books are currently available.")
