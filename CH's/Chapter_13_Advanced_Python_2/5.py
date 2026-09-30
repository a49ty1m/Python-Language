from functools import reduce 
l = [155, 45 , 43, 745, 23, 34, 235]

def greater(a, b):
    if a > b:
        return a
    return b

print(reduce(greater , l))

