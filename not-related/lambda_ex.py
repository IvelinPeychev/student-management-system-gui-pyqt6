# Square
from audioop import reverse

my_list = [5, 4, 3]

print(list(map(lambda x: x ** 2, my_list)))

# List sorting by second item
a = [(0, 2), (4, 3), (10, -1), (19, 9)]
a.sort(key=lambda x: x[1])
print(a)


def myfunc(n):
    return lambda a: a * n


mytripler = myfunc(3)

print(mytripler(11))
