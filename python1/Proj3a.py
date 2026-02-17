# Laura Rodriguez-Adjunta, CS131
# Project 3a

# Main reads numbers in a file, calculates average, and handles exceptions   
def main(): 
    # Try to open the file 
    try: 
        # Open the file 
        num_file = open('numbers.txt','r')
        # Initialize an accumulator 
        sum = 0.0
        # Count how many numbers are counted, to calculate average later 
        digits = 0 
        for num in num_file: 
             # Try reading value from file as a float 
            try: 
                curr_num = float(num)
                sum += curr_num
                digits += 1  
            # Catch exception if value can't be convereted into a float        
            except ValueError: 
                print("Issue reading numbers from the file")
        # Close the file
        num_file.close()
        # Print the average 
        print(f'Average is: {sum/digits:.2f}')
    # Catch an exception if the file can't be opened
    except IOError: 
        print("Issue opening the file")
    except Exception as err: 
        print(err)

# Call the main function 
if __name__ == '__main__':
    main()  