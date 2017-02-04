import os
import time
import math

class bcolors:
    RED = '\033[31m'
    UNDERLINE = '\033[4m'
    ENDC = '\033[0m'
def loop():
    os.system("clear")
    calcType = int(input('What calculation would you like to do?\n1:\tAddition\t(+)\n2:\tSubtraction\t(-)\n3:\tMultiplication\t(x)\n4:\tDivision\t(/)\n5:\tSqaure Root\t(sqrt)\n6:\tSqaured\t\t(sqr)\n7:\tCubed\t\t(cbd)\n8:\tSin()\n9:\tCos()\n10:\tTan()\n\n\nPLEASE ENTER SELECTION: '))

    if calcType <= 4:
        x = float(input("Please enter your first number:\t\t"))
        y = float(input("Please enter your second number:\t"))
        
        if calcType == 1:
            z = x + y
            sign = "added to (+)"
    
        if calcType == 2:
            z = x = y
            sign = "minus (-)"
    
        if calcType == 3:
            z = x * y
            sign = "multiplied by (x)"
    
        if calcType == 4:
            z = x / y
            sign = "divided by (/)"

    if calcType >= 5:
        a = float(input("Please enter your number:\t"))

        if calcType == 5:
            b = a ** 0.5
            sign = "sqaure rooted"
                  
        if calcType == 6:
            b = a ** 2
            sign = "sqaured"
                   
        if calcType == 7:
            b = a ** 3
            sign = "cubed"
        
        if calcType == 8:
            b = math.sin(math.radians(a))
            sign = "x sin"
        
        if calcType == 9:
            b = math.cos(math.radians(a))
            sign = "x cos"
        
        if calcType == 10:
            b = math.tan(math.radians(a))
            


    if calcType <= 4:
        print("\n\n--------------------------------------\n\n\nThe value of", bcolors.RED, x, bcolors.ENDC, " ", sign, " ", bcolors.RED, y, bcolors.ENDC, " is ", bcolors.RED, bcolors.UNDERLINE, z, bcolors.ENDC)
        print("\n\n--------------------------------------\n\n")
        time.sleep(5)
        ANS = z

    if calcType > 4:
        print("\n\n--------------------------------------\n\n\nThe value of", bcolors.RED, a, bcolors.ENDC, " ", sign, " is ", bcolors.RED, bcolors.UNDERLINE, b, bcolors.ENDC)
        print("\n\n--------------------------------------\n\n")
        time.sleep(5)
        ANS = b
    
    calculation = input("Would you like to perform another calculation? Type YES or NO: ")
    if calculation == "YES":
        loop()
    else:
        quit()
loop()

