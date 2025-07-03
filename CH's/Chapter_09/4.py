word = "donkey"
with open("CH's/Chapter_09/hi.txt", "r") as f:
    content=f.read()
    if word in content:
        print(f"The word '{word}' is present in the file.")
        content = content.replace(word, "****")
        with open("CH's/Chapter_09/hi.txt", "w") as f:
            f.write(content)
        print(f"The word '{word}' has been replaced with '****'.")
    else:
        print(f"The word '{word}' is not present in the file.")
# This code checks if the word "donkey" is present in the file "hi.txt"
# If the word is found, it prints a message indicating its presence

'''this code replaces the word "donkey" with "****" in the file "hi.txt"'''

# word = "****"
# with open("CH's/Chapter_09/hi.txt", "r") as f:
#     content=f.read()
#     if word in content:
#         print(f"The word '{word}' is present in the file.")
#         content = content.replace(word, "donkey")
#         with open("CH's/Chapter_09/hi.txt", "w") as f:
#             f.write(content)
#         print(f"The word '{word}' has been replaced with 'donkey'.")
#     else:
#         print(f"The word '{word}' is not present in the file.")
# # This code checks if the word "****" is present in the file "hi.txt"
# # If the word is found, it prints a message indicating its presence

'''this code replaces the word "****" with "donkey" in the file "hi.txt"'''