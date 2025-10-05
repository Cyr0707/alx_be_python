# test_simple_calculator.py

import unittest
from simple_calculator import SimpleCalculator 

class TestSimpleCalculator(unittest.TestCase):
    """
    Unit tests for the SimpleCalculator class, ensuring all methods are tested
    with various scenarios, including consolidation of tests per method.
    """

    def setUp(self):
        """
        Set up the SimpleCalculator instance before each test method is run.
        """
        self.calc = SimpleCalculator()

    # ------------------------------------------------------
    # Test Cases for add() - Consolidated
    # ------------------------------------------------------

    def test_addition(self):
        """Test the addition method with various scenarios (positive, negative, zero, float)."""
        # Positive Integers
        self.assertEqual(self.calc.add(5, 3), 8)

        # Negative Integers
        self.assertEqual(self.calc.add(-5, -3), -8)

        # Mixed Integers
        self.assertEqual(self.calc.add(-1, 5), 4)
        
        # Floats
        self.assertAlmostEqual(self.calc.add(2.5, 3.5), 6.0)
        
        # With Zero
        self.assertEqual(self.calc.add(10, 0), 10)

    # ------------------------------------------------------
    # Test Cases for subtract() - Consolidated
    # ------------------------------------------------------

    def test_subtraction(self):
        """Test the subtraction method with various scenarios (positive, negative result, zero, float)."""
        # Positive Result
        self.assertEqual(self.calc.subtract(10, 4), 6)
        
        # Negative Result
        self.assertEqual(self.calc.subtract(5, 15), -10)

        # With Zero
        self.assertEqual(self.calc.subtract(10, 0), 10)
        
        # Floats
        self.assertAlmostEqual(self.calc.subtract(5.5, 2.2), 3.3)

    # ------------------------------------------------------
    # Test Cases for multiply() - Consolidated into one method
    # ------------------------------------------------------
    
    def test_multiplication(self):
        """Test the multiplication method with various scenarios (positive, negative, zero, float)."""
        # Positive Integers
        self.assertEqual(self.calc.multiply(4, 5), 20)

        # Negative Numbers
        self.assertEqual(self.calc.multiply(-4, 5), -20)
        self.assertEqual(self.calc.multiply(-4, -5), 20)
        
        # By Zero
        self.assertEqual(self.calc.multiply(100, 0), 0)

        # Floats
        self.assertAlmostEqual(self.calc.multiply(1.5, 2.0), 3.0)
        
    # ------------------------------------------------------
    # Test Cases for divide() - Consolidated into one method
    # ------------------------------------------------------

    def test_division(self):
        """Test the division method, covering normal, float, zero, and the division-by-zero edge case."""
        # Normal Division
        self.assertEqual(self.calc.divide(10, 5), 2.0)
        
        # Float Result
        self.assertEqual(self.calc.divide(10, 4), 2.5)

        # Division by Zero (Edge Case)
        self.assertIsNone(self.calc.divide(10, 0))
        
        # Zero by Non-zero
        self.assertEqual(self.calc.divide(0, 5), 0.0)
        
        # With Negative Numbers
        self.assertEqual(self.calc.divide(-10, 5), -2.0)


if __name__ == '__main__':
    unittest.main()
