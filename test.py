# Test file for calculator.py

import pytest
import subprocess
from calculator import add, subtract, multiply, divide  # noqa

# define a test function to test the add function


def test_add():
    # use subprocess to run the calculator app with arguments for adding 2 and 3
    result = subprocess.check_output(
        ['python', 'calculator.py', 'add', '2', '3'])
    # check that the output of the app is equal to the expected result
    assert int(result) == 5

# define a test function to test the subtract function


def test_subtract():
    result = subprocess.check_output(
        ['python', 'calculator.py', 'subtract', '10', '5'])
    assert int(result) == 5


# define a test function to test the multiply function
def test_multiply():
    result = subprocess.check_output(
        ['python', 'calculator.py', 'multiply', '2', '3'])
    assert int(result) == 6


# define a test function to test the divide function
def test_divide():
    result = subprocess.check_output(
        ['python', 'calculator.py', 'divide', '10', '2'])
    assert int(result) == 5

    # use subprocess to run the calculator app with arguments for dividing by 0
    with pytest.raises(ZeroDivisionError):
        # check that the app raises a ZeroDivisionError when dividing by 0
        subprocess.check_output(
            ['python', 'calculator.py', 'divide', '10', '0'])

    # use subprocess to run the calculator app with invalid arguments
    with pytest.raises(subprocess.CalledProcessError):
        # check that the app raises a CalledProcessError when invalid arguments are passed
        subprocess.check_output(
            ['python', 'calculator.py', 'invalid', '10', '2'])
