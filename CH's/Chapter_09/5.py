words = ["donkey", "village","lazy"]
with open("CH's/Chapter_09/hi.txt", "r") as f:
    content=f.read()
    for word in words:
        content = content.replace(word, "*" * len(word))
        with open("CH's/Chapter_09/hi.txt", "w") as f:
            f.write(content)
        print(f"The word '{word}' has been replaced with '****'.")
    else:
   
        print(f"The word '{word}' is not present in the file.")
'''
 This code replaces the words "donkey", "village", and "lazy" with asterisks in the file "hi.txt"
 If the word is found, it prints a message indicating its replacement
'''
