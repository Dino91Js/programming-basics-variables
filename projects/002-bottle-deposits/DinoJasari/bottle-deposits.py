# In many jurisdictions a small deposit is added to drink containers to encourage people to recycle them.


# In one particular jurisdiction, drink containers holding one liter or less have a $0.10 deposit, and drink containers holding more than one liter have a $0.25 deposit.
# - meno di 1 litro deposito 0.10$ 
# - piu di 1 litro deposito 0.25$


# Write a program that reads the number of containers of each size from the user.
# Il programma calcola la quantità di contenitori e la grandezza 

# Your program should continue by computing and displaying the refund that will be received for returning those containers.
# Il programma calcola e visualizza il rimborso dei contenitori inseriti 


# Format the output so that it includes a dollar sign and two digits to the right of the decimal point.
# Formato output = 2 cifre dopo , e simbolo $


print ("")
minore_1l = int(input("Inserire le bottiglie di capacità inferiori a un litro "))
maggiore_1l = int(input("Inserire le bottiglie di capacità maggiori a un litro "))

somma_prezzo_bott = ((minore_1l * 0.10) + (maggiore_1l * 0.25))
totale_bottiglie = (minore_1l) + (maggiore_1l)

print("")
print("Sono state inserite " + str(minore_1l) +  " bottiglie di capacità inferiori a 1l e " + str(maggiore_1l) + " di capacità superiori a 1l")
print("")
print("Totale bottilgie inserite " + str(totale_bottiglie))
print(f"Totale {somma_prezzo_bott:.2f}$")
print("")


