# Write a program that asks the user to enter the width and length of a room.  
# input = lunghezza e larghezza 

# Once these values have been read, your program should compute and display the area of the room.
# output = area della stanza
#   
# The length and the width will be entered as **floating-point numbers**.
# input = numero con la virgola (float)  
# 
# Include units in your prompt and output message; either feet or meters, depending on which
# unit you are more comfortable working with.


print("")
print("Questo porgramma calcola l'area di una stanza i metri.")

larghezza = float(input("Inserire la larghezza della stanza "))
lunghezza = float(input("Inserire la lunghezza della stanza "))
area_stanza = larghezza * lunghezza
print("")
print(f"L'area della stanza è {area_stanza:.2f} m*2")
print("")