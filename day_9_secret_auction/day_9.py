from art import logo
# from replit import clear
# HINT: You can call clear() to clear the output in the console.

print(logo)
all_name_bid = {}

again = True


def highest_bidder(bidding_data):
    highest_bid = 0
    for bidder in bidding_data:
        bidding_amount = int(bidding_data[bidder])
        if bidding_amount > highest_bid:
            highest_bid = bidding_amount
            winner = bidder
    print(f"Winner is {winner} with a bid of {highest_bid}.")


while again:
    user_name = input("What is your name?: \n")
    user_bid = input("What is your bid?: \n")

    all_name_bid[user_name] = user_bid
    # print(all_name_bid)

    ask_again = input("Is there any other person? 'Yes' or 'No': \n").lower()
    if ask_again == "yes":
        # clear()
        again = True
    elif ask_again == "no":
        again = False
        highest_bidder(all_name_bid)
# print(all_name_bid)
