# Total cost

# A cupcake costs 1 dollars and 98 cents.
# Determine, how many dollars and cents should one pay for 10 cupcakes.
# It should print "total cost of 10 cupcakes is 19 dollars and 80 cents"

price = 198
numCupcakes = 10
prePrice = price * numCupcakes
priceDollars = prePrice // 100
priceCents = prePrice % 100
totalPrice = str(priceDollars) + "." + str(priceCents)
print("Price of " + str(numCupcakes) + " cupcakes: $" + str(totalPrice))





# Test if there are 20 cupcakes

price = 198
numCupcakes = 20
prePrice = price * numCupcakes
priceDollars = prePrice // 100
priceCents = prePrice % 100
totalPrice = str(priceDollars) + "." + str(priceCents)
print("Price of " + str(numCupcakes) + " cupcakes: $" + str(totalPrice))