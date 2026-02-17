# Laura Rodriguez-Adjunta, CS131
# Lab 2
print('This program calculates the cost of insulation for a house.')

length = int(input('Enter the length in feet: '))
width = int(input('Enter the width in feet: '))

area = length * width

print(f'The total area that needs to be insulated is {area} square feet.')

unfaced = int(input('How many sq ft should be insulated with UNFACED insulation (must be less than total area): '))

if unfaced > area: 
    print(f'ERROR: You cannot insulate more than {area} square feet.')
    unfaced = int(input('How many sq ft should be insulated with UNFACED insulation (must be less than total area): '))

areaLeft = area - unfaced

faced = int(input('How many sq ft should be insulated with FACED insulation: '))

if faced > areaLeft: 
    print(f'ERROR: You cannot insulate more than {area} square feet.')
    faced = int(input('How many sq ft should be insulated with FACED insulation: '))

totalCost = (faced * 1.04) + (unfaced * 1.02)

print(f'Your total insulation cost is ${totalCost:.2f}')