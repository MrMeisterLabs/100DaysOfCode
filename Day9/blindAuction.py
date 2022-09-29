from replit import clear
from art import logo

print(logo)
print("Welcome to the Auction")

auction_list = {}

while True:
    auction_list["Name"] = input(f"\nWhat is your name? : \n")
    auction_list["Bid"] = float(input(f"\nWhat is your bid amount? : \n"))
    more_bidders = input(f"\nAre there any other bidders? Answer 'yes' or 'no' : \n ")

    if more_bidders == "yes":
        clear()
        # Build logic here
    else:
        break

print(auction_list)
