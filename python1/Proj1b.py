# Laura Rodriguez-Adjunta, CS131
# Project 1b
print('Project 1b: Stock Transaction Program')
print('This program will display the profit/loss made by Joe in the stock market.\n')

COMMISSION_RATE = 0.03

sharesBought = 2000
initialCostPerShare = 40
initialTotal = sharesBought * initialCostPerShare
initialCommision = COMMISSION_RATE * initialTotal
initialBought = initialTotal + initialCommision

# Print amount of money paid for the stock and the commission paid 
print(f'Number of shares purchased: {sharesBought:,}')
print(f'Price per share purchased: ${initialCostPerShare:.2f}')
print(f'Total amount for purchased shares: ${initialTotal:,.2f}')
print(f'Total paid to broker for 3 percent commission is: ${initialCommision:,.2f}')
print(f'Joe\'s final total dollar amount bought: ${initialBought:,.2f}\n')

sharesSold = 2000
finalCostPerShare = 42.75
finalTotal = sharesSold * finalCostPerShare
finalCommission = COMMISSION_RATE * finalTotal
finalTotalWithCommission = finalTotal + finalCommission
finalSold = finalTotal - finalCommission


# Print amount of money made from selling the stock
print(f'Number of shares sold: {sharesSold:,}')
print(f'Price per share sold: ${finalCostPerShare}')
print(f'Total amount for sold shares: ${finalTotal:,.2f}')
print(f'Paid to broker 3 percent commission is: ${finalCommission:,.2f}')
print(f'Joe\'s final total dollar amount sold is: ${finalSold:,.2f}')

#Print the difference
diffAmount = finalSold - initialBought
print(f'Joe\'s difference dollar amount for sold-bought shares is: ${diffAmount:,.2f}')