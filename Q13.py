from functools import reduce

input_lists = [['level', 'noon', 'hello'], ['radar', 'banana', 'world'], ['madam', 'racecar', 'python']]

count_palindromes = lambda lst: list(map(lambda sublist: reduce(lambda x, _: x + 1, filter(lambda a: a == a[::-1], sublist), 0), lst))

result = count_palindromes(input_lists)
print(result)