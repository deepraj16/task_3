import random
from Mypackage.exc import excution_int_input

def square_question():
    num = random.randint(1, 100)
    print(f"What is the square of {num}?")

    res = excution_int_input()
    return res == num ** 2
