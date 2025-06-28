def star(n):
    """
    Returns a string of n stars.
    """
    if n == 0:
        return
    print("*" * n)
    star(n-1)  
a=(int(input("Enter the number of stars: ")))
print(star(a))