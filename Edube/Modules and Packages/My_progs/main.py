from sys import path
path[0] = path[0].replace("My_progs", "My_modules")
from module import suml, prodl, __counter

print(__counter)
zeroes = [0 for i in range(5)]
ones = [1 for i in range(5)]
print(suml(zeroes))
print(prodl(ones))
print(__counter)