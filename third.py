
def palindrome(s):
    for i in range(0, len(s) // 2):
        if (s[i] != s[len(s) - 1 - i]):
            return False
    return True
print(palindrome(input()))
