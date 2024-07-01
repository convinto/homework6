my_dict = {'Vasya':1975, 'Egor':1999, 'Masha':2002, 'Alex':1987, 'Eldar':2005}
print('Dict:', my_dict)
print('Existing value:', my_dict['Egor'])
print(my_dict.get('Ivan', 'Not existing value: None'))
my_dict['Svetlana'] = 1996
my_dict['Elena'] = 1987
a = my_dict.pop('Egor')
print('Deleted value:', a)
print('Modified dictionary:', my_dict)

my_set = {1, 1, 3, 'Яблоко', 42.314, 13, 'Яблоко', 42.314, 13, 'Яблоко', 1, 3}
print('Set:', my_set)
my_set.add((5, 6, 1.6))
my_set.add('Qwerty')
my_set.remove(1)
print('Modified set:', my_set)