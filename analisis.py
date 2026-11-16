#Elaborado por: Fabiana Quesada y Juan Arias
#Fecha de creación: 16/11/2026
#Ultima modificacion:
#Version:3.14.7

#Importaciones
from jugadores import *
import tkinter
#Funciones
def generarAnalisis():
    """
    Funcionalidad:
    Genera un archivo CSV para analizar los
    datos de los jugadores del casino.
    Entrada:
    - Ninguna.
    Salida:
    - Ninguna.
    """
    jugadores=cargarJugadores()
    archivo=open("analisis.csv","w", encoding="utf-8")
    archivo.write("Nombre;Apellido;Username;Puntaje;Liquidez total\n")
    #Agrega los datos de cada jugador
    for jugador in jugadores:
        nombre=jugador[0][1]
        apellido=jugador[0][2]
        username=jugador[0][0]
        puntaje=jugador[2]
        liquidez=(jugador[1][0]+jugador[1][1]*10+jugador[1][2]*50+jugador[1][3]*20+jugador[1][4]*5)
        # Escribir una fila en el CSV
        archivo.write(f"{nombre};{apellido};{username};{puntaje};{liquidez}\n")
    archivo.close()
def ventanaAnalisis(ventanaAnterior):
    """
    Funcionalidad:
    Muestra una ventana para confirmar la
    generación del análisis de jugadores.
    Entrada:
    - ventanaAnterior: Ventana principal del casino.
    Salida:
    - Ninguna.
    """
    ventana=tkinter.Toplevel(ventanaAnterior)
    ventana.title("Generar Análisis")
    ventana.geometry("350x200")
    texto=tkinter.Label(ventana,text="¿Desea generar el análisis de jugadores?")
    texto.pack(pady=20)
    def confirmar():
        """
        Funcionalidad:
        Genera el archivo CSV y muestra
        un mensaje de confirmación.
        Entrada:
        - Ninguna.
        Salida:
        - Ninguna.
        """
        generarAnalisis()
        texto.config(text="Análisis generado correctamente")
        botonConfirmar.config(state="disabled")
    botonConfirmar=tkinter.Button(ventana,text="Confirmar",command=confirmar)
    botonConfirmar.pack(pady=5)
    botonCerrar=tkinter.Button(ventana,text="Cerrar",command=ventana.destroy)
    botonCerrar.pack(pady=5)    
