#import math

# Welcome message

print("Welcome to the tip calculator.")

# Get the bill amount

bill = float(input("What was the total bill? : €"))

# Ask about how many people are splitting the bill

people = int(input("How many people to split the bill? : "))

# Get the tip percentage

tip = int(input("What percentage tip would you like to give? 10, 12, or 15? : "))

# Calculate the bill split amount per person

split = round((((bill * tip/100) + bill) / people), 2)

print(f"Each person should pay: €{split}")