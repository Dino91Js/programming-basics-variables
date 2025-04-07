# Develop a program that reads a four-digit integer from the user and displays the sum of its digits.
# input = numero a 4 cifre 
#  
# For example, if the user enters 3141 then your program should display 3+1+4+1=9.
# output = somma delle 4 cifre 

print("")
num_4c = (input("Inserire numero a 4 cifre "))
somma = 0

for i in num_4c:
    somma = somma + int(i)

print("")
print(somma)
print("")