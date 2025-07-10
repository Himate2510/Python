def reversestrings(s):
    if len(s) == 1:
        return s[0]
    firstch = s [0]
    return reversestrings(s[1:]) + firstch
s = "Hello"
print("Reversed string is: ", reversestrings(s))