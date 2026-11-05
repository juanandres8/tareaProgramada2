#Fecha de creación: 3/11/2026
#Ultima modificacion:
#Version:3.14.7

#Importaciones
import tkinter
from jugadores import *

#Definicion de funciones
def ventanaJugar(ventanaAnterior, username):
    '''
    Funcionalidad:
    Crear y mostrar la ventana de juegos del casino.
    Presenta los botones correspondientes a los juegos disponibles
    y permite regresar al menú principal.
    Entradas:
    ventanaAnterior: Ventana principal desde la cual se abre la ventana de juegos.
    username (str): Nombre del jugador que inició sesión.
    Salidas:
    No retorna ningún valor.
    Muestra una ventana gráfica con las opciones de juegos disponibles.
    '''
    #titulo
    ventanaJugar = tkinter.Toplevel(ventanaAnterior)
    ventanaJugar.configure(bg="lightblue")
    ventanaJugar.title("Menú Juegos")# Título de la ventana
    titulo = tkinter.Label(ventanaJugar,text="Juegos disponibles",font=("Georgia", 28),bg="lightblue")
    titulo.pack(pady=20)
    ventanaJugar.geometry("800x500")# Tamaño de la ventana
    #Botones
    #Ruleta
    botonRuleta = tkinter.Button(ventanaJugar,text="Ruleta",font=("Times New Roman", 16))
    botonRuleta.pack(pady=5)
    #Tragamonedas
    botonTragamonedas = tkinter.Button(ventanaJugar,text="Tragamonedas",font=("Times New Roman", 16))
    botonTragamonedas.pack(pady=5)
    #Blackjack
    botonBlackjack = tkinter.Button(ventanaJugar,text="Blackjack",font=("Times New Roman", 16))
    botonBlackjack.pack(pady=5)
    #Dados
    botonDados = tkinter.Button(ventanaJugar,text="Dados",font=("Times New Roman", 16))
    botonDados.pack(pady=5)
    #Volver a menú principal
    botonVolver = tkinter.Button(ventanaJugar,text="Volver",font=("Times New Roman", 16), command=lambda: [ventanaJugar.destroy(), ventanaAnterior.deiconify()])
    botonVolver.pack(pady=5)
    #mantener abierta la ventana
    ventanaPrincipal.mainloop()
    
