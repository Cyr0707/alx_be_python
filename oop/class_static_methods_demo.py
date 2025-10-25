class Calculator:
    """
    A simple calculator demonstrating the use of
    class methods and static methods in Python.
    """

    # Class attribute
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        """
        Static method to add two numbers.
        Does not access class or instance data.
        """
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """
        Class method to multiply two numbers.
        Accesses class-level attributes via 'cls'.
        """
        print(f"Calculation type: {cls.calculation_type}")
        return a * b
