#Elaborado por: Fabiana Quesada y Juan Arias
#Fecha de creación: 3/11/2026
#Ultima modificacion:
#Version:3.14.7

#Importaciones
import tkinter
from jugadores import *
from ventanaJugar import *
from fichas import ventanaFichas
#Definicion de funciones
def ventanaPrincipal(username):
    '''  
    Funcionalidad:Crear y mostrar la interfaz ventana principal del casino.
    Entradas: username (str): Nombre de usuario del jugador que inició sesión.
    Salidas:No retorna ningún valor.
    Muestra una ventana gráfica con el menú principal del casino.
    '''
    #Titulo
    ventanaPrincipal = tkinter.Tk()
    ventanaPrincipal.configure(bg="lightblue")
    ventanaPrincipal.title("Menú principal")# Título de la ventana
    titulo = tkinter.Label(ventanaPrincipal,text="Bienvenido al Casino",font=("Georgia", 28),bg="lightblue")
    titulo.pack(pady=20)
    ventanaPrincipal.geometry("800x500")# Tamaño de la ventana
    # Username del jugador
    etiquetaUsername = tkinter.Label(ventanaPrincipal,text="Jugador: " + username,font=("Arial", 12),bg="lightblue")
    etiquetaUsername.pack(pady=10)
    #Botones
    #Jugar
    botonJugar = tkinter.Button(ventanaPrincipal,text="Jugar",font=("Times New Roman", 16),command=lambda: [ventanaPrincipal.withdraw(), ventanaJugar(ventanaPrincipal, username)])
    botonJugar.pack(pady=5)
    #Fichas
    botonFichas = tkinter.Button(
    ventanaPrincipal,
    text="Fichas",
    font=("Times New Roman", 16),command=lambda: [ventanaPrincipal.withdraw(),ventanaFichas(ventanaPrincipal, username)])
    botonFichas.pack(pady=5)
    #Ranking
    botonRanking = tkinter.Button(ventanaPrincipal,text="Ranking",font=("Times New Roman", 16))
    botonRanking.pack(pady=5)
    #Analisis
    botonAnalisis = tkinter.Button(ventanaPrincipal,text="Analisis",font=("Times New Roman", 16))
    botonAnalisis.pack(pady=5)
    #Cerrar sesión
    botonCerrar = tkinter.Button(ventanaPrincipal,text="Cerrar sesión",font=("Times New Roman", 16))
    botonCerrar.pack(pady=5)
    #mantener abierta la ventana
    ventanaPrincipal.mainloop()
    
