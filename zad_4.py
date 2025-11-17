def display_only_second_element(numbers):
    for i in range(0, len(numbers), 2):
        print(numbers[i])

numbers = [ 61, 54, 21, 99, 88, 72, 44, 30, 40, 12]

display_only_second_element(numbers)