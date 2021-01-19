# Ask the user for a number. Depending on whether the number is even or odd
# print out an appropriate message to the user.

number = int(input('Give a number:'))
check = int(input('Give a number to divide by:'))

if (number % 4) == 0:
    print (str(number) + ' is a multiple of 4')

# If the number is a multiple of 4, print out a different message.

elif (number % 2) == 0:
    print (str(number) + ' is an even number')

else:
    print (str(number) + ' is an odd number')

#If check divides evenly into num, tell that to the user.
#If not, print a different appropriate message.

if number % check == 0:
    print (str(number) + ' divides evenly by ' + str(check))

else:
    print (str(number) + ' does not divide evenly by ' + str(check))
