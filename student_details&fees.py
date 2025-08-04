# ----------- Student ID Validation ------------
valid_number = False
while not valid_number:
    student_id = input("Enter the student's ID: ")
    
    if student_id.startswith("-") and student_id[1:].isdigit():
        print("Please enter a valid positive number for Student ID.")
    
    elif student_id.isdigit():
        student_id = int(student_id)
        if student_id > 0:
            valid_number = True
        else:
            print("Please enter a valid positive number for Student ID.")
    
    else:
        print("Invalid input. Please enter a numeric Student ID.")

# ----------- Student Name Validation ------------
valid_name = False
while not valid_name:
    student_name = input("Enter the student's name: ").strip().title()
    name_check = student_name.replace(" ", "")
    
    if name_check.isalpha() and len(name_check) >= 3:
        valid_name = True
    else:
        if not name_check.isalpha():
            print("Name should only contain letters and spaces.")
        elif len(name_check) < 3:
            print("Name should be at least 3 characters long.")

# ----------- Email Generation ------------
name_parts = student_name.split()
first_name = name_parts[0].lower()
formatted_id = "STU" + str(student_id).zfill(4)
print("=" * 40)
print(f"\nFormatted Student ID: {formatted_id}")
print("Name:", student_name)
student_email = f"{first_name}.{student_id}@school.edu"
print("Email:", student_email)

# ----------- Tuition Fee Calculation ------------

tuition_fee_valid = False
while not tuition_fee_valid:
    tuition_fee = input("Enter the tuition fee amount: ")
    
    if tuition_fee.startswith("-") and tuition_fee[1:].isdigit():
        print("Please enter a valid positive number for Tuition Fee.")
    
    elif tuition_fee.isdigit():
        tuition_fee = int(tuition_fee)
        if tuition_fee > 0:
            tuition_fee_valid = True
        else:
            print("Please enter non-zero values for Tuition Fee.")
    else:
        print("Enter only numbers for Tuition Fee.")
# ----------- Discount Calculation ------------
discount = 0
print("Enter description")
description = input()
if description.lower().find("reference") != -1:
    discount += 5000
elif "scholarship" in description.lower():
    discount += 7000
elif "promo" in description:
    discount += 3000

# ----------- Final Fee Calculation ------------
final_fee = tuition_fee - discount

print(f"Basic Tuition Fee: ₹{tuition_fee}")
print(f"Total Discount: ₹{discount}")
print(f"Final Tuition Fee: ₹{final_fee}")