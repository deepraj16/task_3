from random import choice
from Mypackage.exc import get_valid_name
from Mypackage.square_question import square_question
from Mypackage.square_root import square_root
from Mypackage.Arith import add, subtract, multiply
from Mypackage.save_json import save_score
import time
score = 0

print("Enter the name: ")
name = get_valid_name()
print("User name:", name)


while True:
    
    functions = [square_question, square_root,square_root,add, subtract, multiply,add]

    chosen_function = choice(functions)
    print("Question:")
    k=time.time()

    try:
        if chosen_function():
            score += 10
        else:
            score -= 5
    except Exception as e:
        print(f"Error during function execution: {e}")
        score -= 5
    m=time.time()
    y=m-k
    print("Time taken:",round(y,2),"seconds")
    print("Score:", score)
    print()

    ch = input("Do you want to continue to another question (yes/no)? ").strip().lower()
    if ch != "yes":
        break
    else:
        print("Continuing to the next question...")

save_score(name, score)
print(f"{name} is the Loser")
print("Final Score:", score)
