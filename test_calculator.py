#!/usr/bin/env python3
"""
Test suite for Basic Calculator App
"""

import unittest
import sys
from io import StringIO
from calculator import add, subtract, multiply, divide, main


class TestCalculatorFunctions(unittest.TestCase):
    """Test individual calculator functions"""
    
    def test_add(self):
        """Test addition function"""
        self.assertEqual(add(5, 3), 8)
        self.assertEqual(add(-5, 3), -2)
        self.assertEqual(add(0, 0), 0)
        self.assertEqual(add(1.5, 2.5), 4.0)
    
    def test_subtract(self):
        """Test subtraction function"""
        self.assertEqual(subtract(10, 4), 6)
        self.assertEqual(subtract(5, 10), -5)
        self.assertEqual(subtract(0, 0), 0)
        self.assertEqual(subtract(7.5, 2.5), 5.0)
    
    def test_multiply(self):
        """Test multiplication function"""
        self.assertEqual(multiply(6, 7), 42)
        self.assertEqual(multiply(-3, 4), -12)
        self.assertEqual(multiply(0, 100), 0)
        self.assertEqual(multiply(2.5, 4), 10.0)
    
    def test_divide(self):
        """Test division function"""
        self.assertEqual(divide(20, 4), 5)
        self.assertEqual(divide(10, 2), 5)
        self.assertEqual(divide(7, 2), 3.5)
        self.assertEqual(divide(-10, 2), -5)
    
    def test_divide_by_zero(self):
        """Test division by zero raises ValueError"""
        with self.assertRaises(ValueError) as context:
            divide(10, 0)
        self.assertIn("Cannot divide by zero", str(context.exception))


class TestCalculatorCLI(unittest.TestCase):
    """Test command-line interface"""
    
    def run_calculator(self, args):
        """Helper method to run calculator with given arguments"""
        # Save original argv and stdout
        original_argv = sys.argv
        original_stdout = sys.stdout
        
        try:
            # Set up test arguments and capture output
            sys.argv = ['calculator.py'] + args
            sys.stdout = StringIO()
            
            # Run main function
            exit_code = main()
            output = sys.stdout.getvalue()
            
            return exit_code, output
        finally:
            # Restore original argv and stdout
            sys.argv = original_argv
            sys.stdout = original_stdout
    
    def test_add_command(self):
        """Test add command via CLI"""
        exit_code, output = self.run_calculator(['add', '5', '3'])
        self.assertEqual(exit_code, 0)
        self.assertIn('8', output.strip())
    
    def test_subtract_command(self):
        """Test subtract command via CLI"""
        exit_code, output = self.run_calculator(['subtract', '10', '4'])
        self.assertEqual(exit_code, 0)
        self.assertIn('6', output.strip())
    
    def test_multiply_command(self):
        """Test multiply command via CLI"""
        exit_code, output = self.run_calculator(['multiply', '6', '7'])
        self.assertEqual(exit_code, 0)
        self.assertIn('42', output.strip())
    
    def test_divide_command(self):
        """Test divide command via CLI"""
        exit_code, output = self.run_calculator(['divide', '20', '4'])
        self.assertEqual(exit_code, 0)
        self.assertIn('5', output.strip())
    
    def test_divide_by_zero_command(self):
        """Test divide by zero via CLI"""
        # Save original stderr
        original_stderr = sys.stderr
        
        try:
            sys.stderr = StringIO()
            exit_code, output = self.run_calculator(['divide', '10', '0'])
            error_output = sys.stderr.getvalue()
            
            self.assertEqual(exit_code, 1)
            self.assertIn("Cannot divide by zero", error_output)
        finally:
            sys.stderr = original_stderr
    
    def test_float_numbers(self):
        """Test calculator with floating point numbers"""
        exit_code, output = self.run_calculator(['add', '1.5', '2.5'])
        self.assertEqual(exit_code, 0)
        self.assertIn('4', output.strip())
    
    def test_negative_numbers(self):
        """Test calculator with negative numbers"""
        exit_code, output = self.run_calculator(['add', '-5', '3'])
        self.assertEqual(exit_code, 0)
        self.assertIn('-2', output.strip())


if __name__ == '__main__':
    unittest.main()
