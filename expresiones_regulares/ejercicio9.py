import re
string = "Hoy estuvimos trabajando con re -regular expression- en python -con VSCode-"
patron = "-(.*?)-"
print(re.findall(patron, string))

