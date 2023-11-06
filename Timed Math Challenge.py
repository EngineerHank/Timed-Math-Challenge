import random

OPERATORS = ['+', '-', '*', '/']
MIN_OPERAND = 2
MAX_OPERAND = 15

def generate_problem():
    left = random.randint(MIN_OPERAND, MAX_OPERAND)
    right = random.randint(MIN_OPERAND, MAX_OPERAND)
    operator = random.choice(OPERATORS)

    expr = str (left) + ' ' + operator + ' ' + str(right)
    print (expr)
    answer = eval(expr)
    return expr, answer

expr, answer = generate_problem()
print (expr, answer)
