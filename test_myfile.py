import pytest
from myfile import calculate_average

def test_calculate_average():
    assert calculate_average([1, 2, 3, 4, 5]) == 3
    assert calculate_average([10, 20, 30, 40, 50]) == 30
    assert calculate_average([1, 1, 1, 1, 1]) == 1
    assert calculate_average([1, 2, 3]) == 2

def test_calculate_average_empty_list():
    with pytest.raises(ZeroDivisionError):
        calculate_average([])

def test_calculate_average_invalid_input():
    with pytest.raises(TypeError):
        calculate_average("invalid input")

# # This test is expected to fail
# def test_calculate_average_failure():
#     # Incorrect assertion
#     assert calculate_average([1, 2, 3, 4, 5]) == 10  
