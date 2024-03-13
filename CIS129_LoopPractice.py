#Bryce Miller
#Brittany Griwzow
#Prog & Problem Solving 1
#3/11/2024

#define function, main
def main():
    while True:
        userNumber = get_integer('Enter a num: ')
        #1.b. tell user whether input is even or odd.
        if (userNumber % 2 == 0):
            print('The number is even!')
        else:
            print('The number is odd!')
        #1.c ask the user if they want to do it again
        #using a decision structure and a loop
        print('do you want to do it again?')
        again = input('enter \'y\' to loop again: ')
        if again != 'y':
            break
    print('The loop has ended')

#input validation
def get_integer(message):
    while True:
        try:
            user_input = int(input(message))
            return user_input
        except ValueError:
            print('Incorrect data entered, please re-attempt')
            
main() #dont forget to call main!

