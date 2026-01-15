import logo
print(logo.logo)
def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    return winner
bidders={}
choice="yes"
while choice == "yes":
        name = input("Enter your name: ")
        bid = int(input("Enter your bid amount: $"))
        bidders[name] = bid
        choice = input("Are there any other bidders? Type 'yes' or 'no'. ").lower()
        print("\n" * 50)
        if choice == "no":
            highest_bidder = find_highest_bidder(bidders)
            print(f"The winner is {highest_bidder} with a bid of ${bidders[highest_bidder]}")

            
# we can also use the max function with a key argument to find the highest bidder
# highest_bidder = max(bidders, key=bidders.get)