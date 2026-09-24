# sensors =  {"living room": 21, "kitchen": 23, "bedroom": 20, "pantry": 22}  # Crea un diccionario llamado sensors con diferentes habitaciones como claves y sus temperaturas como valores
# num_cameras = {"backyard": 6,  "garage": 2, "driveway": 1}  # Crea un diccionario con diferentes ubicaciones y la cantidad de cámaras que hay en cada una
 
# print(sensors)  # Imprime en pantalla el contenido completo del diccionario sensors
# print(num_cameras)  # Imprime en pantalla el contenido completo del diccionario num_cameras
# translations = {"mountain": "orod", "bread": "bass", "friend": "mellon", "horse": "roch" }  # Crea un diccionario que relaciona palabras en inglés con sus respectivas traducciones
# print(translations)  # Imprime en pantalla el diccionario translations
 
##Verifiying an error:  # Indica que se va a comprobar un posible error al utilizar listas como claves de un diccionario
# powers = {[1, 2, 4, 8, 16]: 2, [1, 3, 9, 27, 81]: 3}  # Intenta crear un diccionario utilizando listas como claves, lo cual genera un error porque las listas no pueden ser claves de diccionarios
# # print(powers)  # Esta línea está comentada para evitar intentar imprimir el diccionario que contiene el error
 
# children = {"von Trapp": ["Johannes", "Rosmarie", "Eleonore"] , "Corleone": ["Sonny", "Fredo", "Michael"]}  # Crea un diccionario donde cada familia es una clave y su valor es una lista con los nombres de sus integrantes
# print(children)  # Imprime en pantalla el contenido del diccionario children
 
# my_empty_dictionary = {}  # Crea un diccionario vacío utilizando llaves sin ningún elemento
# print(my_empty_dictionary)  # Imprime en pantalla el diccionario vacío
 
# menu = {"oatmeal": 3, "avocado toast": 6, "carrot juice": 5, "blueberry muffin": 2}  # Crea un diccionario con diferentes alimentos como claves y sus precios como valores
# print("Before: ", menu)  # Imprime el diccionario antes de agregar un nuevo elemento
# menu["cheesecake"] = 8  # Agrega la clave cheesecake al diccionario y le asigna el valor 8
# print("After", menu)  # Imprime el diccionario después de agregar cheesecake
# animals_in_zoo = {"dinosaurs": 0}  # Crea un diccionario que indica que hay 0 dinosaurios en el zoológico
# animals_in_zoo = {"dinosaurs": 0}  # Vuelve a crear el diccionario indicando nuevamente que hay 0 dinosaurios
# animals_in_zoo = {"horses": 2}  # Sobrescribe completamente el diccionario anterior y ahora indica que hay 2 caballos
# print(animals_in_zoo)  # Imprime en pantalla el diccionario con los animales del zoológico
 
 
##Add multiple keys  # Indica que se va a mostrar cómo agregar varias claves al mismo tiempo
# sensors = {"living room": 21, "kitchen": 23, "bedroom": 20}  # Crea un diccionario con tres habitaciones y sus respectivas temperaturas
# print("Before", sensors)  # Imprime el diccionario antes de agregar las nuevas habitaciones
 
# #If we wanted to add 3 new rooms, we could use:  # Explica que se pueden agregar tres nuevas habitaciones utilizando update()
# sensors.update({"pantry": 22, "guest room": 25, "patio": 34})  # Agrega tres nuevas claves con sus respectivos valores al diccionario sensors
# print("After", sensors)  # Imprime el diccionario después de agregar las tres nuevas habitaciones
 
###  # Línea utilizada como separador visual
# user_ids = {"teraCoder": 9018293, "proProgrammer": 119238}  # Crea un diccionario que relaciona nombres de usuario con sus respectivos identificadores
# print(user_ids)  # Imprime en pantalla el diccionario user_ids
# user_ids.update({"theLooper": 138475, "stringQueen": 85739})  # Agrega dos nuevos usuarios y sus identificadores al diccionario
# print(user_ids)  # Imprime el diccionario después de agregar los nuevos usuarios
 
## Overwrite Values ##  # Indica que se va a explicar cómo sobrescribir valores de un diccionario
#We know that we can add a key by using the following syntax:  # Explica que se puede agregar una nueva clave utilizando la sintaxis indicada
#menu["banana"] = 3  # Agregaría una nueva clave llamada banana con el valor 3 al diccionario menu
# menu = {"oatmeal": 3, "avocado toast": 6, "carrot juice": 5, "blueberry muffin": 2}  # Crea un diccionario con alimentos y sus respectivos precios
# print("Before: ", menu)  # Imprime el diccionario antes de modificar alguno de sus valores
# menu["oatmeal"] = 5  # Modifica el valor asociado a la clave oatmeal y lo cambia de 3 a 5
# print("After", menu)  # Imprime el diccionario después de modificar el precio de oatmeal
 
