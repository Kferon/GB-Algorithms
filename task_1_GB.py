"""
Задание 1.

Докажите, что словари обрабатываются быстрее, чем списки.

Реализуйте две функции, в первой нужно заполнить элементами список, во второй-словарь
Сделайте замеры времени выполнения каждой из функций

Подсказка: для замеров воспользуйтесь модулем time (см. примеры урока 1)

Примечание: eсли вы уже знаете, что такое декоратор и как его реализовать,
то реализуйте ф-цию-декоратор и пусть она считает время
И примените ее к двум своим функциям.
"""
import time

i = 0


def fill_dict(n):
    check1 = time.time()
    my_dict = {a: a for a in range(int(n))}
    check2 = time.time()
    x = check2 - check1
    return x





def fill_list(n):
    my_list = []
    check3 = time.time()
    for i in range(n):
        my_list.append(n)
    check4 = time.time()
    y = check4 - check3
    return y


time1 = fill_dict(10000000)
time2 = fill_list(10000000)
print(time2-time1)
