def display_status(word, fail, guessed_letters):
    """Print the hangman drawing, word progress, and guessed letters."""
    print(HANGMAN_STAGES[fail])
    print("\nWord:    ", " ".join(word))
    print("Guessed: ", ", ".join(sorted(guessed_letters)) if guessed_letters else "none")
    print(f"Lives:    {max_life - fail} / {max_life}\n")

