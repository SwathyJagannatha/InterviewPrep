# Python program to generate all possible valid
# ip address using backtracking

# Function to check whether segment is valid or not.
def isValid(s):
    n = len(s)

    # Segment of length one is always valid
    if n == 1:
        return True

    # Converting string into integer
    val = int(s)

    # Invalid case: If it has a preceding zero or 
    # its value is greater than 255
    if s[0] == '0' or val > 255:
        return False

    return True

# Recursive helper function to generate valid IP address
def generateIpRec(s, index, curr, cnt, res):
    temp = ""

    # Base case: Reached end of string and 
    # all 4 segments were not completed
    if index >= len(s):
        return

    if cnt == 3:
        temp = s[index:]

        # Checking 4th (last) segment of IP address
        if len(temp) <= 3 and isValid(temp):
            res.append(curr + temp)

        return

    for i in range(index, min(index + 3, len(s))):
        # Creating next segment of IP address
        temp += s[i]

        # If the created segment is valid
        if isValid(temp):
            # Generate the remaining segments of IP
            generateIpRec(s, i + 1, curr + temp + ".", cnt + 1, res)

# Function to generate valid IP address
def generateIp(s):
    res = []
    generateIpRec(s, 0, "", 0, res)
    return res

if __name__ == "__main__":
    s = "255678166"
    res = generateIp(s)
    
    for ip in res:
        print(ip)