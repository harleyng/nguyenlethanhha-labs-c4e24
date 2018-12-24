from random import *

def generate_quiz():
    # Hint: Return [x, y, op, result]
    x = randint(0, 9)
    y = randint(1, 9)
    op = choice(["+", "-", "*", "/"])
    error = randint(-1, 1)

    if op == "+": 
        result = x + y
    elif op == "-":
        result = x - y
    elif op == "*":
        result = x * y
    else: 
        result = x / y
    
    result = result + error
    return x, y, op, result


def check_answer(x, y, op, result, user_choice):
    print(op)
    
    if user_choice == True:
        if op == "+": 
            if x + y == result:
                return True 
            else: 
                return False 
        elif op == "-":
            if x - y == result:
                return True 
            else:
                return False 
        elif op == "*":
            if x * y == result:
                return True 
            else:
                return False
        else: 
            if x / y == result:
                return True 
            else:
                return False
    else:
        if op == "+": 
            if x + y != result:
                return True 
            else: 
                return False 
        elif op == "-":
            if x - y != result:
                return True 
            else:
                return False 
        elif op == "*":
            if x * y != result:
                return True 
            else:
                return False
        else: 
            if x / y != result:
                return True 
            else:
                return False