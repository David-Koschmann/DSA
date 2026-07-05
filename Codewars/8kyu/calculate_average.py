# Write a function which calculates the average of the numbers in a given array.

# Note: Empty arrays should return 0.

def find_average(numbers):
    sum = 0
    total_nums = len(numbers)
    
    for num in numbers:
        sum += num
    
    if numbers:
        return sum / total_nums
    else:
        return 0