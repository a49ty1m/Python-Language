with open("CH's/Chapter_09/log.txt", "r") as f:
    h=f.read()
    if "python" in h:
        print("the word 'python' is present in the file.")
    else:
        print("the word 'python' is not present in the file.")