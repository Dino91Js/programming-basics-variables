# A bakery sells loaves of bread for €3.49 each. 
# Day old bread is discounted by 60 percent.
# Pane fresco = €3.49       Pane vecchio = 3.49 scontato 60 %  
#
# Write a program that begins by reading the number of loaves of day old bread being purchased from the user.
# input = numero di pane vecchio comprato 

# Then your program should display the regular price for the bread, the discount because it is a day old, and the total price.
# output = prezzo intero, quanto è lo sconto e il prezzo totale 
#  
# Each of these amounts should be displayed on its own line with an appropriate label.
# ogni prezzo su una riga separata 

# All of the values should be displayed using two decimal places, 
# and the decimal points in all of the numbers should be aligned when reasonable values are entered by the user.
# format = 3.00€ (2 cifre dopo ,) allineati orizzontalmente 

print("")
print("Prezzo pane fresco €3.49 (al pezzo). Il pane di ieri è scontato del 60% ")
print("")
pezzi_pane = int(input("Inserire il numero di pezzi "))
print("")

prezzo_intero = pezzi_pane * 3.49
sconto = prezzo_intero * 60 / 100 
totale = prezzo_intero - sconto

print(f"{"Prezzo intero:":<20} {prezzo_intero:.2f}€")
print(f"{"Sconto:":<20} {sconto:.2f}€")
print(f"{"Totale spesa:":<20} {totale:.2f}€")
print("")

