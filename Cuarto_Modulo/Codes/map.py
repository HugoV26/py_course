"""
    * Map Function
    * Returns a map object(which is an iterator) of the results after applying the given function to each item of a given iterable(list, tuple, etc).

    ^ Parameters
    ~ Param1: it's a function to which map passes each element of given iterable
    ~ Param2: it's a iterable which is to be mapped
"""

import math

def mult(n):
    return n * n

numbers = (1, 2, 3, 4, 5)
result = list(map(mult, numbers))
#print(list(result))
print(result)

# ^ Using lambda

result_lambda = set(map(lambda x: x*x, numbers))
print(result_lambda)

# ^ Map can listify the list of strings individually

my_str = ['Paco', "Cachondo"]
list_of_strings = list(map(list, my_str))
print(list_of_strings)

# * Celsius to farenheit
temps = [("Berlin", 29), ("Cairo", 36), ("Buenos Aires", 19), ("Los Angeles", 26), ("Tokyo", 27), ("New York", 28), ("London", 22), ("Beijing", 32)]

# 9/5 * temp + 32

c_to_f = lambda data: (data[0], (9/5*data[1])+32)

print(list(map(c_to_f, temps)))