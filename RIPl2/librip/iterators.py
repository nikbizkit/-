# Итератор для удаления дубликатов
class Unique(object):
    def __init__(self, items, **kwargs):
        # Нужно реализовать конструктор
        # В качестве ключевого аргумента, конструктор должен принимать bool-параметр ignore_case,
        # в зависимости от значения которого будут считаться одинаковые строки в разном регистре
        # Например: ignore_case = True, Aбв и АБВ разные строки
        #           ignore_case = False, Aбв и АБВ одинаковые строки, одна из них удалится
        # По-умолчанию ignore_case = False
        self.lst = items
        self.index = 0
        self.array = []
        self.bool = 0
        pass

    def __next__(self):
        if self.index == len(self.lst):
            raise StopIteration
        if self.lst[self.index] not in self.array:
            self.array.append(self.lst[self.index])
            self.index += 1
            return self.lst[self.index - 1]
        self.index += 1

    def __iter__(self):
        return self

