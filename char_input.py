# Create a program that asks the user to enter their name and their age.
# Print out a message addressed to them that tells them
# the year that they will turn 100 years old.

name = input('What is your name:')
age = int(input('How old are you:'))
year = str((100 - age) + 2021)

print ("Hello " + name + ", you will turn 100 in the year " + year)

# Add on to the previous program by asking the user for another number
# and printing out that many copies of the previous message.

number = int(input('Give a random number:'))

print (("Hello " + name + ", you will turn 100 in the year " + year + '\n') * number)

#Print out that many copies of the previous message on separate lines.
