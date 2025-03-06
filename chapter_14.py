# Выведите на экран список всех файлов из текущего каталога.
print('exersice_1\n')
import os
print(os.listdir('python_projects')) 


# Выведите на экран список всех файлов из родительского каталога. 
print('\nexercise_2\n')
print(os.listdir('.'))
print(os.listdir('..'))



# Присвойте строку This is a test of the emergency text system переменной test1 и запишите эту переменную в файл с именем test.txt.
print('\nexersice_3\n')
test1 = 'This is a test of the emergency text system'
with open('text.txt', 'wt') as test:
    test.write(test1)




# Откройте файл test.txt и считайте его содержимое в строку test2. Будут ли одинаковыми строки test1 и test2?
print('\nexersice_4\n')
with open('text.txt', 'rt') as test:
    if test.read() == test1:
        print('True') 
    else:
        print('False')


