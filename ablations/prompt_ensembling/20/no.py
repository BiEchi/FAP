# 20. Valid Parentheses

def isValidString(s: str) -> bool:
    """
    Description: 
        Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
    Constraints:
        -- 1 <= s.length <= 104
        -- s consists of parentheses only '()[]{}'.
    """

    Stack = []
    HashMap = {'}':'{', ']':'[', ')':'('}
    for i in s:
        if i in HashMap:
            top_element = Stack.pop() if Stack else '#'
            if top_element != HashMap[i]:
                return False
        else:
            Stack.append(i)
    return not Stack
