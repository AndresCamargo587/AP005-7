import pandas as pd

# CARGAR EL ARCHIVO

df = pd.read_csv("Fruits.csv")

# LISTA

opciones = [
    "Información general",
    "Buscar una fruta",
    "Buscar por color",
    "Filtrar por precio",
    "Precio mayor y menor",
    "Estadísticas",
    "Mostrar frutas y colores",
    "Ordenar por precio",
    "Salir"
]

# TUPLA

columnas = ("type", "color", "price usd")

# DICCIONARIO

categorias = {
    "Bajo": "Hasta 1.50 USD",
    "Medio": "Más de 1.50 y hasta 2.50 USD",
    "Alto": "Más de 2.50 USD"
}

# NUEVA COLUMNA

def clasificar_precio(precio):

    if precio <= 1.50:
        return "Bajo"

    elif precio <= 2.50:
        return "Medio"

    else:
        return "Alto"


df["categoria"] = df["price usd"].apply(clasificar_precio)

# MENÚ PRINCIPAL

while True:

    print("\n======================================")
    print(" ANÁLISIS DE FRUTAS ")
    print("======================================")

    for i in range(len(opciones)):
        print(i + 1, ".", opciones[i])

    opcion = input("\nSeleccione una opción: ")

    # 1. INFORMACIÓN GENERAL

    if opcion == "1":

        print("\n--- INFORMACIÓN GENERAL ---")

        print("Cantidad de registros:", len(df))
        print("Cantidad de columnas:", len(df.columns))

        print("\nColumnas:")
        print(df.columns.tolist())

        print("\nPrimeros registros:")
        print(df.head())

    # 2. BUSCAR UNA FRUTA

    elif opcion == "2":

        fruta = input("\nIngrese el nombre de la fruta: ")

        resultado = df[
            df["type"].str.lower() == fruta.lower()
        ]

        if resultado.empty:
            print("\nNo se encontró esa fruta.")

        else:
            print("\nRegistros encontrados:")
            print(resultado)

    # 3. BUSCAR POR COLOR

    elif opcion == "3":

        color = input("\nIngrese el color: ")

        resultado = df[
            df["color"].str.lower() == color.lower()
        ]

        if resultado.empty:
            print("\nNo se encontró ese color.")

        else:
            print("\nRegistros encontrados:")
            print(resultado)

    # 4. FILTRAR POR PRECIO

    elif opcion == "4":

        minimo = float(input("\nIngrese el precio mínimo: "))
        maximo = float(input("Ingrese el precio máximo: "))

        resultado = df[
            (df["price usd"] >= minimo) &
            (df["price usd"] <= maximo)
        ]

        if resultado.empty:
            print("\nNo hay frutas en ese rango.")

        else:
            print("\nFrutas encontradas:")
            print(resultado)

    # 5. PRECIO MAYOR Y MENOR

    elif opcion == "5":

        mayor = df["price usd"].max()
        menor = df["price usd"].min()

        print("\nPrecio mayor:", mayor)
        print("Precio menor:", menor)


        print("\nFruta con mayor precio:")

        fruta_mayor = df[
            df["price usd"] == mayor
        ]

        print(fruta_mayor)


        print("\nFruta con menor precio:")

        fruta_menor = df[
            df["price usd"] == menor
        ]

        print(fruta_menor)

    # 6. ESTADÍSTICAS

    elif opcion == "6":

        print("\n--- ESTADÍSTICAS GENERALES ---")

        print("Promedio:",
              df["price usd"].mean())

        print("Mediana:",
              df["price usd"].median())

        print("Desviación estándar:",
              df["price usd"].std())

        print("Precio mínimo:",
              df["price usd"].min())

        print("Precio máximo:",
              df["price usd"].max())


        print("\n--- ESTADÍSTICAS DE UNA FRUTA ---")

        fruta = input("Ingrese una fruta: ")

        datos = df[
            df["type"].str.lower() == fruta.lower()
        ]

        if datos.empty:
            print("No se encontró esa fruta.")

        else:
            print("Cantidad:",
                  len(datos))

            print("Promedio:",
                  datos["price usd"].mean())

            print("Precio mínimo:",
                  datos["price usd"].min())

            print("Precio máximo:",
                  datos["price usd"].max())


        print("\n--- ESTADÍSTICAS DE UN COLOR ---")

        color = input("Ingrese un color: ")

        datos = df[
            df["color"].str.lower() == color.lower()
        ]

        if datos.empty:
            print("No se encontró ese color.")

        else:
            print("Cantidad:",
                  len(datos))

            print("Promedio:",
                  datos["price usd"].mean())

            print("Precio mínimo:",
                  datos["price usd"].min())

            print("Precio máximo:",
                  datos["price usd"].max())


    # 7. FRUTAS Y COLORES

    elif opcion == "7":

        print("\n--- FRUTAS DIFERENTES ---")

        frutas = df["type"].unique()

        for fruta in frutas:
            print(fruta)


        print("\n--- COLORES DIFERENTES ---")

        colores = df["color"].unique()

        for color in colores:
            print(color)


        print("\nCategorías de precio:")

        for clave in categorias:
            print(clave, ":", categorias[clave])

    # 8. ORDENAR

    elif opcion == "8":

        print("\n1. Menor a mayor")
        print("2. Mayor a menor")

        orden = input("Seleccione: ")

        if orden == "1":

            resultado = df.sort_values(
                "price usd"
            )

            print("\nDatos ordenados:")
            print(resultado)


        elif orden == "2":

            resultado = df.sort_values(
                "price usd",
                ascending=False
            )

            print("\nDatos ordenados:")
            print(resultado)


        else:
            print("Opción incorrecta.")

    # 9. SALIR

    elif opcion == "9":

        print("\nPrograma finalizado.")
        break


    else:

        print("\nOpción incorrecta.")