def remove_dup_word(string):
    # Used to split string around spaces.
    words = string.split()
    
    # To store individual visited words
    hsh = set()

    # Traverse through all words
    for word in words:
        # If current word is not seen before.
        if word not in hsh:
            print(word, end=" ")
            hsh.add(word)

# Driver function
if __name__ == '__main__':
    string = "Geeks for Geeks A Computer Science portal for Geeks"
    remove_dup_word(string)