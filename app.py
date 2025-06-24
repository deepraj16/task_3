students = [("Ajay", 20, "Kopargoan"), ("Ram", 90, "Pune"), ("Shyam", 22, "Mumbai")]

while True:
    print("\n1. Show all student names")
    print("2. Show students with marks > 80")
    print("3. Show class topper")
    print("4. Show students from Kopargoan")
    print("5. Exit")

    try:
        choice = int(input("Enter your choice: "))
        match choice:
            case 1:
                names = [s[0] for s in students]
                print("Student Names:", names)

            case 2:
                result = [s[0] for s in students if s[1] > 80]
                print("Students with marks > 80:", result)

            case 3:
                topper = max(students, key=lambda s: s[1])
                print("Topper:", topper[0])

            case 4:
                result = [s for s in students if s[2].lower() == "kopargoan"]
                print("Students from Kopargoan:", result)

            case 5:
                print("Exiting...")
                break

            case _:
                print("Invalid choice.")
    except ValueError:
        print("Enter a valid number.")
