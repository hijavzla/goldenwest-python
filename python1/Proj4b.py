# Laura Rodriguez-Adjunta, CS131
# Project 4b

def main(): 
    # Explain program to user
    print("This program prints the sum of the digits in a string of numbers, e.g. 1234 will print 10")

    # Prompt the user for a string of numbers
    input_string = input("Input string of numbers: ")

    # Initialize variable to hold sum
    sum = 0 

    # Loop through string to add digits 
    for i in input_string: 
        sum += int(i)
    
    # Print sum of all numbers
    print(f'The sum is {sum}')

# Call the main function
if __name__== '__main__':
    main() 