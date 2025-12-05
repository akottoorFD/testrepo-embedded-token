# testrepo-embedded-token

A basic calculator app written in Python that accepts command-line arguments to perform basic math operations.

## Features

- Addition
- Subtraction
- Multiplication
- Division (with divide-by-zero protection)
- Support for integers and floating-point numbers
- Support for negative numbers

## Usage

Run the calculator with the following command format:

```bash
python3 calculator.py <operation> <num1> <num2>
```

### Examples

```bash
# Addition
python3 calculator.py add 5 3
# Output: 8.0

# Subtraction
python3 calculator.py subtract 10 4
# Output: 6.0

# Multiplication
python3 calculator.py multiply 6 7
# Output: 42.0

# Division
python3 calculator.py divide 20 4
# Output: 5.0

# Works with floats
python3 calculator.py add 1.5 2.5
# Output: 4.0

# Works with negative numbers
python3 calculator.py multiply -3 4
# Output: -12.0
```

### Available Operations

- `add` - Add two numbers
- `subtract` - Subtract the second number from the first
- `multiply` - Multiply two numbers
- `divide` - Divide the first number by the second

### Help

To see all available options:

```bash
python3 calculator.py --help
```

## Testing

Run the test suite to verify the calculator works correctly:

```bash


python3 -m unittest test_calculator.py -v
```
fdc_00239_2346693w4292834
