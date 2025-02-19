enter_details = True
name_arr = []
score_arr = []

print("Student report analyzing... Enter Q to quit")

while enter_details:
    student_name = input("\nEnter Student Name or Q to quit: ")
    if student_name == "Q":
        confirm = input("Are you sure? (Y/n) : ")
        if confirm.lower() == "y":
            enter_details = False
            break

    student_score = input("Enter Student Score or Q to quit: ")
    if student_score == "Q":
        confirm = input("Are you sure? (Y/n) : ")
        if confirm.lower() == "y":
            enter_details = False
            break
    
    # Convert score to integer and check the range
    try:
        student_score = int(student_score)
        if 0 <= student_score <= 100:
            name_arr.append(student_name)
            score_arr.append(student_score)
        else:
            print("Score should be between 0 to 100")
    except ValueError:
        print("Invalid score. Please enter a number.")

# Calculate and print the average
if score_arr:
    avg = sum(score_arr) / len(score_arr)
    print(f"\nAverage Score: {avg}")
else:
    print("\nNo scores to calculate an average.")

