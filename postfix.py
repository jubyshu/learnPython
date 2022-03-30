# 后缀表达式
def infix_to_postfix(string):
    prec = {'*': 3, '/': 3, '+': 2, '-': 2, '(': 1}
    stack = []
    pf_list = []
    token_list = string.split()

    for token in token_list:
        if token in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789':
            pf_list.append(token)
        elif token == '(':
            stack.append(token)
        elif token == ')':
            top_token = stack.pop()
            while top_token != '(':
                pf_list.append(top_token)
                top_token = stack.pop()
        else:
            while len(stack) != 0 and prec[stack[-1]] >= prec[token]:
                pf_list.append(stack.pop())
            stack.append(token)
    while len(stack) != 0:
        pf_list.append(stack.pop())
    return ' '.join(pf_list)


s = '( A + B ) * C'
print(infix_to_postfix(s))


# -----------------------------

def postfix_eval(string):
    stack = []
    token_list = string.split()

    for token in token_list:
        if token in '0123456789':
            stack.append(int(token))
        else:
            operand2 = stack.pop()
            operand1 = stack.pop()
            result = do_math(token, operand1, operand2)
            stack.append(result)
    return stack.pop()


def do_math(op, op1, op2):
    if op == '*':
        return op1 * op2
    elif op == '/':
        return op1 / op2
    elif op == '+':
        return op1 + op2
    else:
        return op1 - op2

c = '7 8 + 3 2 + /'
print(postfix_eval(c))
