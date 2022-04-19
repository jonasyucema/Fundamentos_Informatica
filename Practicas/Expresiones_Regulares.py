# **Expresiones Regulares**
##### **Ejercicio 1** 
import re
from this import d

from jmespath import search 
cadena = 'abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYXZ0123456789'

print(re.search('\w',cadena))

##### **Ejercicio 2** 
import re 
cadena = 'abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYXZ0123456789'

print(re.findall('\w',cadena))

##### **Ejercicio 3**
import re
cadena = 'helena'
print(re.search('he'*,cadena))   

##### **Ejercicio 4**  
import re
string = "holaminombrees_jonas"
patron = '\w' + '' + '\w'
re.search(patron, string)


#####DESAFIOS
#####DESAFIO 1
Podriamos usar las expresiones regulares para agilizar el 'buscar' de alguna palabra clave en algun texto y asi ahorrarnos mas tiempo-

#####DESAFIO 2
Inicio de línea : '^palabra'

Inicio de texto : '\Apalabra'

Fin de linea : 'palabra$'

Fin de texto : 'palabra\Z'

#####DESAFIO 3

#####DESAFIO 4
\d{4}

#####DESAFIO 5
\w [3-6]

#####DESAFIO 6
\. [ab]

#####DESAFIO 7
podriamos usar re.search(), re.findall(), re.group()

#####DESAFIO 8
\d

#####DESAFIO 9
nos buscara la aparicion de 'amet' en todo el texto
#####DESAFIO 10

#####DESAFIO 11
la diferecia entre el re.search() y el re.match(), es que el match trata de 
buscar la primera aparicion de la palabra, mientras que el search lo busca 
en todo el texto

#####DESAFIO 12
La funcion .group() sirve para mostrar el resultado de una búsqueda,
en el ejercicio de resultado nos da las veces que aparece 'amet' en el texto.
 
#####DESAFIO 13
La función sub permite reemplazar todos las ocurrencias del patrón 
por otro patrón en un String.





