# A cupcake costs 1 dollars and 98 cents.
# Determine, how many dollars and cents should one pay for 10 cupcakes.
# It should print "total cost of 10 cupcakes is 19 dollars and 80 cents"

# create a function to do above
# def calculateCost(numCupcakes)

def calcCost(numCupcakes):

    priceCake = 1.98
    totalCost = priceCake * numCupcakes
    costDollars = int(totalCost // 1)
    costCents = int(totalCost % 1 * 100)
    print("The total cost of " + str(numCupcakes) + " cupcakes is " + str(costDollars) + " dollars and " + str(costCents) + " cents.")


calcCost(10)
