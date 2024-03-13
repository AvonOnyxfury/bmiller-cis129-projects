#Bryce Miller
#Brittany Griwzow
#Prog and Problem Solving
#3/9/2024

#Lab 5, Bottle Return.

#This script is meant to simulate a bottle return program.
#It counts how many bottles per day were collected.
#Then it calculates how much payout the program gets from the total collection.
#It collects input on the amount of bottles collected each day for 7 days.
#Then after counting 7 days, it prints out the total as well as the payout.
#It then asks the user if they want to do it again for another week.
#It repeats if the user types 'y'.
#payout is 10 cents per bottle per week.

#It is important to declare proper variable's first.
#counter controls a while loop so it repeats 7 times
#keepGoing decides if the program should continue
keepGoing = 'y'
counter = 0
todayBottles = 0
totalBottles = 0
totalPayout = 0

#create keepGoing loop to make the program run indefinitely.
while keepGoing == 'y':
   
    #reset variables
    counter = 0
    todayBottles = 0
    totalBottles = 0
    totalPayout = 0 
    #create loop for 7 days (it's decreased due to the count updating first.)
    while counter <= 6:
        #count up 1 first so that prompts start on day 1 not 0
        counter = counter + 1
        #collect today bottles in input and calculate others accordingly
        todayBottles = int(input(f'Enter number of bottles for day #{counter}: '))
        #calculate total bottles
        totalBottles += todayBottles
    #calculate totalPayout
    totalPayout = totalBottles / 10    
    #print everything out        
    print(f'\nThe total number of bottles collected is', totalBottles,
          '\nThe total paid out is $ ', totalPayout)
    #Ask if the user wants to go again
    keepGoing = input('\nDo you want to enter another week’s worth of data?\n(Enter y or n): ')
    print()





