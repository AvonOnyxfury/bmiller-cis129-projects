
#Write a short program in Python that asks the user for the number of coffee and muffins they are purchasing.
#The price of a cup of coffee is $5 and the price of a muffin is $4.
#Calculate 6% tax on the subtotal.


#My hypothesis is that python can infer variable types and instantiate them as they are called.
#Therefore, instantiating variables is not necessary.
#Print borders and welcome statement.
print('***************************************\n\nWelcome to Net Beans!\nWhere we get all our beans from ethical bean sources. \n\n')

#Prompt user for how many coffees they want and set 'numCoffee' equal to input.
numCoffee = input('How many beans would you like? (water not included)\n')

#Set 'coffee' equal to 'numcoffee' times 5.
coffee = int(numCoffee)*8.00


#Prompt user for how many muffins they want and set 'numMuffin' equal to input.
numMuffin = input('\n\nHow many muffins would you like? \n')


#set 'coffee' equal to 'muffins' times 5.
muffin = int(numMuffin)*5.00

#Set 'total' to 'coffee' plus 'muffin'.
total = coffee + muffin


#Set 'tax' equal to the "tax on the purchase". (Multiplying by 100 not necessary.)
tax = total * 0.06


#Add 'tax' to 'total'.
total = total + tax

#Print more borders and recipt with variables included. 
print("\n*************************************** \n\n\n\
***************************************\n\n\
Net Beans recipt. \n")

print(numCoffee + " beans at $8 each (water not included, kidney beans): $" + str(coffee)+ "\n\n" + numMuffin
+ " muffins at $5 each: $" + str(muffin) + "\n\n6% tax: $"+ str(tax) +
"\n\n--------- \n\nTotal: $" + str(total)+
"\n\nEnjoy your ethically sourced beans!\n\n***************************************")
          

