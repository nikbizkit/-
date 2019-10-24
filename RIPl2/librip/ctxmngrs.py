# Здесь необходимо реализовать
# контекстный менеджер timer
# Он не принимает аргументов, после выполнения блока он должен вывести время выполнения в секундах
# Пример использования
# with timer():
#   sleep(5.5)
#
# После завершения блока должно вывестись в консоль примерно 5.5

# Декоратор, вычисляющий время выполнения функции

def timer(func):
	import time

	def wrapper(*args, **kwargs):
		t = time.time()
		res = func(*args, **kwargs)
		print("Function " + str(func.__name__) + " : " + str(time.time() - t) + "(sec)")
	return wrapper

