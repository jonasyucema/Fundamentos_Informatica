##### **Ejercicio 1**
from os import terminal_size
from platform import python_branch


leer = open('Ejemplo')
caracter = leer.readline(1)
while caracter != "P":
    print(caracter)
leer.close()
    
##### **Ejercicio 2**
with open('Ejemplo', 'r') as file: 
    contentList = file.readlines()
    for i in range(len(contentList) + n), len(contentList):
        print(contentList[i])

##### **Ejercicio 3**
with open('Ejemplo', 'r') as file: 
    contentList = file.readlines() 
    for i in range(len(contentList) - n), len(contentList): 
        print(contentList[i])

def read_n_back_lines(n, archivo): 
    texto = open(archivo, "r").readlines()
    for i in range((len(texto) -n), len(texto)):
        print(texto[i])
    texto.close()

##### **Ejercicio 4**
with open('Ejemplo', 'r') as file: 
    fileContent = file.readlines()
    print(len(fileContent)) 

##### **Ejercicio 5**
with open('Ejemplo', 'r') as file: 
    fileContent = file.readlines()

for fileline in fileContent: 
    fileline = fileline.replace('w', 'w \n')

with open('Ejemplo', 'a') as file: 
    for i in fileContent:
        file.write(i) 
##### **Ejercicio 6**
-
##### **Ejercicio 7**
def palabra_mas_larga(archivo): 
    palabra = '' 
    max_long = 0
    with open(archivo, 'r') as f: 
        lista_palabra = f.read().split()
        for word in lista_palabra:
            if len(word) > max_long: 
                max_long = len(word)
    print(max_long) 
##### **Ejercicio 8**
-
##### **Ejercicio 9**
def word_counter(archivo): 
    frecuencias = dict() 
    with open(archivo, 'r') as miArchivo: 
        word_list = miArchivo.read().split() 
        for palabra in word_list:
            if palabra in frecuencias: 
                frecuencias[palabra] += 1
            else: 
                frecuencias[palabra] = 1 
        for word in frecuencias.keys(): 
            frecuencias[word] = round(frecuencias[word] / len(word_list),3)
    print(frecuencias) 

##### **EJERCICIO 10**
def join_files(file1, file2, file3): 
    with open(file1, 'r') as f1, open(file2, 'r') as f2, open(file3, 'a') as f3: 
        f3.write(f1.read() + f2.read())

join_files('documento1', 'documento2', 'documento3')

#####DESAFIOS
#####DESAFIO 2
os.mkdir() nos permite crear directorios en python, y os.listdir() seria algo 
asi como un ls en nuestra terminal. el os.listdir() nos mostrara los nombres 
de los archivos y directorios.

#####DESAFIO 3

with open ('manipulacion_archivos.txt', 'r') as files:
    fileContent = files.readlines()
    print('resultado')

podriamos leer los archivos de esta forma tambien:

leer = open('texto')
caracter = leer.readlines()
leer.close()