## Notice the value of "oatmeal" has now changed to 5.  # Indica que el valor asociado a oatmeal ahora es 5
# oscar_winners = {"Best Picture": "La La Land", "Best Actor": "Casey Affleck", "Best Actress": "Emma Stone", "Animated Feature": "Zootopia"}  # Crea un diccionario con diferentes categorías de los premios Oscar y sus ganadores
# print("Before", oscar_winners)  # Imprime el diccionario de ganadores antes de realizar modificaciones
# print()  # Imprime una línea vacía para mejorar la presentación
# oscar_winners.update({"Supporting Actress": "Viola Davis"})  # Agrega al diccionario la categoría Supporting Actress con Viola Davis como ganadora
# print("After1", oscar_winners)  # Imprime el diccionario después de agregar la nueva categoría
# print()  # Imprime una línea vacía para mejorar la presentación
# oscar_winners["Best Picture"] = "Moonlight"  # Cambia el ganador de Best Picture de La La Land a Moonlight
# print("After2", oscar_winners)  # Imprime el diccionario después de modificar el ganador de Best Picture
 
 
###Dict Comprehensions  # Indica que se va a trabajar con comprensiones de diccionarios
#Let’s say we have two lists that we want to combine into a  # Explica que se tienen dos listas que se quieren combinar
#dictionary, like a list of students and a list of their heights,  # Indica que las listas contienen estudiantes y sus alturas
#in inches:  # Especifica que las alturas están expresadas en pulgadas
 
names = ['Jenny', 'Alexus', 'Sam', 'Grace']  # Crea una lista llamada names que contiene los nombres de cuatro estudiantes
heights = [61, 70, 67, 64]  # Crea una lista llamada heights que contiene las alturas de los estudiantes en pulgadas
 
#Python allows you to create a dictionary using  # Explica que Python permite crear un diccionario utilizando una comprensión de diccionario
# a dict comprehension, with this syntax:  # Indica que la sintaxis mostrada permite construir el diccionario
 
# zipStudents = zip(names, heights)  # Combina las listas names y heights en pares de elementos utilizando zip() y guarda el resultado en zipStudents
# print("zipStudents: ", zipStudents)  # Imprime el objeto zip creado a partir de las dos listas
 
# students = {key:value for key, value in zip(names, heights)}  # Crea un diccionario utilizando una comprensión de diccionario, relacionando cada nombre con su respectiva altura
# #students is now {'Jenny': 61, 'Alexus': 70, 'Sam': 67, 'Grace': 64}  # Muestra cómo queda el diccionario después de relacionar los nombres con las alturas
# print(students)  # Imprime en pantalla el diccionario students
 
# #zip() combines two lists into an iterator of tuples with the list elements paired together. This dict comprehension:  # Explica que zip() combina dos listas creando pares de elementos dentro de un iterador
 
# drinks = ["espresso", "chai", "decaf", "drip"]  # Crea una lista con diferentes tipos de bebidas
# caffeine = [64, 40, 0, 120]  # Crea una lista con la cantidad de cafeína correspondiente a cada bebida
 
# zipped_drinks = zip(drinks, caffeine)  # Combina cada bebida con su respectiva cantidad de cafeína utilizando zip()
# print(zipped_drinks)  # Imprime en pantalla el objeto zip que contiene los pares de bebidas y cafeína
 
# drinks_to_caffeine = {key:value for key, value in zipped_drinks}  # Crea un diccionario relacionando cada bebida con su cantidad de cafeína mediante una comprensión de diccionario
# print(drinks_to_caffeine)  # Imprime en pantalla el diccionario que relaciona las bebidas con la cafeína
 
songs = ["Like a Rolling Stone", "Satisfaction", "Imagine", "What's Going On", "Respect", "Good Vibrations"]  # Crea una lista con los nombres de seis canciones
playcounts = [78, 29, 44, 21, 89, 5]  # Crea una lista con la cantidad de reproducciones correspondiente a cada canción
plays = {key:value for key, value in zip(songs, playcounts)}  # Crea un diccionario relacionando cada canción con su cantidad de reproducciones utilizando zip() y una comprensión de diccionario
print(plays)  # Imprime en pantalla el diccionario con las canciones y sus cantidades de reproducciones
plays.update({"Purple Haze": 1})  # Agrega la canción Purple Haze al diccionario con una reproducción
plays.update({"Respect": 94})  # Modifica el valor de Respect y establece su cantidad de reproducciones en 94
print("After: ", plays)  # Imprime el diccionario actualizado después de agregar Purple Haze y modificar Respect
library = {"The Best Songs": plays, "Sunday Feelings": {}}  # Crea un diccionario llamado library que contiene el diccionario plays y otro diccionario vacío
print(library)  # Imprime en pantalla todo el contenido del diccionario library