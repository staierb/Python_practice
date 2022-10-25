# Brad Staier
# 10/24/2022

"""
Practice Python
Exercise 2 -- Odd or even
The exercise comes first (with a few extras if you want the extra challenge or want to spend more time),
followed by a discussion. Enjoy!

Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user.
 Hint: how does an even / odd number react differently when divided by 2?

Extras:

    If the number is a multiple of 4, print out a different message.
    Ask the user for two numbers: one number to check (call it num) and one number to divide by (check).
    If check divides evenly into num, tell that to the user. If not, print a different appropriate message.

"""
# variables
num = int(input("Please supply a number to test: "))
check = int(input("Please supply a number to divide by: "))

# main body
if num % 2 == 0:
    print("The number you supplied is even.")
if num % 2 == 1:
    print("The number you supplied is odd.")
if num % 4 == 0:
    print("The number you supplied is also a multiple of four.")
if num % check == 0:
    print(str(num) + " is divisible by " + str(check) + ".")
if num % check != 0:
    print(str(num) + " is not divisible by " + str(check) + ".")

