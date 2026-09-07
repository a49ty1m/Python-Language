# Compare `for`, `while`, `break`, `continue`, and `pass` by writing one short example of each.


def for_loop(x: int) -> None:
    print("FOR LOOP")
    for i in range (x):
        print(i)
    #it will always run without any condition 

def while_loop(x: int) -> None:
    print("WHILE LOOP")
    i = 0 
    while i < x:
        print(i)
        i += 1
        #it will run before checking the condition first time 

def break_continue_pass(x: int) -> None:
    print("BREAK CONTINUE PASS")
    for i in range (x):
        if i == 2:
            print("BREAK")
            break
        #it will break the loop

        if i == 3:
            print("CONTINUE")
            continue
        #it will skip the current iteration

        if i == 4:
            print("PASS")
            pass
        #it will do nothing mostly used for future programming
            


    
