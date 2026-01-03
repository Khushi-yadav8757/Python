8. Valid Parentheses
s = "()[]{}"
stack = []
mp = {')':'(', ']':'[', '}':'{'}

for c in s:
    if c in mp:
        if not stack or stack.pop() != mp[c]:
            print(False)
            break
    else:
        stack.append(c)
else:
    print(True)
