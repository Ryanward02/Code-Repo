#Question:

#Write a program that calculates and prints the value according to the given formula:
#Q = Square root of [(2 * C * D)/H]
#Following are the fixed values of C and H:
#C is 50. H is 30.
#D is the variable whose values should be input to your program in a comma-separated sequence.

#Example
#Let us assume the following comma separated input sequence is given to the program:
#100,150,180
#The output of the program should be:
#18,22,24

import math
C = 50
H = 30

D = input("Please enter the numbers in a comma separated sequence: ")

x = D.split(",")
val = []

for i in x:
    val.append(int(math.sqrt(2 * 50 * float(i)/ 30)))
    
newstring = str(val)

print(newstring[1:len(newstring)-1])
