#################LISTAS####################
###########################################
my_lista = ['Rojo', 'Azul', 'Amarillo', 'Naranja', 'Violeta', 'Verde']  #Crea una lista llamada my_lista con sus elementos ordenados del 0 al 5
#input()   
print(my_lista)  #Muestra en pantalla todos los elementos de la lista
print(type(my_lista))  #Muestra el tipo de dato de my_lista imprimiendo <class 'list'>
print(my_lista[2])  #Imprime el elemento que se ubica en la posicion 2 de la lista, en este caso Amarillo 

print("my_lista size: ", len(my_lista))  #len() calcula la cantidad de elementos que tiene la lista y muestra en pantalla el comentario 
print(my_lista[0:2])  #Muestra una porcion de la lista desde el 0 hasta el 2 (Rojo, Azul)
print(my_lista[:2])  #Hace lo mismo que la linea anterior pero cuando se omite el primer número python comienza desde el 0 

my_lista.append('Blanco')      #Agrega elemento al final de la lista llamado Blanco
print(my_lista)  #Imprime la lista con el nuevo elemento

my_lista.insert(3, 'Negro')  #Inserta Negro en el indice 3 y desde esa posicion los demas elementos se desplazan a la derecha
print(my_lista)  #Muestra la lista despues de insertar Negro


my_lista.extend(['Marron', 'Gris'])   #Agrega dos elementos nuevos a la lista
print(my_lista)  #Muestra la lista con los dos nuevos elemetos

print(my_lista.index('Azul'))  #Busca la posicion donde se encuentra Azul y lo imprime en pantalla

#my_lista.remove('Magenta')  #Comentario
my_lista.remove('Marron')  #Busca el elemento Marron y lo elimina de la lista
print(my_lista)  #Imprime la lista despues de eliminar Marron

my_lista.insert(8, 'Marron')  #Vuelve a insertar Marron en el indice 8 de la lista 
print(my_lista)  #Imprime nuevamente la lista

print(my_lista.pop())  #pop() elimina y devuelve el ultimo elemento de la lista y se imprime en pantalla
size = len(my_lista)  #Calcula la cantidad de elementos que quedan en la lista y lo guarda en size
print("size = ", size)  #Muestra en pantalla el tamaño de la lista 
#print(my_lista.pop(size))  #Comentario

my_lista_3 = my_lista*3  #Se crea una nueva lista en donde se repiten 3 veces todos los elementos de la lista original
print("my_lista_3: ", my_lista_3)  #Muestra la nueva lista repetida

print("Sort:")  #Imprime Sort:
print()  #Linea vacia para mejor presentación
my_listaSort = my_lista.sort()  #Ordena my_lista en orden alfabético.
print(my_listaSort)  #Se imprime none ya que sort() modifica la lista original

my_NumList = [10, 9, 8, 7, 6 , 5 , 4, 3, 2, 1]  #Crea una lista de numeros enteros ordenados de mayor a menor
print("Ordering my_NumList: ")  #Imprime un mensaje indicando que se va a ordenar la lista de números
my_NumList.sort()  #Ordena los elementos de my_NumList de menor a mayor
print(my_NumList)  #Muestra en pantalla la lista ordenada de menor a mayor
#OrderedLList = my_NumList.sort()  #Comentario

#print(my_listaSort)  #Comentario

#Ordenando lista de mayor a menor
my_NumList.sort(reverse = True)  #Ordena los elementos de my_NumList de mayor a menor utilizando reverse=True
print("De menor a mayor: ", my_NumList)  #Imprime la lista ordenada de mayor a menor


#################TUPLAS####################
###########################################
# Corresponde a una estructura similar a las listas, la diferencia está
# en que no se pueden modificar una vez creadas, es decir que son inmutables:

#Convertir una lista a tupla:prin
print("###########################")  #Imprime una línea de separación
print("###########################")  #Imprime otra línea de separación
print("###########################")  #Imprime otra línea de separación
print("############TUPLAS#########")  #Imprime el título de la sección de tuplas
my_tupla = tuple(my_lista)  #Convierte la lista my_lista en una tupla y guarda el resultado en my_tupla
print()  #Imprime una línea vacía
print()  #Imprime otra línea vacía
print("my_tuple: ", my_tupla)  #Muestra en pantalla el contenido de la tupla

print(my_tupla[0])  #Imprime el primer elemento de la tupla, ubicado en el índice 0
print(my_tupla[2])  #Imprime el tercer elemento de la tupla, ubicado en el índice 2


#Evaluar si un elemento está contenido en la tupla (Devuelve un valor booleano)
print('Rojo' in my_tupla)  #Comprueba si el elemento 'Rojo' se encuentra dentro de la tupla y devuelve True o False
print(my_tupla.count('Rojo'))  #Cuenta cuántas veces aparece el elemento 'Rojo' dentro de la tupla y muestra la cantidad

#Tupla con un solo elemento
my_tupla_unitaria = ('Blanco')  #Crea una variable con el valor 'Blanco', aunque al no tener coma no es realmente una tupla
print(my_tupla_unitaria)  #Muestra en pantalla el contenido de my_tupla_unitaria

#Empaquetado de tupla, tupla sin paréntesis
my_tupla = 'Gaspar', 5, 8, 1999  #Crea una tupla sin utilizar paréntesis, separando los elementos mediante comas
print(my_tupla)  #Muestra en pantalla todos los elementos de la tupla

#Desempaquetado de tupla, se guardan los valores en orden de las variables
nombre, dia, mes, año = my_tupla  #Desempaqueta los elementos de la tupla y los asigna a las variables en el mismo orden
print(nombre)  #Muestra en pantalla el valor almacenado en la variable nombre
print(dia)  #Muestra en pantalla el valor almacenado en la variable dia
print(mes)  #Muestra en pantalla el valor almacenado en la variable mes
print(año)  #Muestra en pantalla el valor almacenado en la variable año

print("Nombre: ", nombre, " - Dia:", dia, " - Mes: ", mes, "- Año: ", año)  #Muestra todos los datos desempaquetados en una sola línea

#Convertir una tupla en una lista
my_lista2=list(my_tupla)  #Convierte la tupla my_tupla en una lista y guarda el resultado en my_lista2
print(my_lista2)  #Muestra en pantalla la lista resultante de convertir la tupla