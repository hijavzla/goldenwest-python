# Laura Rodriguez-Adjunta, CS 131
# Lab 8 
import car

def main(): 
    print("This program creates a car object that is initialized with year_model, make, and speed=0. ")

    # Create car object from Car class
    my_car = car.Car("2016 iA", "Scion")

    # Accelerate 5 times, and print speed each time
    for i in range(5): 
        print("Accelerate")
        my_car.accelerate()
        print(f'Speed: {my_car.get_speed()} mph')

    # Brake 5 times, and print speed each time
    for i in range(5): 
        print("Brake")
        my_car.brake()
        print(f'Speed: {my_car.get_speed()} mph')

# Call main function
if __name__ == '__main__':
    main()