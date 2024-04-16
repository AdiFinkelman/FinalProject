from functools import reduce

string = ["hello", "world", "python", "is", "awesome"]

concat = lambda string: reduce(lambda x, y: x + ' ' + y, string)
result = concat(string)

print(result)