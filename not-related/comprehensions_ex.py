# list, sets, dictionary

# list

my_list = [char for char in 'hello']
my_list2 = [num for num in range(0, 100)]
my_list3 = [num**2 for num in range(0, 100)]
my_list4 = [num**2 for num in range(0, 100) if num % 2 == 0]

# set

my_set = {char for char in 'hello'}
my_set2 = {num for num in range(0, 100)}
my_set3 = {num**2 for num in range(0, 100)}
my_set4 = {num**2 for num in range(0, 100) if num % 2 == 0}

# dict

simple_dict = {'a': 1, 'b': 2}
my_dict = {k: v**2 for k, v in simple_dict.items() if v % 2 == 0}
print(my_dict)
my_dict2 = {item: item*2 for item in [1, 2, 3]}
# print(my_dict2)


for k, v in enumerate(my_list4):
    print(k, v)

# excercise

some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

duplicates = []
for value in some_list:
    if some_list.count(value) > 1:
        if value not in duplicates:
            duplicates.append(value)

print(duplicates)

duplicates2 = list({value for value in some_list if some_list.count(value) > 1})
print(duplicates2)

