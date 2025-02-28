# Создайте файл с именем zoo.py. В нем объявите функцию hours(), которая выводит на экран строку 'Open 9-5 daily'. Далее используйте интерактивный 
# интерпретатор, чтобы импортировать модуль zoo и вызвать его функцию hours().

print('exercise_1\n')

import zoo
zoo.hours()



#  В интерактивном интерпретаторе импортируйте модуль zoo под именем menagerie и вызовите его функцию hours(). 

print('\nexercise_2\n')
import zoo as menegerie
menegerie.hours()


# Оставаясь в интерпретаторе, импортируйте непосредственно функцию hours() из модуля zoo и вызовите ее. 

print('\nexercise_3\n')

from zoo import hours
hours()

# Импортируйте функцию hours() под именем info и вызовите ее.

print('\nexersice_4')
from zoo import hours as info
info()

# Создайте словарь с именем plain, содержащий пары «ключ — значение» 'a': 1, 'b': 2 и 'c':3, а затем выведите его на экран. 

print('\nexercise_5')
plain = {'a':1, 'b' : 2, 'c' : 3}

print(plain)

# Создайте OrderedDict с именем fancy из пар «ключ — значение», приведенных в упражнении 11.5, и выведите его на экран. Изменился ли порядок ключей?

print('\nExercise_6\n')

from collections import OrderedDict

print(OrderedDict(plain))

# Создайте defaultdict с именем dict_of_lists и передайте ему аргумент list. 
# Создайте список dict_of_lists['a'] и присоедините к нему значение 'something for a' за одну операцию. Выведите на экран dict_of_lists['a'].
print('\nexercise_7\n')

from collections import defaultdict 

dict_of_lists = defaultdict(list)
dict_of_lists['a'].append('something for a')
import pprint as p
p.pprint(dict_of_lists)
p.pprint(dict_of_lists['a'])





