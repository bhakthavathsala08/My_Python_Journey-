# Tip calculator Using Number Manipulation and F Strings in Python.
print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? \n"))
tip_per = int(input("What percentage tip would you like to give? 10 12 15 \n"))
people = int(input("How many people to split the bill? \n"))
tip = (tip_per / 100) * bill
total = bill + tip
split = total / people
rounded_split = round(split, 2)
print(f"Each person should pay: ₹{rounded_split}")