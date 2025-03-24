# Python implementation of the approach 

# Function to check if we have found 
# a palindrome of same length as the input 
# which is a rotation of the input string 
def checkPal (x, Len):

    if (x == Len):
        return True
    elif (x > Len):
        if ((x % 2 == 0 and Len % 2 == 0) or (x % 2 != 0 and Len % 2 != 0)):
            return True

    return False

# Function to preprocess the string 
# for Manacher's Algorithm 
def reform (s):

    s1 = "$#"

    # Adding '#' between the characters
    for i in range(len(s)):
        s1 += s[i]
        s1 += "#"

    s1 += "@"
    return s1

# Function to find the longest palindromic 
# substring using Manacher's Algorithm 
def longestPal (s, Len):

    # Current Left Position 
    mirror = 0 
  
    # Center Right Position 
    R = 0
  
    # Center Position 
    C = 0 
  
    # LPS Length Array 
    P = [0] * len(s)
    x = 0 
  
    # Get currentLeftPosition Mirror 
    # for currentRightPosition i 
    for i in range(1, len(s) - 1):
        mirror = 2 * C - i 

        # If currentRightPosition i is 
        # within centerRightPosition R 
        if (i < R):
            P[i] = min((R-i), P[mirror])

        # Attempt to expand palindrome centered 
        # at currentRightPosition i
        while (s[i + (1 + P[i])] == s[i - (1 + P[i])]):
            P[i] += 1

        # Check for palindrome
        ans = checkPal(P[i], Len)
        if (ans):
            return True
        
        # If palindrome centered at current
        # RightPosition i expand beyond 
        # centerRightPosition R, adjust centerPosition
        # C based on expanded palindrome
        if (i + P[i] > R):
            C = i 
            R = i + P[i]

    return False

# Driver Code
if __name__ == '__main__':
    
    s = "aaaad"
    Len = len(s)
    s += s
    s = reform(s)
    print(longestPal(s, Len))
