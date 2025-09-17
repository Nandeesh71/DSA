def evaluate_postfix(expression):
    stack = []
    operators = {'+', '-', '*', '/'}
    tokens = expression.split()

    for token in tokens:
        if token not in operators:
            stack.append(int(token))
        else:
            
            operand2 = stack.pop()
            operand1 = stack.pop()

            
            if token == '+':
                result = operand1 + operand2
            elif token == '-':
                result = operand1 - operand2
            elif token == '*':
                result = operand1 * operand2
            elif token == '/':
              
                result = int(operand1 / operand2)

            stack.append(result)

    return stack[0] if stack else None


expr = "5 1 2 + 4 * + 3 -"  
print("Result:", evaluate_postfix(expr))
