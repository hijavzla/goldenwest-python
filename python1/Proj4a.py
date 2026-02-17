# Laura Rodriguez-Adjunta, CS 131
# Projecta 4a
import matplotlib.pyplot as plt

EXPENSES_FILENAME = 'proj4aexpenses.txt'
EXPENSES_CATEGORIES = ["Rent", "Gas", "Food", "Clothing", "Car Payment", "Misc"]

def main(): 
    # Explain program to user 
    print("This program reads a file with your monthly expenses and creates a pie chart display.")

    # Open file with expenses 
    expenses_file = open(EXPENSES_FILENAME, 'r')

    # Read the content 
    expenses_lines = expenses_file.readlines()

    # Close the file
    expenses_file.close() 

    # Clean up expenses lines by removing new line character at end of expenses 
    expenses_list = [item.rstrip('\n') for item in expenses_lines]

    # Create pie chart of expenses
    plt.pie(expenses_list, labels=EXPENSES_CATEGORIES)
    
    # Add title
    plt.title("Monthly expenses by category")

    # Display pie chart
    plt.show()

# Call the main function
if __name__== '__main__':
    main() 



