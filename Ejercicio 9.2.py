from functools import reduce

numimp = list(filter(lambda x: x % 2 != 0, [0,1,2,3,4,5,6,7,8,9]))
total = reduce(lambda a, b: a + b, numimp)

print(total)