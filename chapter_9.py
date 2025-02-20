#Определите функцию good(), которая возвращает следующий список:['Harry', 'Ron', 'Hermione'].
print('\nexercise_1\n')


def good():
    print(['Harry', 'Ron', 'Hermione'])
    return

good()


# Определите функцию генератора get_odds(), которая возвращает нечетные числа из диапазона range(10). 
# Используйте цикл for, чтобы найти и вывести третье возвращенное значение.

print('\nexercise_2\n')


def get_odds():
    numbers = []
    for number in range(1, 11, 2):
        numbers.append(number) 
    for odds in numbers:
        if numbers.index(odds) == 2:
            print(odds)    
    return (numbers)


print(get_odds())


def get_odds_2():
    for number in range(1, 10, 2):
        yield number


count = 0
for odds in get_odds_2():
    if count == 2:   
        print('third count is %s' % odds)
        break
    count += 1

#Определите декоратор test, который выводит строку 'start' при вызове функ- ции и строку 'end', когда функция завершает свою работу.

print('\nexercise_3\n')

def document_it(func):
    def new_func(*args, **kwargs):
        print('start')
        print('Name of function', func.__name__)
        print('Positional arguments', args)
        print('Keyword arguments', kwargs)
        result = func(*args, **kwargs)
        print(result, 'end')
        return result
    return new_func
    
@document_it
def get_odds():
    numbers = []
    for number in range(1, 11, 2):
        numbers.append(number) 
    for odds in numbers:
        if numbers.index(odds) == 2:
            print(odds)    
    return (numbers)
        
get_odds()


# Определите исключение OopsException. Сгенерируйте его и посмотрите, что произойдет. 
# Затем напишите код, позволяющий поймать это исключение и вывести строку 'Caught an oops'.


print('\nexercisw_4\n')
class OopsException(Exception):
    pass

try: 
   raise OopsException()
except:
    print('Cauth an oops')


list_1 = [1, 2, 4, 5]
position = "f"
try:
    list_1[position]
except IndexError as err:
    print('Index err', err)
except:
    print('Other mistakes')