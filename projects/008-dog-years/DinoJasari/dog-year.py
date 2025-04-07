
# As a result, some people believe that it is better to 
# **count each of the first two human years as 10.5 dog years**     primi 2 anni umani = 10.5 anni canini
# and then **count each additional human year as 4 dog years.**     dopo primi 2 anni umani = 4 anni canini

# Write a program that implements the conversion from human years to dog years described in the previous paragraph.
# Ensure that your program works correctly for:
# - conversions of less than two human years
# - conversions of two or more human years
# L'algoritmo deve fare la conversione da anni umani a quelli canini
# input: anni umani 

# Your program should display an appropriate error message if the user enters a negative number.  
# output:   se viene inserito un numero negativo dare errore 
# 
# output:     48 human years = 205.0 dog year

print("")
anni_umani = int(input("Inserire gli anni umani da convertire "))

if anni_umani > 2:
    anni_canini = ((anni_umani - 2) * 4) + 21 
    print(anni_umani, "anni umani =", anni_canini, "anni canini")
    print("")

elif anni_umani <= 0:
    print("Per favore inserire un numero positivo diverso da 0")
    print("")

else: 
    anni_umani <= 2
    anni_canini = (anni_umani * 10.5)
    if anni_canini == 10.5:
            print(anni_umani, "anno umano =", anni_canini, "anni canini")
            print("")
    else: 
        print(anni_umani, "anni umani = 21 anni canini")
        print("")


            
            

