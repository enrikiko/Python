from functools import reduce

number_list = range(1,100)
multiplier = lambda x, y : x * y

solution = reduce(multiplier, number_list)

print(solution)
