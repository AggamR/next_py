# print sum of name lengths [max 2 lines]
from functools import reduce
print(reduce(lambda x, y: x + y, list(map(lambda x: len(x), open('names.txt', 'r').read().split('\n')))))
