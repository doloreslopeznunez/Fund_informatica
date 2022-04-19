import re
string = input("ingrese una cadena de caracteres: ")
patron = "^3"

if re.match(patron, string) is not None:
    print("el string comienza con el numero 3")
else:
    print("el string no emieza con el numero 3")