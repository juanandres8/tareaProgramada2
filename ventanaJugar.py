#Fecha de creación: 3/11/2026
#Ultima modificacion:
#Version:3.14.7

#Importaciones
import tkinter
from jugadores import *
from ruleta import ventanaRuleta
from tragamonedas import ventanaTragamonedas
from blackJack import ventanaBlackjack
from dados import ventanaDados
from tkinter import messagebox
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
    titulo=tkinter.Label(ventanaJugar,text="Juegos disponibles",font=("Georgia", 28),bg="lightblue")
    titulo.pack(pady=20)
    ventanaJugar.geometry("800x500")# Tamaño de la ventana
    #Mostrar fichas disponibles
    etiquetaFichas = tkinter.Label(ventanaJugar,text="",font=("Arial", 12),bg="lightblue")
    etiquetaFichas.pack(pady=10)
    #Actualizar informacion de las fichas
    def actualizarFichas(event=None):
        jugadores = cargarJugadores()
        jugadorActual = None
        for jugador in jugadores:
            if jugador[0][0] == username:
                jugadorActual = jugador
                break
        if jugadorActual is None:
            etiquetaFichas.config(text="No se encontro la informacion del jugador.")
            return
        etiquetaFichas.config( text=f"Fichas disponibles:\n"
                 f"Rojas: {jugadorActual[1][1]} | "
                 f"Azules: {jugadorActual[1][2]} | "
                 f"Verdes: {jugadorActual[1][3]} | "
                 f"Blancas: {jugadorActual[1][4]}")
    #Mostrar las fichas al abrir la ventana
    actualizarFichas()
    #Botones
    #Ruleta
    botonRuleta=tkinter.Button(ventanaJugar,text="Ruleta",font=("Times New Roman", 16),command=lambda: ventanaRuleta(ventanaJugar, username))
    botonRuleta.pack(pady=5)
    #Tragamonedas
    botonTragamonedas = tkinter.Button(ventanaJugar,text="Tragamonedas",font=("Times New Roman", 16),command=lambda: ventanaTragamonedas(ventanaJugar,username))
    botonTragamonedas.pack(pady=5)
    #Blackjack
    botonBlackjack=tkinter.Button(ventanaJugar,text="Blackjack",font=("Times New Roman", 16),command=lambda:ventanaBlackjack(ventanaJugar,username))
    botonBlackjack.pack(pady=5)
    #Dados
    botonDados = tkinter.Button(ventanaJugar,text="Dados",font=("Times New Roman", 16),command=lambda: ventanaDados(ventanaJugar, username))
    botonDados.pack(pady=5)
    #Volver a menú principal
    botonVolver = tkinter.Button(ventanaJugar,text="Volver",font=("Times New Roman", 16), command=lambda: [ventanaJugar.destroy(), ventanaAnterior.deiconify()])
    botonVolver.pack(pady=5)
    

