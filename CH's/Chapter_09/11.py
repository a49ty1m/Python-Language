with open("CH's/Chapter_09/old.txt", "r") as file:
    content = file.read()

with open("CH's/Chapter_09/new.txt", "w") as file:
    file.write(content)