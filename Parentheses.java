#Check Balanced Parentheses
def is_balanced(expr):
    stack = []
    mapping = {')': '(', ']': '[', '}': '{'}
    for char in expr:
        if char in mapping.values():
            stack.append(char)
        elif char in mapping:
            if not stack or mapping[char] != stack.pop():
                return False
    return not stack

print(is_balanced("({[]})"))  # True
