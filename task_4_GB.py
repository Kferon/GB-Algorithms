"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница, если нет, то вносит ее в кэш

Подсказка: задачу решите обязательно с применением 'соленого' хеширования
Можете условжнить задачу, реализовав ее через ООП
"""

def site_cash(site, cash = [], i = 0, n = 0):
    x = site
    site = hash(site)
    while n < len(cash)-1:
        if cash[i] != site:
            n+=1
            site_cash(site, cash, i+1)
        else:
            continue
    cash.append(x)
    return cash
print(site_cash('http://stackoverflow.com'))


