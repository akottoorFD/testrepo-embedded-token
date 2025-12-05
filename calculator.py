#!/usr/bin/env python3
"""
Basic Calculator App
Performs basic math operations via command-line arguments
"""

import sys
import argparse


def add(a, b):
    """Add two numbers"""
    return a + b


def subtract(a, b):
    """Subtract b from a"""
    return a - b


def multiply(a, b):
    """Multiply two numbers"""
    return a * b


def divide(a, b):
    """Divide a by b"""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def main():
    """Main function to parse arguments and perform calculations"""
    parser = argparse.ArgumentParser(
        description='Basic Calculator - Perform basic math operations',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s add 5 3
  %(prog)s subtract 10 4
  %(prog)s multiply 6 7
  %(prog)s divide 20 4
        """
    )
    
    parser.add_argument(
        'operation',
        choices=['add', 'subtract', 'multiply', 'divide'],
        help='The math operation to perform'
    )
    parser.add_argument(
        'num1',
        type=float,
        help='First number'
    )
    parser.add_argument(
        'num2',
        type=float,
        help='Second number'
    )
    
    args = parser.parse_args()
    
    # Map operation names to functions
    operations = {
        'add': add,
        'subtract': subtract,
        'multiply': multiply,
        'divide': divide
    }
    
    try:
        # Get the function and execute it
        operation_func = operations[args.operation]
        result = operation_func(args.num1, args.num2)
        print(f"{result}")
        return 0
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1
    except Exception as e:
        print(f"Unexpected error: {e}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
