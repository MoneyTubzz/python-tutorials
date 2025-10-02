def calculate_average(numbers):
    if len(numbers) == 0:
        return 0
    
    avg = sum(numbers) / len(numbers)
    return avg

nums = [10, 20, 30, 40, 50]
average = calculate_average(nums)
print(f"The average of {nums} is {average}")