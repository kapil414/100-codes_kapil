def removeSpecialCharacter(s):
    i = 0
    while i < len(s):
        # Finding the character whose ASCII value fall under this range
        if (ord(s[i]) < ord('A') or ord(s[i]) > ord('Z') and ord(s[i]) < ord('a') or ord(s[i]) > ord('z')):
            # erase function to remove the character
            del s[i]
            i -= 1
        i += 1
    print("".join(s))

# main Code
if __name__ == '__main__':
    s = "P*r;e..pi, n'st^a?"
    s = [i for i in s]
    removeSpecialCharacter(s)
