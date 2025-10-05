# test_simple_calculator.py

import unittest
# Assuming simple_calculator.py is in the same directory
from simple_calculator import SimpleCalculator 

class TestSimpleCalculator(unittest.TestCase):
    """
    Unit tests for the SimpleCalculator class, covering all arithmetic operations.
    """

    def setUp(self):
        """
        Set up the SimpleCalculator instance before each test method is run.
        This ensures each test starts with a fresh calculator object.
        """
        self.calc = SimpleCalculator()

    # ------------------------------------------------------
    # Test Cases for add()
    # ------------------------------------------------------

    def test_addition_positive_integers(self):
        """Test addition with two positive integers."""
        self.assertEqual(self.calc.add(5, 3), 8)
        self.assertEqual(self.calc.add(100, 200), 300)

    def test_addition_negative_integers(self):
        """Test addition with two negative integers."""
        self.assertEqual(self.calc.add(-5, -3), -8)
        self.assertEqual(self.calc.add(-10, -100), -110)

    def test_addition_mixed_integers(self):
        """Test addition with positive and negative integers."""
        self.assertEqual(self.calc.add(-1, 5), 4)
        self.assertEqual(self.calc.add(10, -5), 5)

    def test_addition_floats(self):
        """Test addition with floating-point numbers."""
        # Use assertAlmostEqual for float comparison to avoid precision errors
        self.assertAlmostEqual(self.calc.add(2.5, 3.5), 6.0)
        self.assertAlmostEqual(self.calc.add(0.1, 0.2), 0.3)
        
    def test_addition_with_zero(self):
        """Test addition where one operand is zero."""
        self.assertEqual(self.calc.add(10, 0), 10)
        self.assertEqual(self.calc.add(0, -5), -5)

    # ------------------------------------------------------
    # Test Cases for subtract()
    # ------------------------------------------------------

    def test_subtraction_positive_integers(self):
        """Test subtraction resulting in a positive number."""
        self.assertEqual(self.calc.subtract(10, 4), 6)

    def test_subtraction_negative_result(self):
        """Test subtraction resulting in a negative number."""
        self.assertEqual(self.calc.subtract(5, 15), -10)
        
    def test_subtraction_with_zero(self):
        """Test subtraction involving zero."""
        self.assertEqual(self.calc.subtract(10, 0), 10)
        self.assertEqual(self.calc.subtract(0, 5), -5)
        self.assertEqual(self.calc.subtract(-5, 0), -5)
        
    def test_subtraction_floats(self):
        """Test subtraction with floating-point numbers."""
        self.assertAlmostEqual(self.calc.subtract(5.5, 2.2), 3.3)
        self.assertAlmostEqual(self.calc.subtract(10, 3.33), 6.67)

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
        self.assertEqual(self.calc.multiply(0, -5), 0)

    def test_multiplication_floats(self):
        """Test multiplication with floating-point numbers."""
        self.assertAlmostEqual(self.calc.multiply(1.5, 2.0), 3.0)
        self.assertAlmostEqual(self.calc.multiply(0.5, 0.5), 0.25)
        
    # ------------------------------------------------------
    # Test Cases for divide()
    # ------------------------------------------------------

    def test_division_normal_operation(self):
        """Test division resulting in an integer."""
        self.assertEqual(self.calc.divide(10, 5), 2.0)
        
    def test_division_float_result(self):
        """Test division resulting in a float."""
        self.assertEqual(self.calc.divide(10, 4), 2.5)

    def test_division_by_one(self):
        """Test division by 1."""
        self.assertEqual(self.calc.divide(5, 1), 5.0)

    def test_division_by_zero_edge_case(self):
        """Test the specific edge case where the denominator is zero. 
           The class implementation dictates it should return None.
        """
        self.assertIsNone(self.calc.divide(10, 0))
        self.assertIsNone(self.calc.divide(-5, 0))

    def test_division_zero_by_nonzero(self):
        """Test division of zero by a non-zero number (should result in 0)."""
        self.assertEqual(self.calc.divide(0, 5), 0.0)
        
    def test_division_with_negative_numbers(self):
        """Test division involving negative numbers."""
        self.assertEqual(self.calc.divide(-10, 5), -2.0)
        self.assertEqual(self.calc.divide(-10, -5), 2.0)
        self.assertEqual(self.calc.divide(10, -5), -2.0)


# This block allows the script to be run directly as a module
if __name__ == '__main__':
    unittest.main()
