password = "123"
user_input = ""
while user_input != password:
    user_input = input("Enter the password: ")
    if user_input == password:
        print("Access granted.")
    else:
        print("Access denied. Please try again.")


print("=====================================")


i=1
while i <= 20:
    if i % 2 == 0:
        print(i)
    i += 1

print("=====================================")

i = 2
while i <= 20:
     print(i)
     i += 2

print("=====================================")

for i in range(2, 21,2):
    print(i)

print("=====================================")


print("=====================================")

i = 1
while i <= 10:
    j = 1
    while j <= 10:
        print(f"{i} x {j} = {i * j}")
        j += 1
    i += 1

print("=====================================")




