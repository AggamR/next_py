# print shortest names in file [max 4 lines]
# messy 1-liner version:
print('\n'.join([word for word in (open('names.txt', 'r').read().split('\n')) if len(word) == min(map(lambda x: len(x), (open('names.txt', 'r').read().split('\n'))))]))
# cleaner 2 lines version:
# ln = min(map(lambda x: len(x), words := open('names.txt', 'r').read().split('\n')))
# print('\n'.join([word for word in words if len(word) == ln]))
