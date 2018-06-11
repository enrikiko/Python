import sys
import timeit

number_list = [0,1,2,3,4,5,6,7,8,9]
number_tuple = (0,1,2,3,4,5,6,7,8,9)

print("List lenght = ", len(number_list))
print("Tuple lenght = ", len(number_tuple))

for i in number_list:
    print("List:",i)
for i in number_tuple:
    print("Tuple:",i)


print("List size = ", sys.getsizeof(number_list))
print("Tuple size = ", sys.getsizeof(number_tuple))

list_test = timeit.timeit(stmt="[0,1,2,3,4,5,6,7,8,9]",number=10000000)
tuple_test = timeit.timeit(stmt="(0,1,2,3,4,5,6,7,8,9)",number=10000000)
print("List time = ",list_test)
print("Tuple time = ",tuple_test)

person = ("Enrique", "Ramos", "Muñoz")
name, first_surname, second_surname = person
print(first_surname, second_surname, name)
