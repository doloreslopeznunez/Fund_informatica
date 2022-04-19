import re
strings = ["hola", "te", "hoy"]
frase = "hola como te sentis hoy?"

for palabra in strings:
    patron = palabra
if re.search(patron, frase) is not None:    
    print("la palabra esta en la frase")
else:
    print("la palabra no esta en la frase")
