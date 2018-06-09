square = map(lambda x: x**2, range(1,101))
square2 = [i**2 for i in range(1,101)]

print(square)
print(square2)


movies=['Kill Bill V.1', 'Kill Bill V.2', 'The Lion King', 'Catch me if you can', 'Titanic']
tMovies = [title for title in movies if title.startswith('T')]
print(tMovies)
