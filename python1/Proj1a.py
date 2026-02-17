# Laura Rodriguez-Adjunta, CS131
# Project 1a
print('Project 1a: Male and Female Percentages')
print('This program will calculate and print the male and female student percentages.')

men = int(input('What is the number of men registered in the class?: '))
women = int(input('What is the number of women registered in the class?: '))

studentTotal = men + women

print(f'{(men / studentTotal):.2%} of the students are men.')
print(f'{(women / studentTotal):.2%} of the students are women.')