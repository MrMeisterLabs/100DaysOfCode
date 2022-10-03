from replit import clear
from art import logo
from termcolor import colored

print(logo)
print("Welcome to the Auction")

auction_list = {}
winning_bid = 0

def winning_bidder(bidding_record):
    winning_bid = 0
    
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > winning_bid:
            winning_bid = bid_amount
            winner = bidder
    print(f"\n\nThe winning bid is {winning_bid}€ by {bidder}. Congrats {bidder}!")


while True:
    name = input(f"\nWhat is your name? : ")
    bid = int(input(f"\nWhat is your bid amount? : € "))
    
    auction_list[name] = bid
    print(bid)
    more_bidders = input(f"\nAre there any other bidders? Answer 'yes' or 'no' : ")

    if more_bidders == "yes":
        clear()
    else:
        break

print(auction_list)
winning_bidder(bidding_record=auction_list)

























# List the bid amount values in the dictionary that contains bidders and bid amounts
# bid_list = print(list(auction_list.values()))
# bidders_list = print(list(auction_list.keys()))
# for bid in bid_list:
#     print(f"The largest bid is {bid_list}")
