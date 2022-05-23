import re
texto1 = "Esta es la linea uno\npalabra en la linea dos\n"
patron1="\A(E)"
patron2="[2]"
coincidencias=re.findall(patron1, texto1)
print(coincidencias)
print(len(coincidencias))

# ^ cuando esta afuera del corchete,