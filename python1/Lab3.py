# Laura Rodriguez-Adjunta, CS131
# Lab 3

print('This program makes a triangular shape where the height equals the base size entered.')
BASE_SIZE = int(input("Enter base size (integer no larger than 10): "))


# Make sure input is between 1 and 10
while BASE_SIZE > 10 or BASE_SIZE < 1: 
    print('Please choose an integer between 1 and 10')
    BASE_SIZE = int(input("Enter base size (integer no larger than 10): "))

# Build the first half of the shape
for r in range(BASE_SIZE):
    for c in range(r + 1):
        print('*', end='')      
    if r == 0: 
            print(' BOTTOM',end='')
    if r == BASE_SIZE - 1: 
            print(' TOP',end='')
    print()

# Build the second half of the shape
for r in range(BASE_SIZE-1, 0, -1):
    for c in range(r): 
        print('*',end='')
    if r == 1: 
            print(' BOTTOM',end='')
    print()