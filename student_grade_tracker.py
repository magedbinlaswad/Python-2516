# Collect Student Information
student_id = input("Enter Student ID: ")
student_name = input("Enter Student Name: ")
attendance = float(input("Enter Attendance percentage (%): "))

# Initialize variables
num_subjects = 0
total_score = 0

# Input Subject Scores
while True:
    score = float(input(f"Enter score for subject {num_subjects + 1}: "))
    total_score += score
    num_subjects += 1
    
    cont = input("Do you want to enter another score? (yes/no to continue, any other key to stop): ")
    if cont.lower() != 'yes':
        break

# Calculate Average Score
average_score = total_score / num_subjects

# Determine Performance Level
if average_score >= 85:
    performance = "Excellent"
elif average_score >= 70:
    performance = "Good"
elif average_score >= 50:
    performance = "Average"
else:
    performance = "Needs Improvement"

# Check Attendance Status
attendance_status = "OK Attendance Satisfied" if attendance >= 75 else "WARNING Low Attendance"

# Display Final Results
print("\n==== Student Grade Tracker ====")
print(f"Student ID: {student_id}")
print(f"Student Name: {student_name}")
print(f"Total Score: {total_score}")
print(f"Average Score: {average_score:.2f}")
print(f"Performance Level: {performance}")
print(f"Attendance: {attendance}% - {attendance_status}")