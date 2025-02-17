
print('\n exercise_7.1\n')
# Создайте список years_list, содержащий год, в который вы родились, и каждый последующий год 
# вплоть до вашего пятого дня рождения. Например, если вы родились в 1980 году, 
# список будет выглядеть так: years_list = [1980, 1981,1982, 1983, 1984, 1985].

years_list = list(range (1993,1999))
print(years_list)

print('\n exercise_7.2\n')

# В какой год из списка years_list был ваш третий день рождения? Учтите, в первый год вам было 0 лет. 

print(years_list[2])
# В какой год из списка years_list вам было больше всего лет?

print('\n exercise_7.3\n')

print(max(years_list))

# Создайте список things, содержащий три элемента: "mozzarella", "cinderella","salmonella".

print('\n exercise_7.4\n')

things = ["mozzarella", "cinderella", "salmonella"]

# Напишите с большой буквы тот элемент списка things, который означает чело- века, а затем выведите список. Изменился ли элемент списка?

print('\n exercise_7.5\n')

things[1] = things[1].capitalize()

print(things)

# Переведите сырный элемент списка things в верхний регистр целиком и вы- ведите список.

print('\n exercise_7.6\n')

things[0] = things[0].swapcase()

print(things)

# Удалите из списка things заболевание, получите Нобелевскую премию и затем выведите список на экран.

print('\n exercise_7.7\n')

things.remove(things[2])

print(things)

# Создайте список с элементами "Groucho", "Chico" и "Harpo"; назовите его surprise.

print('\n exercise_7.8\n')

surprise = ["Groucho", 'Chico', 'Harpo']

# Напишите последний элемент списка surprise со строчной буквы, затем выведите эту строку в обратном порядке и с прописной буквы.
print('exercise_7.9')
print(len(surprise))
surprise[len(surprise)-1] = surprise[len(surprise)-1].lower()[::-1].capitalize()     

print(surprise)

# Используйте списковое включение, чтобы создать список с именем even, в ко- тором будут содержаться четные числа в промежутке range(10). 

print('\n exercise_7.10\n')

even = [number for number in range(11) if number %2 == 0]
print(even)

# Попробуйте создать генератор рифм для прыжков через скакалку. Напечатайте последовательность двухстрочных рифм. 

print('\n exercise_7.11\n')

start1 = ['fee', 'fie', 'foe']
rhymes = [
    ('floop', 'get a mop'),
    ('fope', 'turn the rope'),
    ('fa', 'get your ma'),
    ('fudge', 'call the judle'),
    ('fat', 'pet the cat'),
    ('fog', 'walk the dog'),
    ('fun', "say we're done" )
]
start2 = ['cat', 'bat', 'that']
first = tuple(word[0].capitalize() + '! \n'for word in rhymes)
print(first)
second = tuple(words[1] + '. \n'for words in rhymes)
print(second) 
print('' .join(word.capitalize() + '! \n' for word in start1))
print(''.join(word + '. \n'for word in start2))
