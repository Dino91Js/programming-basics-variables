# Consider the software that runs on a self-checkout machine.

# One task that it must be able to perform is to determine how much change to provide when the shopper 
# pays for a purchase with cash.
# calcolare il resto quando si paga in contatni 
#  
# Write a program that begins by reading a number of cents from the user as an integer.
# input = numero di monete inserite come int
#   
# Then your program should compute and display the denominations of the coins that should be used 
# to give that amount of change to the shopper.
# output = calcola e visualizza il teglio delle monete che devono essere date come resto 

# **The change should be given using as few coins as possible.**
# usare il meno monete possibili 
#    
# penny 1   nickel 5    dime 10     quarter = 25    loonie = 100    toonie = 200

print("")

spesa_tot = int(input("Spesa totale "))
monete_inserite = int(input("Inserire monete "))
resto = monete_inserite - spesa_tot
print("")

if resto >= 200:
    print(resto // 200, "toonie")
resto = resto % 200

if resto >= 100: 
    print(resto // 100, "loonie")
resto = resto % 100

if resto >= 25: 
    print(resto // 25, "quarter")
resto = resto % 25

if resto >= 10: 
    print(resto // 10, "dime")
resto = resto % 10

if resto >= 5: 
    print(resto // 5, "nickel")
resto = resto % 5

if resto >= 1: 
    print(resto // 1, "penny")
resto = resto % 1

print("")


