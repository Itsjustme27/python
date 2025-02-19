# Function to calculate total marks
def mark(subject_marks):
    total = sum(subject_marks)
    return total

# Function to calculate average (percentage)
def average(total, num_subjects):
    return total / num_subjects

# Function to calculate grade based on percentage
def grade(percentage):
    if 80 <= percentage <= 100:
        return "A+"
    elif 75 <= percentage <= 79:
        return "A"
    elif 70 <= percentage <= 74:
        return "B+"
    elif 65 <= percentage <= 69:
        return "B"
    elif 60 <= percentage <= 64:
        return "C+"
    elif 55 <= percentage <= 59:
        return "C"
    elif 50 <= percentage <= 54:
        return "C-"
    elif 40 <= percentage <= 49:
        return "D"
    else:
        return "F"

# Function to display student details and results
def display(name, tp_number, total, percentage, grade_value):
    print("\n----- Student Report -----")
    print(f"Name: {name}")
    print(f"TP Number: {tp_number}")
    print(f"Total Marks: {total}")
    print(f"Percentage: {percentage:.2f}%")
    print(f"Grade: {grade_value}")

# Main Program
name = input("Enter Student's Name: ")
tp_number = input("Enter TP Number: ")

# Input for subjects
subject_marks = []
num_subjects = int(input("Enter number of subjects: "))

# Getting marks for each subject
for i in range(num_subjects):
    while True:
        try:
            mark_input = int(input(f"Enter marks for Subject {i+1}: "))
            if 0 <= mark_input <= 100:
                subject_marks.append(mark_input)
                break
            else:
                print("Marks should be between 0 and 100. Try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

# Calculations
total_marks = mark(subject_marks)
percentage = average(total_marks, num_subjects)
grade_value = grade(percentage)

# Displaying the results
display(name, tp_number, total_marks, percentage, grade_value)

