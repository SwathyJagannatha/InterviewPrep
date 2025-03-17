# Python3 program for the above approach

# Function to check if a string
# is palindrome or not
def isPalindrome(Str):

    # Length of the string
    Len = len(Str)

    # Check if its a palindrome
    for i in range(Len):

        # If the palindromic
        # condition is not met
        if (Str[i] != Str[Len - i - 1]):
            return False

    # Return true as Str is palindromic
    return True

# Function to check if string str is 
# palindromic after removing every 
# consecutive characters from the str
def isCompressablePalindrome(Str):

    # Length of the string str
    Len = len(Str)

    # Create an empty compressed string
    compressed = ""

    # The first character will always
    # be included in final string
    compressed += Str[0]

    # Check all the characters 
    # of the string
    for i in range(1, Len):

        # If the current character
        # is not same as its previous
        # one, then insert it in 
        # the final string
        if (Str[i] != Str[i - 1]):
            compressed += Str[i]

    # Check if the compressed 
    # string is a palindrome
    return isPalindrome(compressed)

# Driver Code
if __name__ == '__main__':
    
    # Given string
    Str = "abbcbbbaaa"

    # Function call
    if (isCompressablePalindrome(Str)):
        print("Yes")
    else:
        print("No")
