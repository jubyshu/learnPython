s = '([({[()]})]))'


def pair_bracket(string):
    stack = []
    rules = {
        '(': ')',
        '[': ']',
        '{': '}'
    }
    for s in string:
        if s in {'(', '[', '{'}:
            stack.append(s)
        else:
            if len(stack) == 0:
                return False
            elif s == rules[stack[-1]]:
                stack.pop()
            else:
                return False
    if len(stack) == 0:
        return True
    else:
        return False


print(pair_bracket(s))
