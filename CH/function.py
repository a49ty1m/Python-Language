#HI
n = int(input("Enter a number you want factuorial of : "))
def fec(n):
    if n == 0 or n == 1:
        return 1
    else:
        for i in range(1, n+1):
            return n * fec(n-1)
print(fec(n))