# 5. Longest Palindromic Substring

def longestPalindrome(s: str) -> str:
    """
    Given a string s, return the longest palindromic substring in s.
    """

    answer = ""
    max_val = 0
    lens = len(s)
    # complete the part below
    for i in range(len(s)):
        for j in range(i,lens):
            if isPalindromic(s[i:j+1]):
                if len(s[i:j+1]) > max_val:
                    answer = s[i:j+1]
                    max_val = len(s[i:j+1])


    
def isPalindromic(s: str) -> bool:
    """
    Description: decide whether the string is a palindromic substring or not
    Input: s -- a string (not sure whether it's palindrome or not)
    Output: a booling value -- True for palindromic s, False for not
    Constraints: the length of the input string is not decided
    """

    lens = len(s)
    for i in range(lens//2):
        if s[i] != s[lens-i-1]:
            return False
    return True
