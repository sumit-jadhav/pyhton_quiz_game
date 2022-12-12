# from replit import clear
import os

from art import logo
print(logo)

bids={}
bidding_finished=False

def finding_higest_bidder(bidding_record):
    highest_bid=0
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid: 
            highest_bid=bid_amount
            winner=bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")

while not bidding_finished:
    name=input("what is your name ?")
    price=int (input("what is your bid ?"))
    bids[name]=price
    should_cotinue = input("Are there any other bidders? Type 'yes or no'.")
    if should_cotinue =="no":
        bidding_finished==True
        finding_higest_bidder(bids)

    elif should_cotinue=="yes":
        os.system('cls')