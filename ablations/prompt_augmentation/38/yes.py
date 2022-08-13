# 38. Count and Say

def countAndSay(n: int) -> str:
    """
    Description: 
        -- The count-and-say sequence is a sequence of digit strings defined by the recursive formula:
            -- countAndSay(1) = "1"
            -- countAndSay(n) is the way you would "say" the digit string from countAndSay(n-1), which is then converted into a different digit string.
        -- To determine how you "say" a digit string, split it into the minimal number of substrings such that each substring contains exactly one unique digit. 
            Then for each substring, say the number of digits, then say the digit. Finally, concatenate every said digit.
    Input: A positive integer n.
    Output: The n-th term of the count-and-say sequence.
    Constraints: 1 <= n <= 30
    Examples: 
        -- 
        Input: n = 1
        Output: "1"
        Explanation: This is the base case.

        --
        Input: n = 4
        Output: "1211"
        Explanation:
            countAndSay(1) = "1"
            countAndSay(2) = say "1" = one 1 = "11"
            countAndSay(3) = say "11" = two 1's = "21"
            countAndSay(4) = say "21" = one 2 + one 1 = "12" + "11" = "1211"
    """

    res = "1"
    for i in range(1, n):
        count, say, temp = 1, "", res[0]
        for j in range(1, len(res)):
            if res[j] == temp:
                count += 1
            else:
                say += str(count) + temp
                temp = res[j]
                count = 1
        say += str(count) + temp
        res = say
    return res

# Syntax: GOOD
# Sementic: GOOD
