import random 




def  add():
    k= random.randint(1, 100)
    y=random.randint(1, 100)
    print(f"What is {k} + {y}?")
    res = int(input("Enter your answer: "))
    return res == k + y

def subtract():
    k= random.randint(1, 100)
    y=random.randint(1, 100)
    print(f"What is {k} - {y}?")
    res = int(input("Enter your answer: "))
    return res == k - y
def multiply(): 
    y=random.randint(1, 10)
    k= random.randint(1, 10)
    print(f"What is {k} * {y}?")
    res = int(input("Enter your answer: "))
    return res == k * y
 