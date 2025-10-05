# test_simple_calculator.py

import unittest
from simple_calculator import SimpleCalculator 

class TestSimpleCalculator(unittest.TestCase):
    """
    Unit tests for the SimpleCalculator class, covering all arithmetic operations.
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
        self.assertEqual(self.calc.add(100, 200), 300)

        # Negative Integers
        self.assertEqual(self.calc.add(-5, -3), -8)

        # Mixed Integers
        self.assertEqual(self.calc.add(-1, 5), 4)
        self.assertEqual(self.calc.add(10, -5), 5)
        
        # Floats
        self.assertAlmostEqual(self.calc.add(2.5, 3.5), 6.0)
        
        # With Zero
        self.assertEqual(self.calc.add(10, 0), 10)

    # ------------------------------------------------------
    # Test Cases for subtract() - Consolidated into one method
    # ------------------------------------------------------

    def test_subtraction(self):
        """Test the subtraction method with various scenarios (positive, negative result, zero, float)."""
        # Positive Result
        self.assertEqual(self.calc.subtract(10, 4), 6)
        
        # Negative Result
        self.assertEqual(self.calc.subtract(5, 15), -10)
        self.assertEqual(self.calc.subtract(-10, 5), -15)

        # With Zero
        self.assertEqual(self.calc.subtract(10, 0), 10)
        self.assertEqual(self.calc.subtract(0, 5), -5)
        
        # Floats
        self.assertAlmostEqual(self.calc.subtract(5.5, 2.2), 3.3)
        self.assertAlmostEqual(self.calc.subtract(10.0, 3.3), 6.7)

    # ------------------------------------------------------
    # Test Cases for multiply()
    # ------------------------------------------------------
    
    def test_multiplication_positive_integers(self):
        """Test multiplication of two positive integers."""
        self.assertEqual(self.calc.multiply(4, 5), 20)

    def test_multiplication_with_negative(self):
        """Test multiplication involving negative numbers."""
        self.assertEqual(self.calc.multiply(-4, 5), -20)
        self.assertEqual(self.calc.multiply(-4, -5), 20)
        
    def test_multiplication_by_zero(self):
        """Test multiplication where one operand is zero (should result in 0)."""
        self.assertEqual(self.calc.multiply(100, 0), 0)

    def test_multiplication_floats(self):
        """Test multiplication with floating-point numbers."""
        self.assertAlmostEqual(self.calc.multiply(1.5, 2.0), 3.0)
        
    # ------------------------------------------------------
    # Test Cases for divide()
    # ------------------------------------------------------

    def test_division_normal_operation(self):
        """Test division resulting in an integer."""
        self.assertEqual(self.calc.divide(10, 5), 2.0)
        
    def test_division_float_result(self):
        """Test division resulting in a float."""
        self.assertEqual(self.calc.divide(10, 4), 2.5)

    def test_division_by_zero_edge_case(self):
        """Test the specific edge case where the denominator is zero. 
           The class implementation dictates it should return None.
        """
        self.assertIsNone(self.calc.divide(10, 0))
        
    def test_division_zero_by_nonzero(self):
        """Test division of zero by a non-zero number (should result in 0)."""
        self.assertEqual(self.calc.divide(0, 5), 0.0)
        
    def test_division_with_negative_numbers(self):
        """Test division involving negative numbers."""
        self.assertEqual(self.calc.divide(-10, 5), -2.0)


if __name__ == '__main__':
    unittest.main()
