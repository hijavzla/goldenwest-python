# Laura Rodriguez-Adjunta, CS131

# Set global variables
FIXED_SURCHARGE = 1.75

# Function will ask user for package count, and validate input 
def read_package_count(): 
    try: 
        # Will round down if user enters float
        num_packages = float(input('Please enter the number of packages to be sent: '))
        num_packages_int = int(num_packages)

        while num_packages_int < 0: 
            print('Package count cannot be negative.')
            num_packages = float(input('Please enter the number of packages to be sent: '))
            num_packages_int = int(num_packages)

        print(f'Number of packages to be shipped: {num_packages_int}')
        return num_packages_int

    except ValueError: 
        print('ERROR: Package number must be a valid number.')
        return 0

# Ask user for package weight and validate it, will catch error if number is not a valid number 
def read_package_weight(package_number): 
    try: 
        # Read weight as a float 
        input_weight = float(input(f'For package #{package_number} enter weight in lbs: '))
    
        # Return 0 if the weight is invalid
        if input_weight > 20.0 or input_weight <= 0: 
            print('ERROR: Invalid weight entered. Package rejected.')
            return 0    
    
        # Otherwise return the validated weight 
        else: 
            return input_weight
    except: 
        print('ERROR: Package weight must be a valid number')
        return 0

# Ask user for package zone and validate it
def read_package_zone(package_number): 
    # Read zone and convert to lower case
    input_zone = input(f'For package #{package_number} enter zone A, B, or C: ').lower()

    if input_zone == 'a' or input_zone == 'b' or input_zone == 'c': 
        return input_zone

    else:
        print('ERROR: Invalid zone entered. Package rejected.')
        return ''

# Given ALREADY validated weight and zone values, return the package cost
def calculate_cost(weight, zone): 
    # Determine weight class depending on weight entered 
    weight_class = 0 
    if weight <= 1.0: 
        weight_class = 4.25
    elif weight > 1.0 and weight <= 5.0: 
        weight_class = 8.4
    else: 
        weight_class = 17.60

    # Determine zone multiplier depending on zone entered
    zone_multiplier = 0
    if zone == 'a': 
        zone_multiplier = 1.0
    elif zone == 'b': 
        zone_multiplier = 1.15
    else: 
        zone_multiplier = 1.3
    
    # Return cost by multiplying weight class by zone multiplier and adding the fixed surcharge 
    return (weight_class * zone_multiplier + FIXED_SURCHARGE)


# Print summary of the entire shipping order for user
def print_summary(count, total, min_cost, max_cost, num_ok, num_bad): 
    print("\nSUMMARY OF SHIPPED PACKAGES")
    print(f'Total cost: ${total:.2f}')
    print(f'Total packages: {count}')
    print(f'Accepted packages: {num_ok}')
    print(f'Rejected packages: {num_bad}')
    print(f'Cheapest package cost: ${min_cost:.2f}')
    print(f'Most expensive package cost: ${max_cost:.2f}')

    # Only calculate average if more than one package is accepted  
    if num_ok > 0: 
        print(f'Average cost: ${total/num_ok:.2f}')

def main(): 
    print("This program calculates shipping costs depending on package amount, weight, and zone.")
    # Retrieve package count using function that validates user input
    package_count = read_package_count() 

    # Set up total cost accumulators, and min and max, # accepted/rejected packages, set up all variables 
    total_cost = 0
    min_cost = 0
    max_cost = 0
    num_accepted = 0
    num_rejected = 0

    # Iterate through the number of packages to be shipped
    for i in range(package_count): 
        print(f'\nNow we will collect information about package #{i+1}')

        # Get package weight, function will return 0 if weight is invalid 
        package_weight = read_package_weight(i+1)
        if package_weight == 0: 
            num_rejected += 1
        # Only will continue to else, if weight is valid 
        else: 
            # If package weight passes validation, now get package zone
            package_zone = read_package_zone(i+1)
            if package_zone == '': 
                num_rejected += 1
            # Only will continue to else if zone is valid as well 
            else:
                num_accepted += 1
                # With validated weight and zone, calculate the package cost 
                package_cost = calculate_cost(package_weight, package_zone)
                print(f'Package #{i+1} weighs {package_weight} lbs and ships to zone {package_zone} and costs ${package_cost:.2f}')

                # Update all total cost accumulator 
                total_cost += package_cost

                # Update min cost tracker
                if min_cost == 0: 
                    min_cost = package_cost
                else: 
                    min_cost = min(min_cost, package_cost)
                
                # Update max cost racker
                if max_cost == 0: 
                    max_cost = package_cost
                else: 
                    max_cost = max(max_cost, package_cost)

    # After all packages are considered, print out a summary for the user     
    print_summary(package_count, total_cost, min_cost, max_cost, num_accepted, num_rejected)

if __name__ == '__main__':
    main()