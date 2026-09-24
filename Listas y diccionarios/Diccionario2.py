# #### Get A Key  # Indica que se va a explicar cómo obtener un valor utilizando una clave
# #you can access the values in it by providing the key:  # Explica que se puede acceder a los valores de un diccionario proporcionando su clave
 
# building_heights = {"Burj Khalifa": 828, "Shanghai Tower": 632, "Abraj Al Bait": 601, "Ping An": 599, "Lotte World Tower": 554.5, "One World Trade": 541.3}  # Crea un diccionario con los nombres de edificios como claves y sus alturas como valores
# print(building_heights["Burj Khalifa"]) # Imprime la altura asociada a la clave "Burj Khalifa", que es 828
# print(building_heights["Ping An"]) # Imprime la altura asociada a la clave "Ping An", que es 599
 
# zodiac_elements = {"water": ["Cancer", "Scorpio", "Pisces"], "fire": ["Aries", "Leo", "Sagittarius"], "earth": ["Taurus", "Virgo", "Capricorn"], "air":["Gemini", "Libra", "Aquarius"]}  # Crea un diccionario que relaciona cada elemento zodiacal con una lista de signos
# print(zodiac_elements["earth"])  # Accede a la clave "earth" e imprime la lista de signos asociada a ella
# print(zodiac_elements["fire"])  # Accede a la clave "fire" e imprime la lista de signos asociada a ella
 
# ## Get an Invalid Key  # Indica que se va a mostrar qué ocurre al intentar acceder a una clave que no existe
 
# building_heights = {"Burj Khalifa": 828, "Shanghai Tower": 632, "Abraj Al Bait": 601, "Ping An": 599, "Lotte World Tower": 554.5, "One World Trade": 541.3}  # Crea nuevamente el diccionario con las alturas de los edificios
# print(building_heights["Landmark 81"])  # Intenta acceder a una clave que no existe y genera un error KeyError
 
# ##One way to avoid this error is to first check if the key exists in the dictionary:  # Explica que una forma de evitar el error es comprobar primero si la clave existe
# key_to_check = "Landmark 81"  # Guarda en una variable el nombre de la clave que se quiere comprobar
 
# if key_to_check in building_heights:  # Comprueba si la clave almacenada en key_to_check existe dentro del diccionario
#   print(building_heights["Landmark 81"])  # Imprime el valor de Landmark 81 solamente si la clave existe
 
# zodiac_elements = {"water": ["Cancer", "Scorpio", "Pisces"], "fire": ["Aries", "Leo", "Sagittarius"], "earth": ["Taurus", "Virgo", "Capricorn"], "air":["Gemini", "Libra", "Aquarius"]}  # Crea nuevamente el diccionario con los elementos y signos zodiacales
 
# zodiac_elements["energy"] = "Not a Zodiac element"  # Agrega una nueva clave llamada energy con el valor indicado
 
# if "energy" in zodiac_elements:  # Comprueba si la clave energy existe dentro del diccionario
#   print(zodiac_elements["energy"])  # Imprime el valor asociado a la clave energy si esta existe
 
# ##Safely Get a Key  # Indica que se va a mostrar cómo obtener una clave de forma segura
# building_heights = {"Burj Khalifa": 828, "Shanghai Tower": 632, "Abraj Al Bait": 601, "Ping An": 599, "Lotte World Tower": 554.5, "One World Trade": 541.3}  # Crea un diccionario con los nombres de edificios y sus alturas
 
# #this line will return 632:  # Indica que la siguiente línea devolverá el valor 632
# building_heights.get("Shanghai Tower")  # Busca la clave Shanghai Tower y devuelve su valor, que es 632
 
# #this line will return None:  # Indica que la siguiente línea devolverá None porque la clave no existe
# building_heights.get("My House")  # Busca la clave My House y devuelve None porque no existe en el diccionario
 
