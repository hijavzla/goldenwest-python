# Laura Rodriguez-Adjunta, CS131
# Project 2a

print('This program calculates shipping charges based on package weight (lbs)\n')

print('To exit the program enter a weight of 0 or a negative number')
weight = float(input('To calculate shipping charges, enter the weight in lbs: '))

while weight > 0: 
    if weight <= 2: 
        print(f'Your shipping charges are ${weight * 1.50:.2f}')
    
    elif weight > 2 and weight <= 6: 
        print(f'Your shipping charges are ${weight * 3:.2f}')

    elif weight > 6 and weight <= 10: 
        print(f'Your shipping charges are ${weight * 4:.2f}')
    
    elif weight > 10 : 
        print(f'Your shipping charges are ${weight * 4.75:.2f}')

    print("\nTo exit the program enter a weight of 0 or a negative number")
    weight = float(input('To calculate shipping charges, enter the weight in lbs: '))

print('\nThank you for using this shipping calculator program!')