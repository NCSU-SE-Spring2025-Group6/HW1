def calculate_average(numbers):
    total = sum(numbers)
    count = len(numbers)
    average = total / count
    return average

# Intentionally passing a string instead of a list of numbers
result = calculate_average([1,2,3,4,5,6,7,8,9,10])
print("The average is:", result)

if result > 5:
    print("The average is greater than 5")