# ###  # Línea utilizada como separador
# user_ids = {"teraCoder": 100019, "pythonGuy": 182921, "samTheJavaMaam": 123112, "lyleLoop": 102931, "keysmithKeith": 129384}  # Crea un diccionario que relaciona nombres de usuario con sus respectivos identificadores
# user_ids.get("teraCoder")  # Busca el identificador asociado al usuario teraCoder
 
# if user_ids.get("teraCoder") == None:  # Comprueba si el usuario teraCoder no tiene un identificador en el diccionario
#    tc_id = 1000  # Asigna 1000 a tc_id si teraCoder no tiene un identificador
# else:  # Se ejecuta cuando teraCoder sí tiene un identificador
#    tc_id = user_ids.get("teraCoder")  # Obtiene el identificador de teraCoder y lo guarda en tc_id
 
# print(tc_id)  # Imprime en pantalla el identificador almacenado en tc_id
 
# if user_ids.get("superStackSmash") == None:  # Comprueba si el usuario superStackSmash no existe en el diccionario
#      stack_id = 100000  # Asigna 100000 a stack_id si el usuario no existe
 
# print(stack_id)  # Imprime en pantalla el valor almacenado en stack_id
 
# ###Delete a Key  # Indica que se va a explicar cómo eliminar una clave de un diccionario
#.pop() works to delete items from a dictionary, when you know the key value.  # Explica que pop() permite eliminar elementos de un diccionario cuando conocemos su clave
#raffle = {223842: "Teddy Bear", 872921: "Concert Tickets", 320291: "Gift Basket", 412123: "Necklace", 298787: "Pasta Maker"}  # Crea un diccionario donde los números son claves y los premios son sus valores
#print(raffle.pop(320291, "No Prize"))  # Elimina la clave 320291 y devuelve su valor, que es Gift Basket
## Prints "Gift Basket"  # Indica que la línea anterior imprime Gift Basket
#print(raffle)  # Imprime el diccionario después de eliminar la clave 320291
# # Prints {223842: "Teddy Bear", 872921: "Concert Tickets", 412123: "Necklace", 298787: "Pasta Maker"}  # Muestra cómo queda el diccionario después de eliminar el elemento
# print(raffle.pop(100000, "No Prize"))  # Intenta eliminar la clave 100000 y devuelve No Prize porque la clave no existe
# # Prints "No Prize"  # Indica que la línea anterior imprime No Prize
# print(raffle)  # Imprime el diccionario y muestra que no cambió porque la clave 100000 no existía
# # Prints {223842: "Teddy Bear", 872921: "Concert Tickets", 412123: "Necklace", 298787: "Pasta Maker"}  # Muestra el contenido del diccionario después del intento de eliminación
# print(raffle.pop(872921, "No Prize"))  # Elimina la clave 872921 y devuelve su valor, Concert Tickets
# # Prints "Concert Tickets"  # Indica que la línea anterior imprime Concert Tickets
# print(raffle)  # Imprime el diccionario después de eliminar la clave 872921
# # Prints {223842: "Teddy Bear", 412123: "Necklace", 298787: "Pasta Maker"}  # Muestra el contenido final del diccionario
 
# available_items = {"health potion": 10, "cake of the cure": 5, "green elixir": 20, "strength sandwich": 25, "stamina grains": 15, "power stew": 30}  # Crea un diccionario con diferentes objetos y la cantidad disponible de cada uno
# health_points = 20  # Crea una variable que representa los puntos de salud y comienza con 20
 
# health_points += available_items.pop("stamina grains", 0)  # Elimina stamina grains del diccionario y suma su valor a health_points
# health_points += available_items.pop("power stew", 0)  # Elimina power stew del diccionario y suma su valor a health_points
# health_points += available_items.pop("mystic bread", 0)  # Busca y elimina mystic bread, y suma 0 si no existe
 
# print(available_items)  # Imprime los objetos que todavía quedan disponibles
# print(health_points)  # Imprime el total actualizado de puntos de salud
 
