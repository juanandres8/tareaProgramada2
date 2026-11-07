#Elaborado por: Fabiana Quesada y Juan Arias
#Fecha de creación: 6/11/2026
#Ultima modificacion:
#Version:3.14.7

#Importaciones
import random
import re
from tkinter import Toplevel,Label,Entry,Button
from jugadores import cargarJugadores
#Funciones
def crearCasillas():
    """
    Funcionalidad:
    Crea las 37 casillas de la ruleta con su número y color.
    Entrada:
    - Ninguna.
    Salida:
    - casillas:Lista de tuplas con número y color.
    """
    casillas=[]
    for numero in range(37):#Recorre del 0 al 36
        if numero==0:
            color="verde"
        elif numero%2 ==0:
            color="negro"
        else:
            color="rojo"
        casillas.append((numero,color))#Agrega la tupla
    return casillas
def girarRuleta():
    """
    Funcionalidad:
    Selecciona aleatoriamente una casilla de la ruleta.
    Entrada:
    - Ninguna.
    Salida:
    - resultado:Casilla con número y color.
    """
    casillas=crearCasillas()
    numero=random.randint(0, 36)
    resultado=casillas[numero]# Obtiene la casilla
    return resultado# Retorna número y color
def comprobarApuesta(tipoApuesta, apuesta, resultado):
    """
    Funcionalidad:
    Comprueba si la apuesta coincide con el
    resultado obtenido en la ruleta.
    Entrada:
    - tipoApuesta: Tipo de apuesta realizada.
    - apuesta: Color o número seleccionado.
    - resultado: Número y color obtenidos.
    Salida:
    - ganador: Indica si la apuesta ganó.
    """

    if tipoApuesta=="color":
        return apuesta==resultado[1]#Compara colores
    elif tipoApuesta=="numero":
        return apuesta==resultado[0]#Compara números
    else:
        return False# Tipo de apuesta inválido
def calcularPuntos(tipoApuesta, apuesta, resultado):
    """
    Funcionalidad:
    Calcula los puntos ganados o perdidos en la ruleta.
    Entrada:
    - tipoApuesta: Tipo de apuesta realizada.
    - apuesta: Color o número seleccionado.
    - resultado: Número y color obtenidos.
    Salida:
    - puntos: Puntos ganados o perdidos.
    """
    if comprobarApuesta(tipoApuesta, apuesta, resultado):
        if tipoApuesta=="numero":
            return pagos["numero"]["puntos"]#Puntos por número
        else:
            return pagos[apuesta]["puntos"]#Puntos por color
    else:
        return -1#Pierde un punto
def ventanaRuleta(ventanaL,username):
    """
    Funcionalidad:
    Crea la ventana gráfica del juego de ruleta.
    Entrada:
    - ventanaL: Ventana desde la cual se abre la ruleta.
    - username: Nombre de usuario del jugador.
    Salida:
    - Ninguna.
    """
    ventana=Toplevel(ventanaL)
    ventana.title("Ruleta")
    ventana.geometry("800x500")
    titulo=Label(ventana,text="Juego de Ruleta",font=("Arial",16))
    titulo.pack(pady=20)
    # Cargar los jugadores
    jugadores=cargarJugadores()
    for jugador in jugadores:
        if jugador[0][0]==username:
            puntaje=jugador[2]
            textoPuntaje=Label(ventana,text=f"Jugador: {username} | Puntaje: {puntaje}")
            textoPuntaje.pack(pady=8)
            break
    #Solicita la apuesta
    textoApuesta=Label(ventana,text="Ingrese rojo, negro, verde o un número del 0 al 36 para apostar:")
    textoApuesta.pack(pady=18)
    entradaApuesta=Entry(ventana)
    entradaApuesta.pack(pady=18)
    mensaje=Label(ventana, text="")
    mensaje.pack(pady=18)
    def validarApuesta():
        """
        Funcionalidad:
        Valida que la apuesta sea un color permitido
        o un número entre 0 y 36.
        Entrada:
        - Ninguna.
        Salida:
        - Ninguna.
        """
        apuesta=entradaApuesta.get().strip().lower()
        if apuesta=="rojo" or apuesta=="negro" or apuesta=="verde":
            mensaje.config(text="Apuesta válida")
            return("color",apuesta)
        elif re.match(r"^[0-9]+$", apuesta):
            try:
                numero=int(apuesta)
                if 0<=numero<=36:
                    mensaje.config(text="Apuesta válida")
                    return("numero",numero)
                else:
                    mensaje.config(text="El número debe estar entre 0 y 36")
                    return None
            except ValueError:
                mensaje.config(text="Número inválido")
                return None
        else:
            mensaje.config(text="Ingrese una apuesta válida")
            return None
    botonValidar=Button(ventana, text="Validar apuesta",command=validarApuesta)
    botonValidar.pack(pady=10)
    def realizarGiro():
        """
        Funcionalidad:
        Gira la ruleta y muestra el resultado
        de la apuesta realizada.
        Entrada:
        - Ninguna.
        Salida:
        - Ninguna.
        """
        datos=validarApuesta()#Valida la apuesta
        if datos is not None:
            tipoApuesta=datos[0]
            apuesta=datos[1]
            resultado=girarRuleta()#Gira la ruleta
            puntos=calcularPuntos(tipoApuesta, apuesta, resultado)
            mensaje.config(text=f"Salió el {resultado[0]} ({resultado[1]})\n"f"Puntos de esta jugada: {puntos}")
    #Botón para girar la ruleta
    botonGirar=Button(ventana, text="Girar Ruleta",command=realizarGiro)
    botonGirar.pack(pady=10)
# Tabla de pagos de la ruleta
pagos = {
    "rojo": {
        "multiplicador": 2,
        "puntos": 1
    },
    "negro": {
        "multiplicador": 2,
        "puntos": 1
    },
    "verde": {
        "multiplicador": 3,
        "puntos": 2
    },
    "numero": {
        "puntos": 2
    }
}
