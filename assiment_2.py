#input from user

tuition_fee = float(input("Enter the original tuition fee: "))
category = input("Enter Your student category (A, B, C, or others): ").upper()

#initialize discount
discount = 0

#Apply discount based on category
if category == "A":
    discount = 0.30
elif category == "B":
    discount = 0.20
elif category == "C":
    discount = 0.10
else:
    discount = 0

# calculate final fee
discount_amount = tuition_fee * discount
final_fee = tuition_fee - discount_amount

# output

print(f"\nOriginal Tuition Fee: ₹{tuition_fee: .1f}")
print(f"Discount Applied: ₹{discount_amount: .1f}")
print(f"Final Tuition Fee to Pay: ₹{final_fee: .1f}")