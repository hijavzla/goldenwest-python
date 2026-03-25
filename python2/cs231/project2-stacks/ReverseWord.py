# A program to reverse the letters of a word and check if it is a palindrome

from SimpleStack import *

stack = Stack(100)          # Create a stack to hold letters

word = input("Enter a word/phrase to check if it is a palindrome: ")
stripped_word = ""         # Create string to hold word stripped of non-alpha numeric characters

for letter in word:         # Loop over letters in word
   if not stack.isFull() and letter.isalpha():   # Push letters on stack if not full AND alphanumeric character
      stack.push(letter)
      stripped_word += letter
    
reverse = ''                # Build the reversed version
while not stack.isEmpty():  # by popping the stack until empty
   reverse += stack.pop()

if stripped_word == reverse:  # Check if word is a palindrome
   print("Word is palindrome!")
else: 
   print("Sorry. Word is not a palindrome.")