print('exercise_1\n')


# Создайте класс Thing, не имеющий содержимого, и выведите его на экран. Затем создайте объект example этого класса и также выведите его. Совпада- ют ли выведенные значения? 


class Thing():
    pass


print(Thing)

example = Thing()

print(example)


print('\nexercise_2\n')

# Создайте новый класс с именем Thing2 и присвойте переменной letters зна- чение 'abc'. Выведите на экран значение letters. 


class Thing2():
    pass


letters = Thing2()

letters = 'abc'

print(letters)


print('\nexercise_3\n')

# Создайте еще один класс, который, конечно же, называется Thing3. В этот раз присвойте значение 'xyz' атрибуту объекта letters. Выведите на экран зна-
# чение атрибута letters. Понадобилось ли вам создавать объект класса, чтобы сделать это?

class Thing3():
    pass


letters = Thing3()
letters.xyz = 'xyz'
print(letters.xyz)


print('\nexersise_4\n')


# Создайте класс Element, имеющий атрибуты объекта name, symbol и number. Создайте объект этого класса со значениями 'Hydrogen', 'H' и 1.


class Element():
    def __init__(self, name, symbol, number):
        self.name = name
        self.symbol = symbol
        self.number = number


obj = Element('Hydrogen\n', 'H\n', 1)

print(obj.name, obj.symbol, obj.number)


print('\nexersice_5\n')

# Создайте словарь со следующими ключами и значениями: 'name': 'Hydrogen _1', 'symbol': 'H', 'number': 1. 
# Далее создайте объект с именем hydrogen класса Element с помощью этого словаря. 

dic = {'name' : 'Hydrogen_1', 'symbol' : 'H', 'number' : '1'}
hydrogen = Element(**dic)

print(hydrogen.name)

print('\nexercise_6\n')


# Для класса Element_2 определите метод с именем dump(), который выводит на экран значения 
# атрибутов объекта (name, symbol и number). Создайте объект hydrogen из этого нового 
# определения и используйте метод dump(), чтобы вы- вести на экран его атрибуты.


class Element_2():
    def __init__(self, name, symbol, number):
        self.name = name
        self.symbol = symbol
        self.number = number
    def dump(self):
        print(' ' + self.name + '\n', self.symbol + '\n',  self.number)


hydrogen_2 = Element_2('Hydrogen_2', 'H', 1)
hydrogen_2.dump()


print('\nexercise_7\n')

# Вызовите функцию print(hydrogen). В определении класса Element измените имя метода dump на __str__, 
# создайте новый объект hydrogen и затем снова вызовите метод print(hydrogen).

print(hydrogen_2)

class Element_3():
    def __init__ (self, name, symbol, number):
        self.name = name
        self.symbol = symbol
        self.number = number
    def __str__ (self):
        return f'{self.name}, {self.symbol}, {self.number}'
        
        
hydrogen_3 = Element_3("Hydrogen_3", 'H', 1)


print(hydrogen_3)

print('\nexercise_8\n')

# Модифицируйте класс Element_4, сделав атрибуты name, symbol и number приватными. 
# Определите свойство получателя для каждого атрибута, возвращающее его значение. 


class Element_4():
    def __init__(self, name='Hydrogen_4', symbol='H', number='1'):
        self.__name = name
        self.__symbol = symbol
        self.__number = number
    
    @property
    def name(self):
        return self.__name
    
    @property
    def symbol(self):
        return self.__symbol
    
    @property
    def number(self):
        return self.__number
    
    @name.setter
    def name(self, name):
        self.__name = name
    
    @symbol.setter
    def symbol(self, symbol):
        self.__symbol = symbol
    
    @number.setter
    def number(self, number):
        self.__number = number
    
    def __str__(self):
        return f'{self.__name}, {self.__symbol}, {self.__number}'


example = Element_4()
example.name = 'H'

example.number = '999'
print(example.name, '\n', example.number)

print(example)

print('\nexercise_9\n')
#Определите три класса: Bear, Rabbit и Octothorpe. Для каждого из них опре- делите всего один метод — eats(). Он должен возвращать значения 'berries'
# (для Bear), 'clover' (для Rabbit) или 'campers' (для Octothorpe). Создайте
# по одному объекту каждого класса и выведите на экран то, что ест указанное животное. 

class Bear():
    @staticmethod
    def eats():
        return 'berries'

class Rabbit():
    @staticmethod
    def eats():
        return 'clover'

class Octothorpe():
    @staticmethod
    def eats():
        return 'campers'
    
vinny = Bear()
print(vinny.eats())
rodger = Rabbit()
print(rodger.eats())
octoth = Octothorpe()
print(octoth.eats()) 

print('\nexercise_10\n')
#Определите три класса: Laser, Claw и SmartPhone. Каждый из них имеет только один метод — does(). 
# Он возвращает значения 'disintegrate' (для Laser), 'crush' (для Claw) или 'ring' (для SmartPhone).
#  Далее определите класс Robot, который содержит по одному объекту каждого из этих классов. Определите метод does() для класса Robot, 
# который выводит на экран все, что делают его компоненты.

class Laser():
    def does(self):
        return "disintegrate"
    
class Claw():
    def does(self):
        return "crush"

class SmartPhone():
    def does(self):
        return "ring"
    
class Robot():
    def __init__(self):
        self.laser = Laser()
        self.claw = Claw()
        self.smartphone = SmartPhone()
    def does(self):
        print(f"{self.laser.does()}, {self.claw.does()}, {self.smartphone.does()}")

Robot().does()   