translation = {
    "sahayta": "help",
    "sahayta kijiye": "help me",
    "khelo": "play",
    "kutta": "dog",
    "billi": "cat",
    "gadha": "donkey",
    "bhas":"bull",
    "gadi": "car",
}

word = input("Hindi to English Dictionary\nEnter a Hindi word: ")

print(f"The English meaning of the {word} is:", translation.get(word, "Word not found in dictionary"))
# or "Translation not available"))