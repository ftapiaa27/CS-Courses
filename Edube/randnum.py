# from random import random
# for i in range(5):
#     print(random())

# from random import randrange, randint

# print(randrange(10), end=' ')
# print(randrange(0, 10), end=' ')
# print(randrange(0, 10, 1), end=' ')
# print(randint(0, 10))

from random import choice, sample

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(choice(my_list))
print(sample(my_list, 5))
print(sample(my_list, 10))