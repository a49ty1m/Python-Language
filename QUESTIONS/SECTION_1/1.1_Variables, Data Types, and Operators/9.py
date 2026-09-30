# Use the walrus operator (`:=`) to assign and check a value inside a `while` loop condition.

def walrus_input_loop() -> None:
    print("Type anything you want. Type 'exit' to stop.")
    
    # Walrus assigns to user_input AND checks if it is not 'exit'
    while (user_input := input("Enter something: ").strip()) != "exit":
        print(f"Echo: {user_input} (Length: {len(user_input)})")
    
    print("Exited the loop successfully.")


if __name__ == "__main__":
    walrus_input_loop()
