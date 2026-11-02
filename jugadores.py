#Elaborado por: Fabiana Quesada y Juan Arias
#Fecha de creación: 30/10/2026
#Ultima modificacion:
#Version:3.14.7

# Importaciones
import pickle
# Funciones
def cargarJugadores():
    """
    Funcionalidad:
    Carga la lista de jugadores almacenados en el archivo.
    Entrada:
    -Ninguna.
    Salida:
    -jugadores(list): Lista de jugadores registrados.
    """
    try:
        archivo = open("jugadores", "rb")
        jugadores = pickle.load(archivo)
        archivo.close() 
        return jugadores            
    except FileNotFoundError:
        return []# Retorna lista vacía
def guardarJugadores(jugadores):
    """
    Funcionalidad:
    Guarda la lista de jugadores en un archivo binario.
    Entrada:
    -jugadores(list): Lista de jugadores registrados.
    Salida:
    - Ninguna: No retorna ningún valor.
    """
    archivo = open("jugadores", "wb")
    pickle.dump(jugadores, archivo)# Guarda los datos
    archivo.close()
