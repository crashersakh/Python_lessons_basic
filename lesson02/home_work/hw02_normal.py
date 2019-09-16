import random

# Задача-1:
# Дан список, заполненный произвольными целыми числами, получите новый список,
# элементами которого будут квадратные корни элементов исходного списка,
# но только если результаты извлечения корня не имеют десятичной части и
# если такой корень вообще можно извлечь
# Пример: Дано: [2, -5, 8, 9, -25, 25, 4]   Результат: [3, 5, 2]

list1 = [2, -5, 8, 9, -25, 25, 4]
list2 = []
for elem in list1:
    if elem > 0:
        new_elem  = elem ** 0.5
        int_elem  = int(new_elem)
        if ( int_elem - new_elem ) == 0:
            list2.append(int_elem)
for elem in list2:
    print(elem)

# Задача-2: Дана дата в формате dd.mm.yyyy, например: 02.11.2013.
# Ваша задача вывести дату в текстовом виде, например: второе ноября 2013 года.
# Склонением пренебречь (2000 года, 2010 года)
strdate = input('Введите дату в формате DD.MM.YYYY: ')
list_date = strdate.split('.')
print(list_date)
if list_date[1] == '01':
    month = 'января'
elif list_date[1] == '02':
    month = 'февраля'
elif list_date[1] == '03':
    month = 'марта'
elif list_date[1] == '04':
    month = 'апреля'
elif list_date[1] == '05':
    month = 'мая'
elif list_date[1] == '06':
    month = 'июня'
elif list_date[1] == '07':
    month = 'июля'
elif list_date[1] == '08':
    month = 'августа'
elif list_date[1] == '09':
    month = 'сентября'
elif list_date[1] == '10':
    month = 'октября'
elif list_date[1] == '11':
    month = 'ноября'
elif list_date[1] == '12':
    month = 'декабря'

listnum = ['первое', 'второе', 'третье','четвертое', 'пятое', 'щестое','седьмое', 'восьмое', 'девятое']
if int(list_date[0]) == 10:
    datestr = 'десятое'
elif int(list_date[0]) == 11:
    datestr = 'одинадцатое'
elif int(list_date[0]) == 12:
    datestr = 'двенадцатое'
elif int(list_date[0]) == 13:
    datestr = 'тринадцатое'
elif int(list_date[0]) == 14:
    datestr = 'четырнадцатое'
elif int(list_date[0]) == 15:
    datestr = 'пятнадцатое'
elif int(list_date[0]) == 16:
    datestr = 'шестнадцатое'
elif int(list_date[0]) == 17:
    datestr = 'семнадцатое'
elif int(list_date[0]) == 18:
    datestr = 'восемнадцатое'
elif int(list_date[0]) == 19:
    datestr = 'девятнадцатое'
elif int(list_date[0]) == 20:
    datestr = 'двадцатое'
elif int(list_date[0]) == 30:
    datestr = 'тридцатое'
else:
    minusindex = int(list_date[0]) - 1
    if int(list_date[0]) < 10:
        datestr = listnum[minusindex]
    elif (int(list_date[0]) < 30)   and (  int(list_date[0]) > 20) :
        datestr = 'двадцать' + listnum[minusindex]
    elif int(list_date[0]) > 30:
        datestr = 'тридцать' + listnum[minusindex]
print('{} {} {} года'.format(datestr,month,list_date[2]))
# Задача-3: Напишите алгоритм, заполняющий список произвольными целыми числами
# в диапазоне от -100 до 100. В списке должно быть n - элементов.
# Подсказка:
# для получения случайного числа используйте функцию randint() модуля random
numelements = int(random.randint(1, 20))
randlist = []
for __ in range(numelements):
    randlist.append(random.randint(-100, 100))
for elem in randlist:
    print(elem)

# Задача-4: Дан список, заполненный произвольными целыми числами.
# Получите новый список, элементами которого будут:
# а) неповторяющиеся элементы исходного списка:
# например, lst = [1, 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 2, 4, 5, 6]
# б) элементы исходного списка, которые не имеют повторений:
# например, lst = [1 , 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 4, 6]
list_last = [1, 2, 4, 5, 6, 2, 5, 2]
lst2_1 = []
lst2_2 = []
for el4 in list_last:
    if  list_last.count(el4) < 2:
        lst2_2.append(el4)
        lst2_1.append(el4)
    else:
        if  lst2_1.count(el4) == 0:
            lst2_1.append(el4)
print(lst2_1)
print(lst2_2)