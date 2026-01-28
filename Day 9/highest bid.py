import art

print(art.logo)
print("ENTER THE BID")
bids={}
next=1
bids={}

while next==1:
    name=input("Enter your name:")
    bids[name]=int(input("enter your bid: ₹"))
    next=int(input("enter 1 if you would like to continue or 0 if you would like to end: "))
    print("\n"*20)
    print(art.logo)


high={}

for key in bids:
    high[key]=bids[key]
    break

winner=''
high=0
for key in bids:
    bid_amount=bids[key]
    if bid_amount>high:
        high=bid_amount
        winner=key

print(f"The highest bid is {high} and the winner is {winner}")