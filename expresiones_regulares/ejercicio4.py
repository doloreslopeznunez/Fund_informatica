import re
string = "Defíni la función aprobar_materias"
patron = '\w' + '_' + '\w'
re.search(patron, string) 
