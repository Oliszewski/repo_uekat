# A) Rozwiązanie wykorzystując pętlę for
def multiplyer_function(numbers1):
    result = []
    for number in numbers1:
        result.append(number * 2)
    return result

numbers_list = [1, 2, 3, 4, 5]
print("A) Wynik multiplyer_function:", multiplyer_function(numbers_list))


# B) Rozwiązanie wykorzystując listę składną
def multiplyer_function2(numbers2):
    return [number * 2 for number in numbers2]
numbers_list2 = [2, 4, 6, 8, 10]
print("B) Wynik multiplyer_function2:", multiplyer_function2(numbers_list2))
