def square(number):
    return number**2

number_list = range(101)
solution = list(map(square, number_list))

print(solution)
