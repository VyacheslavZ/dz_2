#Дан массив размера N. После каждого отрицательного элемента массива вставьте элемент с нулевым значением.
#Пример:
#- пусть N = 4, тогда [28, -46, 14, -14] => [28, -46, 0, 14, -14, 0]Дан массив размера N. 
# После каждого отрицательного элемента массива вставьте элемент с нулевым значением.

from random import randint


def random_list(listlen):
    datalist = list()
    for i in range(listlen):
        datalist.append(randint(-100, 101))
    return datalist


def null_insertion(data_list):
    for i in range(len(data_list) - 1, -1, -1):
        if data_list[i] < 0:
            data_list.insert(i + 1, 0)
    return data_list


def input_method():
    try:
        list_size = int(input('Введите размер массива: '))
        if list_size > 0:
            return list_size
        else:
            return exit('Не верное значение')
    except ValueError:
        return exit('Не верное значение')


list_len = input_method()
data = random_list(list_len)
print(data, end=' => ')
data = null_insertion(data)
print(data)