# Predict the result of comparison and logical expressions using `and`, `or`, and `not`.

def comparitions(x: int,y : int) -> None:
    print("{} and {}".format(x,y), bool(x and y))
    print("{} or {}".format(x,y), bool(x or y))
    print("not {}".format(x), bool(not x))
    print("not {}".format(y), bool(not y))
    print("{} and {} or {}".format(x,y,y), bool(x and y or y))

comparitions(1,0)
comparitions(1,1)
comparitions(0,1)
comparitions(0,0)