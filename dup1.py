# Python program to remove three consecutive duplicates 

# function to remove three consecutive duplicates 

def remove3ConsecutiveDuplicates(string):
    val = ""
    i = 0
    while (i < len(string)):
        if (i < len(string) - 2 and
            string[i] * 3 == string[i:i + 3]):
            i += 3
        else:
            val += string[i]
            i += 1
            
    if (len(val) == len(string)):
        return val
    else:
        return remove3ConsecutiveDuplicates(val)

# Driver code 
string = "aabbbaccddddc"
val = remove3ConsecutiveDuplicates(string)
print(val)
