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

    # Initialize the stack
    stack = []

    # Loop through the string
    for char in s:
        # If the char is an opening bracket, push it to the stack
        if char in ['(', '[', '{']:
            stack.append(char)
        # If the char is a closing bracket, pop the stack and check if the popped char is the same as the current char
        elif char in [')', ']', '}']:
            if not stack:
                return False
            if stack.pop() != char:
                return False
    # If the stack is empty, the string is valid
    return not stack

# Syntax: GOOD
# Semantic: GOOD
