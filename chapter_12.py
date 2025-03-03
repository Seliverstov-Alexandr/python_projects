# Создайте строку Unicode с именем mystery и присвойте ей значение '\U0001f4a9'. Выведите на экран значение строки mystery. 
# Выведите на экран значение пере- менной mystery и ее имя Unicode. 
print('exersice_1\n')
import unicodedata
mystery = '\U0001f4a9'
print(mystery, unicodedata.name(mystery) )

# Закодируйте строку mystery, на этот раз с использованием кодировки UTF-8, в переменную типа bytes с именем pop_bytes.
#  Выведите на экран значение переменной pop_bytes. 

print('\nexersice_2\n')


print(unicodedata.name(mystery), '\n', unicodedata.lookup(unicodedata.name(mystery)))
pop_bytes = mystery.encode('utf-8')
print(pop_bytes)

# Используя кодировку UTF-8, декодируйте переменную pop_bytes в строку pop_string. Выведите на экран значение переменной pop_string. 
# Равно ли оно значению переменной mystery? 

print('\nexercise_3\n')

pop_string = pop_bytes.decode('utf-8')
print(type(pop_string), '\n', pop_string, '\ncomparison', pop_string == mystery)


#При работе с текстом могут пригодиться регулярные выражения. В следую- щем примере (пример 12.1) мы воспользуемся ими несколькими способами.
# Перед вами стихотворение Ode on the Mammoth Cheese, написанное Джеймсом Макинтайром в 1866 году во славу головки сыра весом 7000 фунтов, 
# которая была изготовлена в Онтарио и отправлена в международное путешествие. Если не хотите самостоятельно перепечатывать это стихотворение, 
# используйте свой любимый поисковик и скопируйте текст в программу. 
# Или скопируйте стихотворение из проекта «Гутенберг» (http://bit.ly/mcintyre-poetry). Назовите следующую строку mammoth:

print('\nexersice_4\n')

mammoth = "\tWe have seen thee, queen of cheese,\n\t\
Lying quietly at your ease, \n\t\
Gently fanned by evening breeze,\n\t\
Thy fair form no flies dare seize.\n\t\
All gaily dressed soon you'll go\n\t\
To the great Provincial show,\n\t\
To be admired by many a beau \n\t\
In the city of Toronto.\n\t\
Cows numerous as a swarm of bees,\n\t\
Or as the leaves upon the trees, \n\t\
It did require to make thee please,\n\t\
And stand unrivalled, queen of cheese.\n\t\
May you not receive a scar as\n\t\
We have heard that Mr. Harris \n\t\
Intends to send you off as far as \n\t\
The great world's show at Paris.\n\t\
Of the youth beware of these,\n\t\
For some of them might rudely squeeze\n\t\
And bite your cheek, then songs or glees \n\t\
We could not sing, oh! queen of cheese.\n\t\
We'rt thou suspended from balloon,\n\t\
You'd cast a shade even at noon,\n\t\
Folks would think it was the moon \n\t\
About to fall and crush them soon."
print(mammoth)

#Импортируйте модуль re, чтобы использовать функции регулярных выраже- ний в Python. Примените функцию re.findall()
# для вывода на экран всех слов, начинающихся с буквы с.
print('\nexersice_5\n')
import re
print(re.findall(r'\bc\w*',mammoth, re.IGNORECASE))



#Найдите все четырехбуквенные слова, которые начинаются с буквы c.
print('\nexercise_6\n')
print(re.findall(r'\bc\w{3}\b',mammoth, re.IGNORECASE))


# Найдите все слова, которые заканчиваются на букву r. 
print('\nexersice_7\n')
print(re.findall(r'\w*r\b',mammoth))

# Найдите все слова, которые содержат три гласные подряд. 
print('\nexcersise_8\n')
print(re.findall(r'\b\w*[euioa]{3}\w*\b',mammoth, re.IGNORECASE))

# Используйте метод unhexlify для того, чтобы преобразовать шестнадцате- ричную строку, созданную путем 
# объединения двух строк для размещения на странице, в переменную типа bytes с именем 
# gif:'47494638396101000100800000000000ffffff21f9' + '0401000000002c000000000100010000020144003b'
print('\nexersice_9\n')

import binascii
gif_string = '47494638396101000100800000000000ffffff21f9' + '0401000000002c000000000100010000020144003b'
gif= binascii.unhexlify(gif_string)

print(gif)




# Байты, содержащиеся в переменной gif, определяют однопиксельный про- зрачный GIF-файл. Этот формат является одним из самых распространенных.
# Корректный файл формата GIF начинается со строки GIF89a. Корректен ли этот файл?
print('\nexersice_10\n')
if gif[:6] == b'GIF89a':
    print('correct')
else:
    print('NO')




# Ширина GIF-файла в пикселах является шестнадцатибитным целым числом с обратным порядком байтов, которое начинается со смещения 6 байт. 
# Высота имеет такой же размер и начинается со смещения 8 байт. Извлеките и выведите на экран эти значения для переменной gif. Равны ли они 1?
print('\nexersice_11\n')
import struct
print(len(gif))

width =struct.unpack('<6xH34x',gif)[0]
height = struct.unpack('<8xH32x', gif)[0]

print(width, height)