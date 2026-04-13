def is_balanced_paranthesess(Stack):
    stack=Stack()
    for ch in Stack:
        if ch=='(':
            stack.push(ch)
        elif ch==')':
            if stack.is_empty():
                return False
            stack.pop()
    return stack.is_empty()
print(is_balanced_paranthesess("((()))"))
