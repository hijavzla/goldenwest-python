# Laura Rodriguez-Adjunta, CS131
# Lab 9: Recursive List Sum 

FIXED_LIST = [1, 2, 3, 4]

# Function recursively finds the sum of values in a list and returns the sum (list must have at least 1 value in it)
def count_list(input_list): 
    # Base case that returns the value of the 0 index, if the length is equal to 1
    if len(input_list) == 1: 
        return input_list[0]
    
    # recursive call to itself but with a subset of the list starting at index 1 until the end 
    else: 
        return input_list[0] + count_list(input_list[1:]) 

def main():
    print("This program recursively calculates the sum of all the numbers in this list: [1, 2, 3, 4]")
    
    # Create list of numbers
    numbers = FIXED_LIST

    # Get the sum of the list, using the recursive function 
    print(f'The sum of the numbers is {count_list(numbers)}.')

# Call the main function
if __name__== '__main__':
    main() 