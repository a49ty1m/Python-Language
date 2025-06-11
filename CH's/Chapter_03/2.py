name = input("Enter Your Name : ")
date = input("When Would You Like to Join With us : ")
print(f'''
    Dear {name}
    You Are Selected!
    You Can Join From {date}''')

    
#second way
letter = '''Dear <|Name|>, 
You are selected! 
<|Date|> '''

print(letter.replace("<|Name|>", name).replace("<|Date|>", date))