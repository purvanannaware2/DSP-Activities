# Infix Expression to Postfix Expression

def precedence(operator):
    if operator == '+' or operator == '-':
        return 1
    elif operator == '*' or operator == '/':
        return 2
    elif operator == '^':
        return 3
    return 0


def infix_to_postfix(expression):
    stack = []
    postfix = ""

    for char in expression:
        # If character is an operand
        if char.isalnum():
            postfix += char

        # If opening bracket
        elif char == '(':
            stack.append(char)

        # If closing bracket
        elif char == ')':
            while stack and stack[-1] != '(':
                postfix += stack.pop()
            stack.pop()

        # If operator
        else:
            while (stack and stack[-1] != '(' and
                   precedence(stack[-1]) >= precedence(char)):
                postfix += stack.pop()

            stack.append(char)

    # Pop remaining operators
    while stack:
        postfix += stack.pop()

    return postfix


expression = input("Enter infix expression: ")

print("Postfix expression:", infix_to_postfix(expression))