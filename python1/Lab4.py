# Laura Rodriguez-Adjunta, CS131

# Global variables cost per ticket category and fixed fee 
FRONT_TICKET = 26.50
GENERAL_TICKET = 18.25
BALCONY_TICKET = 11.75
FIXED_FEE = 1.40

# Function that checks if ticket number is valid (e.g. above 0) and returns number of tickets of a given seat type which is passed as an argument 
def get_seats(seat_type): 
    # Will round down if user enters a float 
    seats_float = float(input(f'How many {seat_type} seats were sold?: '))
    seats = int(seats_float)

    while seats < 0: 
        # If the seats are negative or a float, inform the user of the error 
        print("You've entered an invalid number of seats, must be greater or equal to zero.")
        # Prompt the user again for the number of seats 
        seats = int(input(f'How many {seat_type} seats were sold?: '))

    return seats

# Function that calculates total sales depending on ticket numbers passed in 
def total_sales(front, general, balcony): 
    return (front * FRONT_TICKET) + (general * GENERAL_TICKET) + (balcony * BALCONY_TICKET)

# Function that formats dollar amounts properly with commas and decimal places
def dollars(amount): 
    return (f'{amount:,.2f}')

def main(): 
    # Describe the program to the user
    print('This program calculates total revenue for movie tickets by asking user for amount of tickets sold in each category.\n')

    # Print out the ticket price information for the user
    print('There are three categories of seating at the theater:')
    print(f'Front row seating: ${dollars(FRONT_TICKET)}')
    print(f'General seating: ${dollars(GENERAL_TICKET)}')
    print(f'Balcony seating: ${dollars(BALCONY_TICKET)}')

    # Explain the fixed fee added to all tickets
    print(f'A ${dollars(FIXED_FEE)} fixed fee is added to all tickets, regardless of category.\n')

    # Use the get_seats function to prompt user for # of seats per category, function validates user input
    front_tix = get_seats("front row")
    general_tix = get_seats("general")
    balcony_tix = get_seats("balcony")

    # Calculate totals: total tickets sold, total gross revenue, total fee revenue, and the grand total 
    total_tix = front_tix + general_tix + balcony_tix
    total_gross = total_sales(front_tix, general_tix, balcony_tix)
    total_fees = total_tix*FIXED_FEE
    grand_total = total_gross + total_fees

    # Print a category summary: for each category, print # of tickets, gross ticket sales, and fee sales 
    print("\nCATEGORY SUMMARY:")
    print(f'Front row tickets: {front_tix}\tGross: ${dollars(front_tix*FRONT_TICKET)}\tFees: ${dollars(front_tix*FIXED_FEE)}')
    print(f'General tickets: {general_tix}\tGross: ${dollars(general_tix*GENERAL_TICKET)}\tFees: ${dollars(general_tix*FIXED_FEE)}')
    print(f'Balcony tickets: {balcony_tix}\tGross: ${dollars(balcony_tix*BALCONY_TICKET)}\tFees: ${dollars(balcony_tix*FIXED_FEE)}')

    # Using the values calculated above, print overall totals
    print("\nTOTALS:")
    print(f'Total tickets sold: {total_tix}')
    print(f'Total gross revenue: ${dollars(total_gross)}')
    print(f'Total fees: ${dollars(total_fees)}')
    print(f'Grand total: ${dollars(grand_total)}')

if __name__ == '__main__':
    main()

