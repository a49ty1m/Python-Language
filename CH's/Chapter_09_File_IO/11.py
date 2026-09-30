with open("CH's/Chapter_09_File_IO/old.txt", "r") as file:
    content = file.read()

with open("CH's/Chapter_09_File_IO/new.txt", "w") as file:
    file.write(content)