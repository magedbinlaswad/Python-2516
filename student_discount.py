# Get user input

student_name = input("Enter your name: ")
grade = int(input("Enter your grade level between (1 - 12): "))
tuition_fee = float(input("Enter your tuition fee: "))
is_topper = input("Is the student an academic topper? (yes/no): ").strip().lower()

# Validate grade
if grade < 1 or grade > 12:
    print("Invalid grade! Please enter a grade between 1 and 12.")
else:
    discount = 0
    # Determine discount based on grade level
    if grade >= 9:
        if is_topper == 'yes':
            discount = 0.20  # 20% discount for toppers in grades 9-12
        else:
            discount = 0.10  # 10% discount for non-toppers in grades 9-12
    elif grade >= 6:
            discount = 0.05  # 5% discount for grades 6-8
    else:
        discount = 0.0

    # Use match-case for additional discount
    match grade:
        case 12:
            additional_discount = 0.05  # Additional 5% discount for grade 12 students
        case 11:
            additional_discount = 0.03  # Additional 3% discount for grade 11 students
        case 10:
            additional_discount = 0.02  # Additional 2% discount for grade 10 students
        case _:
            additional_discount = 0.0  # No additional discount for other grades

# Calculate total discount and final fee 

total_discount = discount + additional_discount
discount_amount = tuition_fee * total_discount
final_fee = tuition_fee - discount_amount


# Output the results    
print(f"\nstudent name: {student_name}")
print(f"Grade level: {grade}")
print(f"academic topper status: {is_topper}")
print(f"Tuition fee: ₹{tuition_fee:.2f}")
print(f"Total discount: {total_discount * 100:.1f}%")
print(f"Discount amount: ₹{discount_amount:.2f}")
print(f"Final tuition fee: ₹{final_fee:.2f}")