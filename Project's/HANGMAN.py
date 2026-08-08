import random

# ── Constants ─────────────────────────────────────────────────


def greet():
    name = input("What is your name? : ").strip()
    print(f"Hello {name}, Welcome to the HANGMAN's Game\n")
    return name


def valid_guess(guessed_letters):
    """keeps asking for a valid letter until it gets one"""
    while True:
        guess = input("Guess a Letter: ").lower().strip()
        if len(guess) != 1 or not guess.isalpha():
            print("Please Enter A Valid Letter")
        elif guess in guessed_letters:
            print("You Already Guessed That")
        else:
            return guess


def display_status(word, fail, guessed_letters):
    """Print the hangman drawing, word progress, and guessed letters."""
    print(HANGMAN_STAGES[fail])
    print("\nWord:    ", " ".join(word))
    print("Guessed: ", ", ".join(sorted(guessed_letters)) if guessed_letters else "none")
    print(f"Lives:    {max_life - fail} / {max_life}\n")


# ── Setup ───────────────────────────────────────────────────────
name = greet()

wordlist = ["hacker", "devlop", "poetry", "master", "python", "cyborg", "smiloo", "bugbug", "random"]
secret_word = random.choice(wordlist)
# DEBUG — remove before sharing
print("[DEBUG] secret_word:", secret_word)
max_life = len(secret_word)

word = ["_"] * len(secret_word)

print(f"The word has {len(secret_word)} letters.\n")

HANGMAN_STAGES = [
    """
       -----
       |   |
           |
           |
           |
           |
    =========""",
    """
       -----
       |   |
       O   |
           |
           |
           |
    =========""",
    """
       -----
       |   |
       O   |
       |   |
           |
           |
    =========""",
    """
       -----
       |   |
       O   |
      /|   |
           |
           |
    =========""",
    """
       -----
       |   |
       O   |
      /|\\  |
           |
           |
    =========""",
    """
       -----
       |   |
       O   |
      /|\\  |
      /    |
           |
    =========""",
    """
       -----
       |   |
       O   |
      /|\\  |
      / \\  |
           |
    =========""",
]


# ── Game Loop ───────────────────────────────────────────────────
fail = 0
guessed_letters = []
score = 0

while fail < max_life:

    display_status(word, fail, guessed_letters)

    guess = valid_guess(guessed_letters)
    guessed_letters.append(guess)

    if guess in secret_word:
        print("✅ Correct!\n")
        for index, letter in enumerate(secret_word):   # index starts at 0 — correct!
            if guess == letter:
                word[index] = letter
                score += 10
    else:
        fail += 1
        print(f"❌ Wrong! {max_life - fail} lives remaining.\n")

    if "_" not in word:
        display_status(word, fail, guessed_letters)
        print("🎉 YOU WIN!")
        print(f"Your Score: {score}")
        break

else:
    display_status(word, fail, guessed_letters)
    print("💀 Too many tries! You lost.")
    print(f"The word was: '{secret_word}'")
    print(f"Your Score: {max(0, score - 100)}")





