#Создайте англо-французский словарь с названием e2f и выведите его на экран. Вот ваши первые слова: dog/chien, cat/chat и walrus/morse. 

print('\nexercise_1\n')

e2f = {'dog' : 'chien', 'cat' : 'chat', 'walrus' : 'morse'}

# Используя словарь e2f, выведите французский вариант слова walrus. 

print('\n exercise_2\n')

print(e2f.get('walrus'))

# Создайте французско-английский словарь f2e на основе словаря e2f. Используйте метод items.

print('\n exercise_3\n') 

f2e = {value: key for key,value in e2f.items()}

print(f2e)

# Используя словарь f2e, выведите английский вариант слова chien. 

print('\nexercise_4\n')

print(f2e.get('chien'))

# Выведите на экран множество английских слов из ключей словаря e2f. 

print('\nexercise_5\n')

print(set(e2f.keys()))

# Создайте многоуровневый словарь life. Используйте следующие строки для ключей верхнего
#  уровня: 'animals', 'plants' и 'other'. Сделайте так, чтобы ключ 'animals' ссылался на другой 
# словарь, имеющий ключи 'cats', 'octopi' и 'emus'. Сделайте так, чтобы ключ 'cats' ссылался на 
# список строк со значени- ями 'Henri', 'Grumpy' и 'Lucy'. Остальные ключи должны ссылаться на пустые словари. 

print('\n exercise_6\n')

life = dict({'animals' : {'cats': ['Henry', 'Grumpy', 'Lucy'], 'octopi': {}, 'emus': {} }, 'plants':{}, 'other':{}})
print(life)

# Выведите на экран высокоуровневые ключи словаря life. 

print('\nexercise_7\n')

print(life.keys())

#Выведите на экран ключи life['animals']. 

print('\nexercise_8\n')

print(life['animals'].keys())

# Выведите значения life['animals']['cats']. 

print('\nexercise_9\n')

print(life['animals']['cats'])

# Используйте генератор словаря, чтобы создать словарь squares. 
# Используйте range(10), чтобы получить ключи. В качестве значений используйте возведен- ное в квадрат значение каждого ключа.

print('\nexercise_10\n') 

squares = {key : key**2 for key in range(10)}

print(squares)

#Используйте генератор множества, чтобы создать множество odd из нечетных чисел диапазона range(10)

print('\nexercise_11\n')

odd = set(number for number in range(10) if number %2 !=0 )
print(odd)

# Используйте включение генератора, чтобы вернуть строку 'Got ' и числа из диапазона range(10). Итерируйте по этой конструкции с помощью цикла for. 

print('\nexercise_12\n')

print(', '.join(f"Got {number}" for number in range(10)))

#Используйте функцию zip(), чтобы создать словарь из кортежа ключей('optimist', 'pessimist', 'troll') и 
# кортежа значений ('The glass is half full', 'The glass is half empty', 'How did you get a glass?'). 

print('\nexercise_13\n')

print(dict(zip({'optimist', 'pessimist', 'troll'}, {'The glass is half full', 'The glass in half empty', 'How did you get a glass?'})))

# Используйте функцию zip(), чтобы создать словарь с именем movies, в котором
# объединены списки titles = ['Creature of Habit', 'Crewel Fate', 'Sharks On a Plane'] и 
# plots = ['A nun turns into a monster', 'A haunted yarn shop', 'Check your exits'].

print('\nexercise_14\n')
titles = ['Creature of Habit', 'Crewel Fate', 'Shark On a Plane']
plots = ['A nun turns into a monster', 'A haunted yarn shop', 'Chek your exits']
movies = dict(zip(titles, plots))
print(movies)