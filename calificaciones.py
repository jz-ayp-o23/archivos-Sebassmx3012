"""
José Sebastián González Ortega
9/11/2023
Lee el archivo calificaciones.txt el cual contiene nombre y calificaciones, 
por lo que los lee de allí y crea un archivo con 'w' llamado "promedios.txt" 
en donde tiene el formato {APELLIDO, Nombre: promedio} 
"""
def calcular_promedio(calificaciones):
    "Calcula el promedio de las calificaciones"
    return sum(calificaciones) / len(calificaciones)
def main():
    "Abre el archivo calificaciones.txt para lectura y escritura de promedios.txt"
    with open('data/calificaciones.txt', 'r') as entrada:
        # Abre el archivo "promedios.txt" para escritura
        with open('data/promedios.txt', 'w') as salida:
            # Lee cada línea del archivo de entrada
            for linea in entrada:
                # Divide la línea en palabras
                palabras = linea.split()
                # Extrae el nombre y las calificaciones
                nombre = palabras[0] + ' ' + palabras[1]
                calificaciones = list(map(int, palabras[2:]))
                # Calcula el promedio de las calificaciones
                promedio = calcular_promedio(calificaciones)
                # Escribe en el archivo de salida en el formato deseado
                salida.write(f"{palabras[1]}, {palabras[0]}: {promedio:.2f}\n")

if __name__ == "__main__":
    main()
