import random

OPERATORS = ['+', '-', '*', '/']
MIN_OPERAND = 2
MAX_OPERAND = 15
TOTAL_PROBLEMS = 10


def generate_problem():
    left = random.randint(MIN_OPERAND, MAX_OPERAND)
    right = random.randint(MIN_OPERAND, MAX_OPERAND)
    operator = random.choice(OPERATORS)

    expr = str (left) + ' ' + operator + ' ' + str(right)
    print (expr)
    answer = eval(expr)
    return expr, answer

expr, answer = generate_problem()
print(expr, answer)

for i in range(TOTAL_PROBLEMS):
    expr, answer = generate_problem()
    while True:
        guess = input("Problem #" + str(i + 1) + ": " + expr + " = ")
    print(expr, answer)
    user_answer = int(input('What is the answer? '))
    if user_answer == answer:
        print('Correct!')
    else:
        print('Incorrect! The answer is', answer)