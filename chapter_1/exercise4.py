# make file with name lengths [max 3 lines]
open('name_lengths.txt', 'w').write('\n'.join(list(map(lambda x: str(len(x)), (open('names.txt', 'r').read().split('\n'))))))
