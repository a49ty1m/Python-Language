a = " Aditya Mishra"
b=a.split("a")  # this will split the string into a list of characters
print(b) 
c=a.split("  ")# this will split the string into a list of characters
# Note: The second argument is two spaces, so it will split at double spaces.
print(c)
d=a.split()# this will split the string into a list of characters
# Note: The default behavior of split() is to split at any whitespace and remove extra spaces.
# This means it will split at single spaces, tabs, and newlines, and it will not include empty strings in the result.
# For example, if there are multiple spaces between words,
# they will be treated as a single space.
# This is useful for cleaning up strings with irregular spacing.
print(d)

