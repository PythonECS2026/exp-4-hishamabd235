# AIM: Write a Python program to calculate the simple interest based on user input.
# Coder: Hisham Shariq Abdullah
# Date: 19/02/26

# Write your code here
print("Simple Interest Calculator")

principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the rate of interest: "))
time = float(input("Enter Time Period in Years: "))

simple_interest = principal* rate* time/100

print("Simple Interest:", simple_interest)
