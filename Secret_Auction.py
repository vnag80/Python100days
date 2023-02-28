import os
auction_dictionary={}
resp = "yes"
while(resp == "yes"):
  name = input("Enter the name of the person")
  value = int(input("enter the Action value"))
  auction_dictionary[name] = value
  resp = input("Enter Would you llike to add any other 'yes' or 'no'")
  os.system('cls')
lowest_bidder = {"highest": 0}
for auction  in auction_dictionary:
    if auction_dictionary[auction] > lowest_bidder["highest"] :
        lowest_bidder["highest"] = auction_dictionary[auction]
        lowest_bidder["name"] = auction

print(f'the highest bidder is {lowest_bidder["name"]} and value is {lowest_bidder["highest"]}')
