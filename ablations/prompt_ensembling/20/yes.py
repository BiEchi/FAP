# 20. Valid Parentheses

def isValidString(s: str) -> bool:
    """
    Description: 
        Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
        An input string is valid if:
            -- Open brackets must be closed by the same type of brackets.
            -- Open brackets must be closed in the correct order.
    Input: string -- the string with parenthesis
    Output: True -- the string with parenthesis is valid
            False -- the string with parenthesis is invalid
    Constraints:
        -- 1 <= s.length <= 104
        -- s consists of parentheses only '()[]{}'.
    Example: 
        -- Input: s = "()"
            Output: true
        -- Input: s = "()[]{}"
            Output: true
        -- Input: s = "(]"
            Output: false
    """

    # create a list to store the open parenthesis
    parenthesis = []
    # create a dictionary to store the corresponding closed parenthesis
    close = {'(': ')', '[': ']', '{': '}'}
    # iterate through the string
    for i in s:
        # if the character is an open parenthesis, append it to the list
        if i in close.keys():
            parenthesis.append(i)
        # if the character is a closed parenthesis
        else:
            # if the list is empty, return False
            if not parenthesis:
                return False
            # if the closed parenthesis doesn't match the last opened parenthesis, return False
            if close[parenthesis[-1]] != i:
                return False
            # if the closed parenthesis matches the last opened parenthesis, remove the last opened parenthesis from the list
            parenthesis.pop()
    # if the list is empty, return True; if the list is not empty, return False
    return not parenthesis

# test cases
print(isValidString('()[[{()}]'))