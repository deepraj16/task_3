import re

def get_valid_name():
    name = input(": ").strip()
    if name.isdigit():
        raise ValueError("Invalid input: Name cannot be a number.")
    if not re.fullmatch(r"[A-Z][a-zA-Z ]*", name):
        raise ValueError("Invalid name format. Name must start with a capital letter and contain only letters and spaces.")
    return name

def excution_int_input():
    try:
        num = int(input("Enter a number: "))
        if num < 0:
            raise ValueError("Negative value not allowed.")
        return num
    except ValueError as e:
        raise ValueError(f"Invalid input: {e}")
    finally:
        print("Execution completed")
