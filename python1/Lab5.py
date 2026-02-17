# Laura Rodriguez-Adjunta, CS131
# Lab 5
import matplotlib.pyplot as plt

def main():
    print("This program displays a graph with three lines: y = x, y = x^2, and y = x^3, from the range of 0 to 12.5, in increments of 0.25")

    # Create an empty list 
    y_line = []

    # Append to empty list values that start at 0.0 and end at 12.50, in increments of 0.25
    for i in range(0, 1275, 25): 
        y_line.append(i/100)
    
    # Create new list via list comprehension that squares every value in original y_line list
    y_square = [item**2 for item in y_line]

    # Create new list via list comprehension that cubes every value in original y_line list 
    y_cube = [item**3 for item in y_line]

    # Plot y_line against y_line, y_square, and y_cube. Add dot markers.
    plt.plot(y_line, y_line, marker='o')
    plt.plot(y_line, y_square, marker='o')
    plt.plot(y_line, y_cube, marker='o')

    # Add title and axis labels to the graph
    plt.title('Line, Square, and Cube lines')
    plt.xlabel('x axis')
    plt.ylabel('y axis')

    # Add a grid to the graph 
    plt.grid(True)

    # Make graph appear for user 
    plt.show()

if __name__ == '__main__':
    main()