import re
texto1 = "A la grande le puse -Cuca-, 123456789"
patron1="[A-Z0-9a-z]+"
patron2="[2]"
coincidencias=re.findall(patron1, texto1)
print(coincidencias)
print(len(coincidencias))
