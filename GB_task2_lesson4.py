"""
Задание 2.

Приведен код, который формирует из введенного числа
обратное по порядку входящих в него цифр.
Задача решена через рекурсию

Сделайте замеры времени выполнения кода с помощью модуля timeit

Попробуйте оптимизировать код, чтобы снизить время выполнения
Проведите повторные замеры

Подсказка: примените мемоизацию

Добавьте аналитику: что вы сделали и почему
"""
import timeit


def memorize(func):
    def g(n, memory={}):
        r = memory.get(n)
        if r is None:
            r = func(n)
            memory[n] = r
        return r

    return g


@memorize
def recursive_reverse(number):
    if number == 0:
        return str(number % 10)
    return f'{str(number % 10)}{recursive_reverse(number // 10)}'


print(recursive_reverse(9 ** 99))

print(timeit.timeit("recursive_reverse(9**100)", setup="from __main__ import recursive_reverse", number=1000))

# Без мемоизации время выполнения примерно равно 0.060693899999999995, с ней - 0.0009699000000000027 т.к. благодаря
# механизму мемоизации полученные данные от рекурсии сразу записываются в словарь
