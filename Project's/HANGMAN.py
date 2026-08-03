import random

name = input("What is your name? : ")
def greet(name):
    print(f"Hello {name}, Welcome to the HANGMAN's Game")
greet(name)

wordlist = ["hacker", "devlop", "poetry", "master", "python", "cyborg", "smiloo", "bugbug", "random"]
def pick_word(wordlist: list[str]) -> str:
    secret_word = random.choice(wordlist)
    return secret_word


word = []


for _ in range(len(secret_word)):
    word.append("_")
print(word)



game_over = False
while not game_over:
    guess = input("Guess The Letter:").lower()
    i=0 #score
    f=0 # fails
    for p in range(len(secret_word)): # p is possition (0,1,2,3,4,5)
        letter = secret_word[p]    # letter at the possition p
        i+=1
        if letter == guess:
            print("Possition is ", p+1)
            word[p] = letter
        else:  f+=1

    print(word)
    if "_" not in word:
        print ("You Won")
        print("Your Score Is : ",i)
        game_over= True
    if f == 6:
        print ("Too Many Tires, You Lost")

'''
## 1️⃣ Refactor into functions & add a `main` guard  
Separate concerns (setup, display, input handling, win/lose logic). This makes the script easier to test and extend.

```python
def pick_word(wordlist: list[str]) -> str:
    """Return a random word and hide it."""
    secret = random.choice(wordlist)
    masked = ["_"] * len(secret)
    return secret, masked

def display_state(masked: list[str]) -> None:
    print(masked)

def process_guess(secret: str, masked: list[str], guess: str) -> tuple[int, int]:
    """Update `masked` in‑place and return (hits, misses)."""
    hits = misses = 0
    for i, ch in enumerate(secret):
        if ch == guess:
            masked[i] = ch
            hits += 1
        else:
            misses += 1
    return hits, misses
```

```python
if __name__ == "__main__":
    # … call the functions here …
```

---

## 2️⃣ Track already‑guessed letters  
Prevent the player from “wasting” attempts on a letter they’ve already tried.

```python
used: set[str] = set()
...
guess = input("Guess a letter: ").lower()
if guess in used:
    print("You already tried that letter.")
    continue
used.add(guess)
```

---

## 3️⃣ Use a configurable max‑tries constant  
Replace the hard‑coded `6` with a named constant (or derive it from the word length).

```python
MAX_TRIES = 6          # or len(secret_word) + 2
fails = 0
...
if fails >= MAX_TRIES:
    print("Too many tries – you lost!")
    break
```

---

## 4️⃣ Clean up messaging & spelling  
* “Possition” → **Position**  
* “Tires” → **Tries**  
* Capitalise prompts for consistency.

```python
print(f"Position is {i + 1}")
...
print("Too many tries – you lost.")
```

---

## 5️⃣ Use `enumerate` instead of indexing manually  
Makes the loop clearer and removes the comment about “p is position”.

```python
for idx, letter in enumerate(secret_word):
    if letter == guess:
        print(f"Position is {idx + 1}")
        masked[idx] = letter
```

---

## 6️⃣ Separate score from loop counter  
`i` currently counts every iteration, which equals the number of guesses – that’s fine for a *score*, but it’s clearer to name it `guess_count`.

```python
guess_count = 0
...
guess_count += 1
...
print("Your score is:", guess_count)
```

---

## 7️⃣ Hide the secret word in production runs  
You currently `print(secret_word)`. Remove that line or guard it with a debug flag.

```python
DEBUG = False
if DEBUG:
    print(secret_word)
```

---

## 8️⃣ Validate input length  
Force the player to enter a single character (or a whole word for a “guess the word” mode).

```python
guess = input("Guess a letter: ").lower()
if len(guess) != 1 or not guess.isalpha():
    print("Please enter a single alphabetic character.")
    continue
```

---

## 9️⃣ Add a small game‑loop wrapper (optional)  
Allow the user to replay without restarting the script.

```python
while True:
    play_hangman()
    again = input("Play again? (y/n): ").lower()
    if again != "y":
        break
```

---

## 10️⃣ Minor style tweaks (PEP 8)

| Before | After |
|--------|-------|
| `word.append("_")` (inside a `for` loop) | `masked = ["_"] * len(secret_word)` |
| Multiple blank lines | Keep **max one** blank line between logical blocks |
| Mixed tabs/spaces | Use **4 spaces** throughout |

---

## 📂 File reference

You can open the script directly here: **[HANGMAN.py](file:///home/smilo/Desktop/MY_FOLDER/Python-Language/Project%27s/HANGMAN.py)**  

Apply the suggestions you like, re‑run the game (`python -u "…/HANGMAN.py"`), and you should see cleaner output, proper attempt limits, and a more maintainable code base. 🎮🚀'''