# ##Get All Keys  # Indica que se va a explicar cómo obtener todas las claves de un diccionario
# test_scores = {"Grace":[80, 72, 90], "Jeffrey":[88, 68, 81], "Sylvia":[80, 82, 84], "Pedro":[98, 96, 95], "Martin":[78, 80, 78], "Dina":[64, 60, 75]}  # Crea un diccionario con estudiantes como claves y listas de calificaciones como valores
# print(list(test_scores))  # Convierte las claves del diccionario en una lista y la imprime
# # Prints ["Grace", "Jeffrey", "Sylvia", "Pedro", "Martin", "Dina"]  # Muestra el resultado esperado con todas las claves
 
# for student in test_scores.keys():  # Recorre todas las claves del diccionario utilizando el método keys()
#  print(student)  # Imprime el nombre del estudiante en cada repetición
 
# user_ids = {"teraCoder": 100019, "pythonGuy": 182921, "samTheJavaMaam": 123112, "lyleLoop": 102931, "keysmithKeith": 129384}  # Crea un diccionario con usuarios y sus identificadores
# num_exercises = {"functions": 10, "syntax": 13, "control flow": 15, "loops": 22, "lists": 19, "classes": 18, "dictionaries": 18}  # Crea un diccionario con temas de programación y cantidad de ejercicios
 
# users = user_ids.keys()  # Obtiene todas las claves del diccionario user_ids y las guarda en users
# lessons = num_exercises.keys()  # Obtiene todas las claves del diccionario num_exercises y las guarda en lessons
 
# print(users)  # Imprime el objeto que contiene las claves de user_ids
# print(lessons)  # Imprime el objeto que contiene las claves de num_exercises
 
##Get All Values  # Indica que se va a explicar cómo obtener todos los valores de un diccionario
# test_scores = {"Grace":[80, 72, 90], "Jeffrey":[88, 68, 81], "Sylvia":[80, 82, 84], "Pedro":[98, 96, 95], "Martin":[78, 80, 78], "Dina":[64, 60, 75]}  # Crea un diccionario con estudiantes como claves y listas de calificaciones como valores
 
# for score_list in test_scores.values():  # Recorre todos los valores del diccionario utilizando values()
#  print(score_list)  # Imprime la lista de calificaciones de cada estudiante
 
# num_exercises = {"functions": 10, "syntax": 13, "control flow": 15, "loops": 22, "lists": 19, "classes": 18, "dictionaries": 18}  # Crea un diccionario con temas de programación y cantidad de ejercicios
 
# total_exercises = 0  # Crea una variable para almacenar el total de ejercicios y comienza en cero
 
# for exercises in num_exercises.values():  # Recorre todos los valores del diccionario num_exercises
#   total_exercises += exercises  # Suma la cantidad de ejercicios actual al total acumulado
# print(total_exercises)  # Imprime la cantidad total de ejercicios
 
##Get All Items  # Indica que se va a explicar cómo obtener todas las claves y valores de un diccionario
# biggest_brands = {"Apple": 184, "Google": 141.7, "Microsoft": 80, "Coca-Cola": 69.7, "Amazon": 64.8}  # Crea un diccionario con marcas y sus valores en miles de millones de dólares
 
# for company, value in biggest_brands.items():  # Recorre cada par de clave y valor del diccionario y los guarda en company y value
#  print(company + " has a value of " + str(value) + " billion dollars. ")  # Une el nombre de la empresa con su valor convertido a texto y muestra el resultado
 
# pct_women_in_occupation = {"CEO": 28, "Engineering Manager": 9, "Pharmacist": 58, "Physician": 40, "Lawyer": 37, "Aerospace Engineer": 9}  # Crea un diccionario con diferentes profesiones y el porcentaje de mujeres en cada una
 
# for occupation, percentage in pct_women_in_occupation.items():  # Recorre cada profesión y su porcentaje correspondiente utilizando items()
#   print("Women make up " + str(percentage) + " percent of " + occupation + "s.")  # Convierte el porcentaje a texto y construye una frase indicando el porcentaje de mujeres en cada profesión