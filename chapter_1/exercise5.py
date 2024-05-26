# print all names of certain length [max 3 lines]
length = int(input('Enter name length: '))
print('\n'.join([word for word in (open('names.txt', 'r').read().split('\n')) if len(word) == length]))
