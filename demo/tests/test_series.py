import pytest 
from series.series import fibonacci
from series.series import lucas
from series.series import sum_series


############  Fibonacci  ############
''' Sample: 0, 1, 1, 2, 3, 5, 8, 13, ...'''

def test_fibonacci_zero():
    actual = fibonacci(0)
    expected = 0
    assert actual == expected
    
def test_fibonacci_two():
    actual = fibonacci(2)
    expected = 1
    assert actual == expected

def test_fibonacci_seven():
    actual = fibonacci(7)
    expected = 13
    assert actual == expected

# @pytest.mark.skip(reason="Skipping this test for now")
def test_fibonacci_string():
    actual = fibonacci("7")
    expected = "The input is not an integer!"
    assert actual == expected
    
############  Lucas numbers  ############
''' Sample: 2, 1, 3, 4, 7, 11, 18, 29, ...'''
# @pytest.mark.skip(reason="Skipping this test for now")
def test_lucas_zero():
    actual = lucas(0)
    expected = 2
    assert actual == expected

def test_lucas_one():
    actual = lucas(1)
    expected = 1
    assert actual == expected

def test_lucas_three():
    actual = lucas(3)
    expected = 4
    assert actual == expected

def test_lucas_five():
    actual = lucas(5)
    expected = 11
    assert actual == expected
    
############  Sum series  ############
''' sample: 0, 1, 1, 2, 3, 5, 8, 13, ...'''
''' Sample: 2, 1, 3, 4, 7, 11, 18, 29, ...'''
''' sample: 4, 5, 9, 14, 23, 37, 60, 97, ...'''

# @pytest.mark.skip(reason="Skipping this test for now")

def test_sum_series_zero_fibonacci():
    actual = sum_series(5,0,1)
    expected = 5
    assert actual == expected

def test_sum_series_five_lucas():
    actual = sum_series(5,2,1)
    expected = 11
    assert actual == expected

def test_sum_series_seven():
    actual = sum_series(7,4,5)
    expected = 97
    assert actual == expected

def test_sum_series_six():
    actual = sum_series(6,4,5)
    expected = 60
    assert actual == expected
    