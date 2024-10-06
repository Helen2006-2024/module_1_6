my_dict = {'Sasha': 1996, 'Ksu': 2014, 'Ann': 1971, 'Helen': 1979}
print(my_dict)
print(my_dict['Helen'])
print(my_dict.get('Kate'))
print(my_dict.get('Kate', 'Такого ключа нет'))
my_dict.update({'Nik': 2000,
                'Denis': 1985})
print(my_dict)
del my_dict['Ann']
print(my_dict)
my_set = {1, 2, 'a', 'b', 'a', 1, 'cat', (1, 2)}
print(my_set)
print(my_set.add('c'))
print(my_set)
print(my_set.add(3))
print(my_set)
print(my_set.discard('a'))
print(my_set)