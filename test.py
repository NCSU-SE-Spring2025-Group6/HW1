from myfile import calculate_average

def test_should_fail():
  assert calculate_average([1,2,3]) == 1

def test_should_pass():
  assert calculate_average([1,2,3]) == 2
