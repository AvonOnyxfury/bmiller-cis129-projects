# Module 4 Lab-4
# Bryce Miller
# 2/27/2024

# This program is meant to calculate store budget bonuses and employee
# bonuses based on store performance. Each type of bonus has multiple tiers.
# Store budget is based on total monthly sales. Wheras individual employee
# bonuses are awarded based on the percent increse in sales
# presumably since the month before.

# A store that sells over or equal to $110,000 worth of stuff gets $6,000.
# A store that sells over or equal to $100,000 worth of stuff gets $5,000.
# A store that sells over or equal to $90,000 worth of stuff gets $4,000.
# A store that sells over or equal to $80,000 worth of stuff gets $3,000.
# Any sales under that gets nothing.

# 5% or over sales increase gets employees an extra $75.
# 4% or over sales increase gets employees an extra $50.
# 3% or over sales increase gets employees an extra $40.
# Employees get nothing for anything under that.

# declare local variables. variables must be defined before they can be compared.
monthlySales = 0 #monthly sales amount dollars
storeAmount = 0 # store bonus amount dollars
empAmount = 0 # employee bonus amount dollars
salesIncrease = 0 # percent increase in sales. float 0.01 is 1%
prompt1 = 'Enter the monthly sales: $' # string literal
prompt2 = 'Enter percent of sales increase: ' # string literal

#Input: Ask user for monthly sales and set monthlySales equal to input.

monthlySales = float(input(prompt1))

#Processing: determine storeAmount, the amount of store bonus

if monthlySales >= 110000:
    storeAmount = 6000
elif monthlySales >= 100000:
    storeAmount = 5000
elif monthlySales >= 90000:
    storeAmount = 4000
elif monthlySales >= 80000:
    storeAmount = 3000
else: storeAmount = 0

#Input: Ask user for increase in sales set salesIncrease equal to input.
#Processing: turn Input into a percent
salesIncrease = float(input(prompt2))
salesIncrease = salesIncrease / 100

#Processing: determine empAmount, the employee bonus

if salesIncrease >= 0.05:
    empAmount = 75
elif salesIncrease >= 0.04:
    empAmount = 50
elif salesIncrease >= 0.03:
    empAmount = 40
else:
    empAmount = 0

#Output: print it all out nicely.
print("The store bonus amount is $", storeAmount)
print("The employee bonus amount is $", empAmount)
#Processing/Output: Congratulate user for productivity.
if ( storeAmount == 6000 ) and (empAmount == 75):
    print('Congrats! You have reached the highest bonus amounts possible! ')
