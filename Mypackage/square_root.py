import random
import math
from Mypackage.exc import excution_int_input

def square_root():
    
    num = random.choice([i**2 for i in range(1, 30)])
    print(f"What is the square root of {num}?")

    res = excution_int_input()
    return res == int(math.sqrt(num))
