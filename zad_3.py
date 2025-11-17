def display_even_numbers(numbers3):
    for number3 in numbers3:
        if number3 % 2 == 0:
            print(number3)

numbers_list3 = list(range(10))
print("C) Liczby parzyste w numbers_list3:")
display_even_numbers(numbers_list3)