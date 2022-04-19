import re
string = input("escriba algo: ")
patron = '\d'
lista = []

for caracter in string:
    lista=re.findall(patron, string)
    print(lista)
    

