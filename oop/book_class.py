class Book:
    """
    Represents a book with a title, author, and publication year.
    Implements magic methods for initialization, destruction, and string representations.
    """
    
    def __init__(self, title: str, author: str, year: int):
        """
        Constructor: Initializes the Book instance.
        
        :param title: The title of the book (str).
        :param author: The author of the book (str).
        :param year: The publication year (int).
        """
        self.title = title
        self.author = author
        self.year = year
        print(f"Book '{self.title}' created.")

    def __str__(self) -> str:
        """
        String Representation (__str__): Returns a user-friendly string format.
        Format: "(title) by (author), published in (year)"
        This is used by print() and str().
        """
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self) -> str:
        """
        Official Representation (__repr__): Returns an unambiguous string that 
        can be used to recreate the object.
        Format: "Book('(title)', '(author)', (year))"
        This is used by repr().
        """
        # Note the use of quotes around title and author to make it a valid constructor call
        return f"Book('{self.title}', '{self.author}', {self.year})"

    def __del__(self):
        """
        Destructor (__del__): Called when the object is about to be destroyed.
        Prints a cleanup message.
        """
        print(f"Deleting {self.title}")
