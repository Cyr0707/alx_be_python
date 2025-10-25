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
        String Representation: Returns a user-friendly string format.
        This is used by print() and str().
        """
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self) -> str:
        """
        Official Representation: Returns an unambiguous string that can 
        be used to recreate the object.
        This is used by repr().
        """
        return f"Book('{self.title}', '{self.author}', {self.year})"

    def __del__(self):
        """
        Destructor: Called when the object is about to be destroyed (deleted).
        Prints a cleanup message.
        """
        # The destructor is called when the reference count of the object drops to zero.
        print(f"Deleting {self.title}")

# Note: The provided main.py will handle the creation and testing.
