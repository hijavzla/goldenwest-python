# Laura Rodriguez-Adjunta, CS131
print('I calculate the amount of sugar, butter, and flour needed to make your desired number of cookies.')
cookies=int(input('Enter the desired amount of cookies: '))

# Determine ingredients needed per cookie 
sugarPerCookie=float(1.5 / 48)
butterPerCookie=float(1 / 48)
flourPerCookie=float(2.75 / 48)

# Given input (number of cookies) calculate amount of each ingredient needed
sugar=float(cookies * sugarPerCookie)
butter=float(cookies * butterPerCookie)
flour=float(cookies * flourPerCookie)

# Print out needed incredients
print(f'{sugar:.2f} cups of sugar.')
print(f'{butter:.2f} cups of butter.')
print(f'{flour:.2f} cups of flour.')
