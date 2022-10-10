# Ask user for a year and check if it is a leap year

year = int(input("Please type in a year: "))

# If a year is divisible by 4, it is a leap year
if year % 4 == 0:
    # If a year is ALSO divisible by 100 and 400, it is a leap year
    if year % 100 == 0: 
        # If the year % 100 is TRUE, then run the following IF statement
        if year % 400 == 0:
            print(f"{year} is a leap year.")
        # If a year is NOT divisible by 400, it is not a leap year
        elif year % 400 != 0:
            print(f"{year} is not a leap year.")
    else:
        print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")