import streamlit as st

# Sample data
students = [("Ajay", 20, "Kopargoan"), ("Ram", 90, "Pune"), ("Shyam", 22, "Mumbai")]


st.title("Student Information System")

choice = st.selectbox("Choose an option:", [
    "Show all student names",
    "Show students with marks > 80",
    "Show class topper",
    "Show students from Kopargoan"
])

if choice == "Show all student names":
    names = [s[0] for s in students]
    st.write("Student Names:", names)

elif choice == "Show students with marks > 80":
    result = [s[0] for s in students if s[1] > 80]
    if result:
        st.write("Students with marks > 80:", result)
    else:
        st.write("No students found with marks above 80.")

elif choice == "Show class topper":
    topper = max(students, key=lambda s: s[1])
    st.write("Topper:", topper[0])

elif choice == "Show students from Kopargoan":
    result = [s for s in students if s[2].lower() == "kopargoan"]
    if result:
        st.write("Students from Kopargoan:")
        for s in result:
            st.write(f"Name: {s[0]}, Marks: {s[1]}")
    else:
        st.write("No students found from Kopargoan.")
