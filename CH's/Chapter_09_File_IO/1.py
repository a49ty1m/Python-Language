f= open("CH's/Chapter_09_File_IO/poem.txt", "r")
# print(f.read())
c = f.read()  # Reading the entire file
if ("star" in c):
    print("star is present in the file")
else:
    print("star is not present in the file")
f.close()