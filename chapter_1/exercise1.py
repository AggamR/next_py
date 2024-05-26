# print longest mame in the file [max 2 lines]
from functools import reduce
print(reduce(lambda x, y: x if len(x) > len(y) else y, open('names.txt', 'r').read().split('\n')))
