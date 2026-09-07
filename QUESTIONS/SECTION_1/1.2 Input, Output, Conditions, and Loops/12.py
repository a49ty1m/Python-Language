# Validate numeric input so that non-numeric values do not crash your program.

def validity_checker(inp: str) -> int:
    if inp.isdigit():
        print('''Valid input
        it's an interger''')
    else:
        print(f"""Invalid input
        it's not an interger 
        it's an {type(inp)}""")

validity_checker(input("Enter a value: "))