# i = 10
# for i in range(10, 0, -1):
#     print(i)

# a = 6/(2*3)
# print(4%11)

# x = int(input())
# y = int(input())

# x = x % y
# print(x)
# x = x % y
# print(x)
# y = y % x

# print(y)

# print(1//2)

import string


class String:
    def __init__(self, string):
        self.string = string
        
    def __add__(self, other):
        return self.string + other.string