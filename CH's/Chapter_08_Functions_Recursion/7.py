'''
def rem(l, word):
    for item in l:
        return l.remove(word)

l = ["hi", "hello", "world", "python", "programming", "language", "code"]
'''

def rem(l, word):
    n = [] 
    for item in l:
        if not(item == word):
            n.append(item.strip(word))
    return n


l = ["Harry", "Rohan", "Shubham", "an"]

print(rem(l, "an"))