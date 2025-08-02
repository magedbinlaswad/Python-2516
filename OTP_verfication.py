# Define the correct OTP
correct_otp = "1234"
attempts = 3

while attempts:
    user_input = input("Enter the 4-digit OTP: ")
    
    if len(user_input) != 4 :
        print("OTP must be 4 digits long. Please try again.")
    elif user_input == correct_otp:
        print("OTP verified successfully!")
        break
    else:
        attempts -= 1
        if attempts > 0:
            print(f"Incorrect OTP. You have {attempts} attempt(s) left.")
        else:
            print("Maximum attempts done, try after 24 Hours.")
