# Laura Rodriguez-Adjunta, CS131
# Lab 6

# Global constant list holds all month names in order, and month number is the index 
MONTH_LIST = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

# This function validates month entered by user and returns True if validation passes, otherwise it prints an error and returns False 
def validate_month(month):
    # Convert month string into an integer, leading zeros will be stripped 
    month_int = int(month)
    
    # Check that month string is between values of 1 and 12
    if month_int < 1 or month_int > 12: 
        print("ERROR: invalid month")
        return False
    
    return True 

# This function validates day entered by user and returns True if validation passes, otherwise it prints an error and returns False 
def validate_day(day):
    # Convert day string into an integer, leading zeros will be stripped
    day_int = int(day)

    # Check that day is between values of 1 and 31
    if day_int < 1 or day_int > 31:
        print('ERROR: invalid day')
        return False
    
    return True

# This function validates year entered by user and returns True if validation passes, otherwise it prints an error and returns False
def validate_year(year): 
    year_int = int(year)

    if year_int < 1 or year_int >= 10000: 
        print('ERROR: invalid year')
        return False

    return True 

# This function converts validated month, day, and year strings to new format: Month Day, Year. 
def convert_format(month, day, year):

    # Retrieve month from stored list 
    month_conversion = MONTH_LIST[int(month) - 1] 
    
    # Check year, if less than 4 integers, then assume it is 21st century
    if len(year) == 3:
        year = '2' + year
    if len(year) == 2: 
        year = '20' + year
    if len(year) == 1: 
        year = '200' + year
    
    print(f'This is a valid date: {month_conversion} {day}, {year}')


def main(): 
    # Explain the program to the user
    print('This program converts dates from a mm/dd/yyyy format to new format: Month Day, Year.')

    # Initiate variable to control loop
    ask_again = 'y'
    
    while ask_again.lower() == 'y':

        # Ask user for input date, and split by '/'
        date = input('\nEnter your date in this format month/day/year: ').split('/')

        # Set month, day, year by retrieving them from the created list
        month = date[0]
        day = date[1]
        year = date[2]

        # Only convert format if month, day, and year pass validation checks 
        if validate_month(month) and validate_day(day) and validate_year(year): 
            convert_format(month, day, year)
        
        # Ask user if they would like to convert another date
        print("\nWould you like to convert another date?")
        ask_again = input('Type \'y\' for yes, anything else for no: ')
            

if __name__ == '__main__':
    main()


