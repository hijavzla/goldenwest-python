# Laura Rodriguez-Adjunta, CS131
# Project 4c Word Frequency

FILE_NAME = "Hamlet_2B_or_not_2B.txt"

# Function processes the contents of the file and prints the summary information for the user
def process_file(content): 
    # Clean up content by converting all words to lower case and replacing special characters 
    cleaned_content = content.lower().replace(':','').replace(';','').replace(',','').replace('!','').replace('?','').replace('.','').replace('-',' ')
    
    # Split content by spaces to create list of all words 
    word_list = cleaned_content.split()
    
    # Create an empty dictionary where the keys are the unique words in the dictionary, and the value will hold # of word appearances 
    dict_words = {}

    # Iterate through word list and update dictionary accordintly 
    for word in word_list:
        # Only words that are at least two characters are counted 
        if len(word) >= 2: 
            dict_words[word] = dict_words.get(word, 0) + 1
    
    # Iterate through dictionary (sorted by keys), whand print key value pairs to show how many times each word appears
    print('The following displays the number of times of each word appears: ') 
    for kv_pair in sorted(dict_words.keys()): 
        print(kv_pair, dict_words[kv_pair])


def main(): 
    print("This program reads the content of a file and prints the frequency of each word.")

    # Open the file named "Hamlet_2B_or_not_2b.txt"
    myfile = open(FILE_NAME, 'r')

    # Read the files content
    myfile_content = myfile.read()

    # Close the file 
    myfile.close() 

    # Call function to process contents of file, and print information to user 
    process_file(myfile_content)


# Call the main function
if __name__== '__main__':
    main() 