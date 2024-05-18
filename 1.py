# Given 

input_array = [1, 3, 4, 5, 6, 7, 8, 9, 10]

n = len(input_array) + 1
sum_of_integers = (n * (n + 1)) // 2
sum_of_array_elements = sum(input_array)
missing_number = sum_of_integers - sum_of_array_elements
print("Missing Number:", missing_number)
