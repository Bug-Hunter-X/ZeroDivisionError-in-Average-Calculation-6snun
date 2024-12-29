def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list
    return sum(numbers) / len(numbers)

# Example usage:
my_numbers = [10, 20, 30, 40, 50]
average = calculate_average(my_numbers)
print(f"The average is: {average}")

empty_list = []
average_empty = calculate_average(empty_list)
print(f"The average of an empty list is: {average_empty}") 