from librip.gens import gen_random
from librip.iterators import Unique

data1 = [1, 1, 1, 1, 3, 4, 4, 1, 2, 2, 2, 2, 2]
data2 = gen_random(1, 3, 10)

# Реализация задания 2

a = Unique(data1)
print([i for i in a if i != None])

data = ['a', 'B', 'A', 'b']
c = Unique(data)
print([i for i in c if i != None])
