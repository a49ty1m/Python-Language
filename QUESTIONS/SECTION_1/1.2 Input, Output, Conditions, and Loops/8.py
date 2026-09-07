# Accept 10 numbers and display how many are even and how many are odd.

def count_even_odd(numbers: list[int]) -> tuple[int,int]:
    even = 0
    odd = 0
    for _ in numbers:
        if _ % 2 == 0:
            even += 1
        else:
            odd += 1
    return even, odd

numbers = [int(input("Enter Number {} : ".format(i+1))) for i in range(10)]

even,odd = count_even_odd(numbers)
print("Even Numbers : ",even)
print("Odd Numbers : ",odd)
