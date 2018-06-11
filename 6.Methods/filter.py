import statistics

number_list = range(100)

half_full = filter(lambda x : x > statistics.mean(number_list), number_list)
half_empty = filter(lambda x : x < statistics.mean(number_list), number_list)

print(half_full)
print(half_empty)
