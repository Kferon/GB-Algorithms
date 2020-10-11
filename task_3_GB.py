"""
Задание 3.
Определить количество различных подстрок с использованием хеш-функции.
Дана строка S длиной N, состоящая только из строчных латинских букв.

Подсказка: примените хеши и множества

рара:

рар
ра
ар
ара
р
а
"""
import hashlib
my_str = input('Введите строку: ')

res = set()

for i in range(len(my_str)):
    for j in range(i, len(my_str)):
        res.add(hashlib.sha256(my_str[i:j + 1].encode()).hexdigest())

print(f'Количество неповторяющихся подстрок - {len(list(res))}')
