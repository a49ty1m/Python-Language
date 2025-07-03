def gen_table(n):
    table=""
    for a in range(1, 11):
        table += f"{n} x {a} = {n * a}\n"
    with open(f"CH's/Chapter_09/table_of_{n}.txt", "w") as f:
        f.write(table)
    print(f"Table of {n} generated successfully.")
# This code generates multiplication tables from 1 to 20 and saves them in separate text files
# Each file is named "table_of_n.txt" where n is the number for which the
    # This function generates a multiplication table for the number n

for i in range(1, 21):
    gen_table(i) 