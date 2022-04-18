# **Práctica de introducción a Python - Parte 2**
##### **Ejercicio 1**
palabra = input('ingresa una palabra')
if palabra = palabra.title[0]
print('la primera letra es mayuscula') 
    else:
        print('la primera letra es minuscula')

##### **Ejercicio 2**
numero = input('ingresa un numero')
if numero % 2 == 0:
    print ('es par') 
else:
    print('es impar')
if numero < 0:
    print ('El numero es negativo')
elif numero > 0:
    print('El numero es positivo')
else:
    print('El numero es cero')

##### **Ejercicio 3**
numero = input('escribi un numero del 1 al 6')
if numero < 1 or numero >6
    print('El numero ingresado es incrorecto')

##### **Ejercicio 4**
peso = input('ingrese el peso de su paquete')
if peso >5:
    print('podes pasar y el costo de tu paquete dependiendo a donde se dirija sera de:América del Sur=10.00 dólares, América Central=15.00 dólares, América del Norte=18.00 dólares, Europa=24.00 dólares, Asia=30.00 dólares')
else:
    print ('su paquete no puede ser transportado, o porque no ingreso ningun valor, o porque excede el peso permitido por nuestros terminos de seguridad')

##### **Ejercicio 5**
dia_de_la_semana = input('decime el numero del dia de una semana del 1 al 7')
dia_semana = {1: 'lunes', 2:'martes', 3:'miercoles', 4:'jueves', 5:'viernes', 6:'sabado', 7:'domingo'}
if dia_de_la_semana >7 or < 1:
    print(su numero de la semana es menor a 1 o mayor a 7)
else:
    print(dia_de_la_semana[dia_semana])

##### **Ejercicio 6**
lista1 = [1, 2, 3, 4, 5]
lista2 = [5, 4, 3, 2, 1]

lista2 = list(lista1)

##### **Ejercicio 7**
numero = int(input('Ingresa un numero'))
agregar_numero = []
while agregar_numero >0:
    agregar_numero.append(numero)
print(numero + agregar_numero)

##### **Ejercicio 8**
lista1 = [1, 2, 3, 4, 5]
lista2 = [1, 2, 3, 4, 5]
suma = 0

for i in (lista1, lista2):
    suma = suma + i
print ('el resultado es:' + suma)

##### **Ejercicio 9**
nombres = []
edades = []

nombre = input('ingresa el nombre')
edad = input('ingresa la edad')

if nombre != '*':
    print(nombre)
    elif nombre = '*'
    print('no valido')
else:
    print(max(edades)+nombres)

##### **Ejercicio 10**
diccionario = {}
cadena = input('escribi una cadena:')
for caracter in cadena:
    diccionario[caracter] +=1
else:
    diccionario[caracter] = 1
for clave, valor in diccionario.items():
    print(clave, valor)

##### **Ejercicio 11**
contadores = {}
caracter = 'predeterminado'
for letra in caracter + caracter.upper():
    contadores[letra] = 0
cadena = input('ecribi una cadena:')
for caracter in cadena:
    if caracter.lower() in caracter:
        contadores[caracter]=+1

for campo, valor in contadores.items():
    print (campo, valor)

##### **Ejercicio 12*
nombres_alumnos = input('ingresa la cantidad de alumnos:')
alumnos = {}

for numero in range(nombres_alumnos):
    alumno = input('alumno:')
    notas = []
    nota = int(input('nota:'))
    while nota >= 0:
        notas.append(nota)
        nota = int(input('nota:'))
    alumnos[alumno] = notas

for alumno in alumnos:
    print)alumno, sum(alumnos[alunmo]) / len(alumnos[alumno])

##### **Ejercicio 13**
n1 = int(input('ingresa un numero'))
n2 = int(input('ingresa otro numero'))

def esMultiplo(n1, n2):
    if (n1%n2) == 0:
        print(str(n1)+ 'es multiplo de' + str(n2))
    elif (n2%n1) == 0:
         print(str(n2) + 'es multiplo de' + str(n1))
    else:
        print('los numeros que ingresaste no son validos')



































































































































    
