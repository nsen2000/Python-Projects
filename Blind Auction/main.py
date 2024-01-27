ask = True
bidders = {}

while(ask == True):
  name = input("What is your name? ")
  bid = input("What is your bid? $")
  bidders[name] = bid
  ask = input("Are there any other bidders? Type 'yes' or 'no'. ")
  if ask == "yes":
    ask = True
  else:
    ask = False


max_bid = 0
for key in bidders:
  if int(bidders[key]) > max_bid:
    max_bid = int(bidders[key])
    max_bidder = key

print(f"The winner is {max_bidder} with a bid of ${max_bid}")
k=input("press anything to exit")