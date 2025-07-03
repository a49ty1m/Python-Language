with open("CH's/Chapter_09/file1.txt", "r") as file1, open("CH's/Chapter_09/file2.txt", "r") as file2:
    content1 = file1.read()
    content2 = file2.read()

if content1 == content2:    
    print("The files are identical.")
else:   
    print("The files are different.")