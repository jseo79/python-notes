import os
import math
from functools import reduce

# x = [5, 43, 2]

# for i in range(10):
#     print(math.ceil(4.5))

# print("poopasd")

# print("My name is {p} {a} {s}".format(p=x, a="pee", s="alsda"))

# a = 1.234

# print("hello %s %.2f %c" % ("Joseph", a, "A"))


# x = input("what is your favorite flavor?")

# print(x)

# str = "abcdefghijklmnop"
# str = str[:5]
# print(str)

# firstName = "Joseph"
# middleName = "Dongmin"
# lastName = "Seo"

names = ["Joseph", "Dongmin", "Seo"]
# print("-".join(names))

# meat = "chicken"
# print(f"I like to eat {meat}")

# names.remove("Dongmin")
# print(names)

# l4 = [1, 2, 3]

# for x in l4:
#     print("poop")

# l5 = [3, 6, 9]
# iter1 = iter(l5)
# print(next(iter1))
# print(next(iter1))

# print(type([1, 2, 3, 4]))
# print(type(list(range(1))))

# x = list(range(4))
# print(x)

# x = [1, 3, 5, 7, 8, 9]
# print(x[::-1])
# print(x.reverse())

# heroes = {"Superman": "Clark Kent", "Batman": "Bruce Wayne"}

# print(heroes["Superman"])

# x = [1, 2]

# x[1] = 5
# print(x)

# print(list(heroes.keys()))

# heroes = {"Superman", "Clark Kent", "Batman", "Bruce Wayne"}

# heroes2 = {"Poop"}

# heroes.add("poop")
# heroes.discard("Superman")
# heroes.discard("batman")
# print(heroes)

# print(heroes.symmetric_difference(heroes2))


# def get_sum(int1, int2):
#     return int1 + int2


# x = get_sum(1, 5)

# print(x)


# def getSum(*args):
#     sum = 0
#     for arg in args:
#         sum += arg
#     return sum


# print(getSum(1, 4, 3, 4, 2, 3, 4, 4))


# def multBy(x):
#     return lambda z: x / z


# print(multBy(7)(2))


# def addition(n):
#     return n + n

# numbers = (1, 2, 3, 4)
# result = map(addition, numbers)
# print(result)
# print(list(result))


# def isEven(x):
#     return x % 2 == 0


numbers = [1, 5, 11, 10, 36, 5, 2, 7]
# print(list(filter(isEven, numbers)))


# def add(x, y):
#     return x + y

# print(reduce(addAll, numbers))

# while True:
#     try:
#         number = int(input("input?"))
#         break
#     except ValueError:
#         print("Not a number")
# print("It is a number!")


# class Square:
#     def __init__(self, height="0", width="0"):
#         self.height = height
#         self.width = width

#     @property
#     def height(self):
#         print("Getting the height!")
#         return self.__height

#     @height.setter
#     def height(self, value):
#         if value.isdigit():
#             self.__height = value
#         else:
#             print("Please only enter numbers!")


# bigBoi = Square()

# bigBoi.height = "10"
# print(bigBoi.height)

# Python program for implementation of MergeSort

# Merges two subarrays of arr[].
# First subarray is arr[l..m]
# Second subarray is arr[m+1..r]
#poop