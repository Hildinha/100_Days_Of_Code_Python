# This is a simple python script that was made at 100 Days Of Code on day 2
print("Welcome to the tip calculator.")
total_bill = float(input("What was the total bill? $"))
tip_percentage = int(input("How much tip would you like to give? 10, 12, or 15? "))
tip_division = int(input("How many people to split the bill? "))
total_bill += round(total_bill * (tip_percentage / 100), 2)
tip_per_person = round(total_bill / tip_division, 2)
print(f"Each person should pay: ${tip_per_person}")
