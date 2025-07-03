with open("CH's/Chapter_09/log.txt", "r") as f:
    lines=f.readlines()
    # this will store lines in a list
    line_no=1
    for line in lines:
        # here it will assign each line to the variable (line)
        if "python" in line:
            print(f"the word 'python' is present in the file at line {line_no}.")
            break
        # if the word 'python' is present in the line, it will print the line number
        # and break the loop
        line_no += 1 # incrementing the line number
    else:
        print("the word 'python' is not present in the file.")
        # if the word 'python' is not present in the file, it will print this message
# this else block is associated with the for loop, not the if statement