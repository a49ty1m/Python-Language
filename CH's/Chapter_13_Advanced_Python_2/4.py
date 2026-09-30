a = [155, 4546645 , 67756443, 45468745, 23423423, 34534534, 234235]
dev5 = lambda x : x%5 == 0
b = list(filter(dev5 , a))
print(b)

