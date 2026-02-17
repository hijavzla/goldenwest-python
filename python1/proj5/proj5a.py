# Laura Rodriguez-Adjunta
# Proj5a 
import shiftsupervisor

# Display_staff_info accepts an object and shows its attributes 
def display_staff_info(staff_member): 
    # Print attributes that all employee objects have
    print(f'Name: {staff_member.get_name()}')
    print(f'Number: {staff_member.get_number()}')

    # Print attributes that only Shiftsupervisor objects have 
    if isinstance(staff_member, shiftsupervisor.Shiftsupervisor):
        print(f'Bonus: ${staff_member.get_bonus():,.2f}')
        print(f'Salary: ${staff_member.get_salary():,.2f}')

def main(): 
    # Explain program to user
    print("This program displays staff information of Employee and Shiftsupervisor objects.")

    # Create Employee object
    my_employee = shiftsupervisor.Employee('Carol Baskin', 12345)

    # Create Shiftsupervisor object 
    my_shiftsupervisor = shiftsupervisor.Shiftsupervisor('Barack Obama', 12346, 10000, 500000)

    # Display the employee data
    print('=== Regular Employees ===')
    display_staff_info(my_employee)
    # Display supervisor data
    print('=== Supervisor Employees ===')
    display_staff_info(my_shiftsupervisor)

# Call the main function
if __name__== '__main__':
    main() 
