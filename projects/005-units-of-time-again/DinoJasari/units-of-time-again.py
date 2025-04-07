# In this exercise you will reverse the process described in Exercise 4.

# Develop a program that begins by reading a number of seconds from the user.
# input = leggere e salvare in una variabile il numero del utente
# 
# Then your program should display the equivalent amount of time in the form D:HH:MM:SS, where D, HH, MM, and SS represent days, hours, minutes and seconds respectively.
# output =  restituire il dato in formato D:HH:MM:SS (giorni, ore, minuti e secondi)

# The hours, minutes and seconds should all be formatted so that they occupy exactly two digits. 
# Il formato delle ore, min e sec deve occupare 2 spazi/cifre 

# Use your research skills determine what additional character needs to be included in the format specifier
# so that leading zeros are used instead of leading spaces when a number is formatted to a particular width.
# Il formato utlizzato deve uare lo 0 al posto degli spazi quando il numero è a 1 cifra


print("")
secondi_tot = int(input("Inserire numero di secondi "))

giorni = (secondi_tot // 86400) 
secondi_rg = (secondi_tot % 86400) 

ore = (secondi_rg // 3600) 
secondi_ro = (secondi_rg % 3600) 

min = (secondi_ro // 60) 
secondi = (secondi_ro % 60) 

format = f"{giorni:02}:{ore:02}:{min:02}:{secondi:02}"
print("")
print(format)
print("")
