from librip.gens import field

goods = [
    {'title': 'Ковер', 'price': 2000, 'color': 'green'},
    {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'},
    {'title': 'Стелаж', 'price': 7000, 'color': 'white'},
    {'title': 'Вешалка для одежды', 'price': 800, 'color': 'white'}
]

print(list(field(goods, None)))

print(list(field(goods, 'title')))

print(list(field(goods, 'title', 'price')))

print(list(field(goods, 'title', 'price', 'color')))

print(list(field(goods, 'title', 'price', None, 'color', None)))


# Доп задания: кортежи квадрата чисел

print([(x, x * x) for x in range(1, 5)])

arr = [1, 2, 3, 4, 5]
a = map(lambda x: (x, x * x), arr)
print(list(a))
