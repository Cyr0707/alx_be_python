class Book:
    """
    Base class representing a generic book.
    """

    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"Book: {self.title} by {self.author}"


class EBook(Book):
    """
    Derived class representing an electronic book.
    Inherits from Book and adds file_size (in KB).
    """

    def __init__(self, title, author, file_size):
        super().__init__(title, author)
        self.file_size = file_size

    def __str__(self):
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"


class PrintBook(Book):
    """
    Derived class representing a printed book.
    Inherits from Book and adds page_count.
    """

    def __init__(self, title, author, page_count):
        super().__init__(title, author)
        self.page_count = page_count

    def __str__(self):
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"


class Library:
    """
    Represents a library that contains multiple books.
    Demonstrates composition by containing a list of Book objects.
    """

    def __init__(self):
        self.books = []

    def add_book(self, book):
        """
        Adds a Book, EBook, or PrintBook instance to the library.
        """
        self.books.append(book)

    def list_books(self):
        """
        Prints details of each book in the library.
        """
        for book in self.books:
            print(book)
