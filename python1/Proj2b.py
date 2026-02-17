# Laura Rodriguez-Adjunta, CS131
# Project 1b

# Project description for user
print("This program calculates population growth based on starting population, daily average increase rate, and number of days left to multiply.\n")
print("When done, enter 0 or a negative value for any input.\n")

# Get initial values from user
initial_pop = int(input("Starting number of organisms: "))
daily_increase = int(input("Average daily increase (as a %): "))
number_days = int(input("Number of days to multiply: "))

# Execute program if all inputs are greater than 0
while initial_pop > 0 and daily_increase > 0 and number_days > 0:
    
    # Print result table headers
    print("\nDay Approximate\t\tPopulation")

    # Print table values 
    for i in range(number_days): 
        # On the first day, the population is equal to initial population 
        if i == 0: 
            print(f'1\t\t\t{initial_pop}')
        
        else: 
            # Calculate new population, and set new population size
            initial_pop = initial_pop * daily_increase /100 + initial_pop
            print(f'{i + 1}\t\t\t{initial_pop:.7f}')

    # Remind user to enter 0 or negative value to exit program again
    print("\nWhen done, enter 0 or a negative value for any input.\n")

    # Prompt user for input values again
    initial_pop = int(input("Starting number of organisms: "))
    daily_increase = int(input("Average daily increase (as a %): "))
    number_days = int(input("Number of days to multiply: "))

print("\n*** Thank you for using this population calculator ***")