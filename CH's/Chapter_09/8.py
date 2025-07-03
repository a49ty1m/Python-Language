with open("CH's/Chapter_09/this.txt", "r") as f:
    content=f.read()
    # this will read the content of the file

with open("CH's/Chapter_09/this_copy.txt", "w") as g:
    content = g.write(content)
    # this will write the content of the file to another file