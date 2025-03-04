def remove_consecutive_duplicates(s):
    n = len(s)

    # Create a list to track the counts of consecutive duplicates
    dp = [0] * n
    dp[0] = 1

    result = [s[0]]

    for i in range(1, n):
        # If the current character is the same as the previous one,
        # increment the count in the dynamic programming list
        if s[i] == s[i - 1]:
            dp[i] = dp[i - 1] + 1
        else:
            dp[i] = 1

        # Append the current character to the result list
        result.append(s[i])

        # If the count reaches three, remove the last three characters
        if dp[i] == 3:
            for _ in range(3):
                result.pop()

    return ''.join(result)

if __name__ == "__main__":
    str1 = "aabbbaccddddc"
    result1 = remove_consecutive_duplicates(str1)
    print("Input:", str1)
    print("Output:", result1)

    str2 = "aabbaccddc"
    result2 = remove_consecutive_duplicates(str2)
    print("Input:", str2)
    print("Output:", result2)
    
