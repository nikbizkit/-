# Здесь необходимо реализовать декоратор, print_result который принимает на вход функцию,
# вызывает её, печатает в консоль имя функции, печатает результат и возвращает значение
# Если функция вернула список (list), то значения должны выводиться в столбик
# Если функция вернула словарь (dict), то ключи и значения должны выводить в столбик через знак равно
# Пример из ex_4.py:
# @print_result
# def test_1():
#     return 1
#
# @print_result
# def test_2():
#     return 'iu'
#
# @print_result
# def test_3():
#     return {'a': 1, 'b': 2}
#
# @print_result
# def test_4():
#     return [1, 2]
#
# test_1()
# test_2()
# test_3()
# test_4()
#
# На консоль выведется:
# test_1
# 1
# test_2
# iu
# test_3
# a = 1
# b = 2
# test_4
# 1
# 2

# Декоратор print_result

def	print_result(decorator_arg):
	def	decorated_func():
		# Печать имени функции,  которую вызвали
		print(decorator_arg.__name__)
		#Если возвращаемое значение у функции 'int' or 'string' => просто выводим их на экран
		if isinstance(decorator_arg(), int) == True or isinstance(decorator_arg(), str) == True:
			print(decorator_arg())
		#Если возвращаемое значение у функции 'словарь' => печатаем ключ и значение, между ними '='
		elif isinstance(decorator_arg(), dict) == True:
			for key, value in decorator_arg().items():
				print(str(key) + ' = ' + str(value))
		# Если возвращаемое значение у функции 'массив' => печатаем в столбик его элементы
		elif isinstance(decorator_arg(), list) == True:
			for i in decorator_arg():
				print(i)
		# Возвращаем указатель на функцию
		return decorator_arg
	return decorated_func()

