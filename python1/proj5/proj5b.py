# Laura Rodriguez-Adjunta, CS131
# Project 5b: Largest List Item via Recursion
FIXED_LIST = [3000, 2, 4, -2, 3, 3, 0, 1999, 8, -10000]

# Recursive function  finds the largest value in the list passed in as the argument  
def return_largest(list): 
    if len(list) == 1: 
        return list[0]
    else: 
        return max(list[0], return_largest(list[1:]))

def main(): 
    # Tell the user what the program does: 
    print(f'This program finds the largest value in this list: {FIXED_LIST}')
    

    numbers = FIXED_LIST

    # Call the function that finds the largest number in the list 
    biggest_number = return_largest(numbers)

    # Print results for the user
    print(f'The biggest number in {numbers} is {biggest_number}.')

# Call the main function
if __name__== '__main__':
    main() 