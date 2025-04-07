# Create a program that reads a duration from the user as a number of days, hours, minutes, and seconds. 
# input = sequenza di 4 numeri con lo spazio in mezzo 

# Compute and display the total number of seconds represented by this duration.
# restituisci il totale in secondi 

# giorni = 86400
# ore = 3600
# minuti = 60
# secondi = 1

print("")
giorni, ore, minuti, secondi = input("Digitare la sequenza di numeri in questo ordine: giorni, ore, minuti e secondi, lasciando uno spazio tra ciascun numero " ).split()

print("")
totale_secondi = (int(giorni) * 86400) + (int(ore) * 3600) + (int(minuti) * 60) + int(secondi)

print("La somma espressa in secondi è:" , totale_secondi)
print("")