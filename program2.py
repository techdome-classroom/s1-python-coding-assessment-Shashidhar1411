def decode_message(s: str, p: str) -> bool:
    
    dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]
    dp[0][0] = True  
    
    for j in range(1, len(p) + 1):
        if p[j - 1] == '*':
            dp[0][j] = dp[0][j - 1]
        else:
            break
    
    
    for i in range(1, len(s) + 1):
        for j in range(1, len(p) + 1):
            if p[j - 1] == '*':
                dp[i][j] = dp[i][j - 1] or dp[i - 1][j]
            elif p[j - 1] == '?' or p[j - 1] == s[i - 1]:
                dp[i][j] = dp[i - 1][j - 1]

    
    return dp[len(s)][len(p)]

# Example usage
print(decode_message("aa", "a"))       # Expected output: False
print(decode_message("aa", "*"))       # Expected output: True
print(decode_message("cb", "?a"))      # Expected output: False
print(decode_message("adceb", "*a*b")) # Expected output: True
print(decode_message("acdcb", "a*c?b")) # Expected output: False
