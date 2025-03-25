# Python 3 implementation to check 
# whether binary representation of
# a number is palindrome or not

# function to reverse bits of a number
def reverseBits(n) :
  rev = 0
    
  # traversing bits of 'n' from the right
  while (n > 0) :

     # bitwise left shift 'rev' by 1
     rev = rev << 1

     # if current bit is '1'
     if (n & 1 == 1) :
        rev = rev ^ 1

     # bitwise right shift 'n' by 1
     n = n >> 1
    
     # required number
     return rev
    
# function to check whether binary
# representation of a number is
# palindrome or not
def isPalindrome(n) :

    # get the number by reversing 
    # bits in the binary
    # representation of 'n'
    rev = reverseBits(n)

    return (n == rev)


# Driver program to test above
n = 9
if (isPalindrome(n)) :
    print("Yes")
else :
    print("No")
    
