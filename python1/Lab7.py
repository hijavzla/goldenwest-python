# Laura Rodriguez-Adjunta, CS 131
# Lab 7 

# File to be read, must be in same directory otherwise please provide full path to file 
FILE_NAME = 'Hamlet_2B_or_not_2b.txt'

# Function processes the contents of the file and prints the summary information for the user 
def assess_file(content_string): 
    # Split string that contains the file content by spaces
    word_list = content_string.split()

    # Convert to lower case and remove all punctuation marks
    cleaned_list = [item.lower().strip('.').strip(',').strip(':').strip(';').strip('’').strip('!').strip('?').replace('’','').replace('-', ' ') for item in word_list]

    # Create a set of the unique words contained in the file
    set_words = set(cleaned_list) 

    # Create a dictionary where the keys are the unique words in the dictionary, and the value will hold # of word appearances 
    dict_words = {}

    # Initialize word count: for each word in the set containing the unique words, add a dictionary element with an initial value of 0 
    for word in set_words: 
        dict_words[word] = 0

    # Iterate through the cleaned list, for each word, update the dictionary with +1 to account for the word appearing another time
    for value in cleaned_list: 
        dict_words[value] = dict_words[value] + 1
    
    # Iterate through dictionary (sorted by keys), whand print key value pairs to show how many times each word appears
    print('The following displays the number of times of each word appears: ') 
    for kv_pair in sorted(dict_words.keys()): 
        print(kv_pair, dict_words[kv_pair])

    # Print number of unique words by counting the length of the set containing the unique words 
    print(f'\nNumber of unique words: {len(set_words)}')

    # Print number of total words by counting the length of the list containing all the words in the file 
    print(f'Number of total words: {len(cleaned_list)}')


def main():
    # Explain program to the user 
    print("This program reads a file and prints the number of times each word appears, the total number of unique words, and the total number of words.\n")

    # Open the file named "Hamlet_2B_or_not_2b.txt"
    myfile = open(FILE_NAME, 'r')

    # Read the files content
    myfile_content = myfile.read()

    # Close the file 
    myfile.close() 

    # Call function to process contents of file, and print information to user 
    assess_file(myfile_content)

# Call the main function
if __name__== '__main__':
    main() 

