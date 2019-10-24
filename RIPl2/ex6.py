import json
import sys
from librip.ctxmngrs import timer
from librip.decorators import print_result
from librip.gens import field, gen_random
from librip.iterators import Unique as unique

path = 'data_light.json'

# Здесь необходимо в переменную path получить
# путь до файла, который был передан при запуске

with open(path) as f:
    data = json.load(f)

# Далее необходимо реализовать все функции по заданию, заменив `raise NotImplemented`
# Важно!
# Функции с 1 по 3 дожны быть реализованы в одну строку
# В реализации функции 4 может быть до 3 строк
# При этом строки должны быть не длиннее 80 символов

@print_result
def f1():
    return sorted(list(field(data, 'job-name')))
   # raise NotImplemented

# Фильтр: выводит слова, в которых есть слово 'программист'
def prog(arr):
    if ('программист' in arr):
        return arr

@print_result
def f2():
    return list(filter(prog, f1()))
    #raise NotImplemented

def python(arr):
    return str(arr) + ' с опытом  Python'

@print_result
def f3():
    return list(map(python, f2()))
    #raise NotImplemented


@print_result
def f4():
    return list(zip(f3(), gen_random(100000, 200000, len(f3()))))
    #raise NotImplemented

# @timer
# def good():
#     f4(f3(f2(f1())))
#
# good()
with timer():
    f4(f3(f2(f1(data))))

