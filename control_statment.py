score = int(input("Enter your score (0-100): "))

# Convert score to grade symbol
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

# Use match-case to print message
match grade:
    case "A":
        print("Grade: A")
    case "B":
        print("Grade: B")
    case "C":
        print("Grade: C")
    case "D":
        print("Grade: D")
    case "F":
        print("Grade: F")