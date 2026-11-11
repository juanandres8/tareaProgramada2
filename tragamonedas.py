#Elaborado por: Fabiana Quesada y Juan Arias
#Fecha de creación: 30/10/2026
#Ultima modificacion:
#Version:3.14.7

#importaciones
import tkinter
import random
from tkinter import messagebox
from jugadores import cargarJugadores, guardarJugadores

#Matriz de los rodillos
rodillos = [ ["🍒", "🍋", "🍇", "⚡", "⭐"],
    ["🍒", "🍋", "🍇", "⚡", "⭐"],
    ["🍒", "🍋", "🍇", "⚡", "⭐"]]

#Diccionario de pagos
pagos = {"ganar": {"multiplicador": 2,"puntos": 2},"perder": {"multiplicador": 0,"puntos": -1}}

def girarRodillos():
    """
    Funcionalidad:
    Selecciona aleatoriamente un simbolo para cada rodillo.
    Entradas:
    - Ninguna.
    Salidas:
    - resultado: Tupla con los tres simbolos seleccionados.
    """
    resultado = []
    for posicion in range(3):
        simbolo = random.choice(rodillos[posicion])
        resultado.append(simbolo)
    return tuple(resultado)

def comprobarGanador(resultado):
    """
    Funcionalidad:
    Comprueba si los tres simbolos son iguales.
    Entradas:
    - resultado: Tupla con los simbolos obtenidos.
    Salidas:
    - True si gana.
    - False si pierde.
    """
    if resultado[0] == resultado[1] == resultado[2]:
        return True
    return False


def actualizarFichas(jugador, fichasApostadas, gano):
    """
    Funcionalidad:
    Descuenta las fichas apostadas y entrega el premio
    si el jugador gana.
    Entradas:
    - jugador: Datos del jugador.
    - fichasApostadas: Lista con las fichas apostadas.
    - gano: Indica si el jugador ganó.
    Salidas:
    - jugador: Datos actualizados.
    """
    for posicion in range(4):
        cantidad = fichasApostadas[posicion]
        #Descontar fichas apostadas
        jugador[1][posicion + 1] -= cantidad
        #Entregar premio si gana
        if gano:
            premio = cantidad * pagos["ganar"]["multiplicador"]
            jugador[1][posicion + 1] += premio
    return jugador


def actualizarPuntaje(jugador, gano):
    """
    Funcionalidad:
    Actualiza el puntaje del jugador.
    Entradas:
    - jugador: Datos del jugador.
    - gano: Indica si ganó o perdió.
    Salidas:
    - Puntaje actualizado.
    """
    if gano:
        jugador[2] += pagos["ganar"]["puntos"]
    else:
        jugador[2] += pagos["perder"]["puntos"]
    return jugador[2]


def ventanaTragamonedas(ventanaAnterior, username):
    """
    Funcionalidad:
    Crea la ventana gráfica del juego de tragamonedas.
    Entradas:
    - ventanaAnterior: Ventana desde donde se abre.
    - username: Nombre del jugador.
    Salidas:
    - Ninguna.
    """
    #Crear ventana
    ventana = tkinter.Toplevel(ventanaAnterior)
    ventana.configure(bg="lightblue")
    ventana.title("Tragamonedas")
    ventana.geometry("650x650")
    #Cargar jugadores
    jugadores = cargarJugadores()
    jugadorActual = None
    for jugador in jugadores:
        if jugador[0][0] == username:
            jugadorActual = jugador
            break
    if jugadorActual is None:
        messagebox.showerror("Error", "Jugador no encontrado")
        ventana.destroy()
        return
    #Titulo
    titulo = tkinter.Label(ventana,text="MÁQUINA TRAGAMONEDAS",font=("Georgia", 25, "bold"),fg="black",bg="lightblue")
    titulo.pack(pady=15)
    #Informacion del jugador
    textoJugador = tkinter.Label(ventana,text="Jugador: " + username,font=("Arial", 12),fg="black",bg="lightblue")
    textoJugador.pack(pady=5)
    #Puntaje
    textoPuntaje = tkinter.Label(ventana,text="",font=("Arial", 12),fg="black",bg="lightblue")
    textoPuntaje.pack(pady=5)
    #Fichas disponibles
    textoFichas = tkinter.Label(ventana,text="",font=("Arial", 12),fg="black",bg="lightblue")
    textoFichas.pack(pady=5)
    #Actualizar informacion
    def actualizarInformacion():
        textoPuntaje.config(text=f"Puntaje: {jugadorActual[2]}")
        textoFichas.config(
            text=f"Rojas: {jugadorActual[1][1]} | "
            f"Azules: {jugadorActual[1][2]} | "
            f"Verdes: {jugadorActual[1][3]} | "
            f"Blancas: {jugadorActual[1][4]}")
    actualizarInformacion()
    #Crear rodillos en pantalla
    marcoRodillos = tkinter.Frame(ventana,bg="lightblue")
    marcoRodillos.pack(pady=20)
    etiquetasRodillos = []
    for posicion in range(3):
        etiqueta = tkinter.Label( marcoRodillos, text="❔", font=("Arial", 40), width=3, bg="white")
        etiqueta.grid( row=0, column=posicion, padx=10)
        etiquetasRodillos.append(etiqueta)
    #Solicitar fichas para apostar
    textoApuesta = tkinter.Label(ventana,text="Seleccione las fichas que desea apostar:",font=("Arial", 13),fg="white",bg="lightblue")
    textoApuesta.pack(pady=10)
    colores = ["Rojas", "Azules", "Verdes", "Blancas"]
    entradas = []
    for color in colores:
        marco = tkinter.Frame(ventana, bg="lightblue")
        marco.pack(pady=2)
        etiqueta = tkinter.Label(marco,text=color + ":",font=("Arial", 11),fg="black",bg="lightblue",width=10)
        etiqueta.pack(side="left")
        entrada = tkinter.Entry(marco,font=("Arial", 11),width=10)
        entrada.insert(0, "0")
        entrada.pack(side="left")
        entradas.append(entrada)
    #Mensaje de resultados
    mensaje = tkinter.Label(ventana,text="¡Buena suerte!",font=("Arial", 13, "bold"),fg="green",bg="lightblue")
    mensaje.pack(pady=12)
    #Validar fichas apostadas
    def validarApuesta():
        fichasApostadas = []
        for posicion in range(4):
            try:
                cantidad = int(entradas[posicion].get())
            except ValueError:
                messagebox.showerror("Error","Debe ingresar cantidades enteras",parent=ventana)
                return None
            if cantidad < 0:
                messagebox.showerror("Error","No puede apostar fichas negativas",parent=ventana)
                return None
            if cantidad > jugadorActual[1][posicion + 1]:
                messagebox.showerror("Error",f"No tiene suficientes fichas {colores[posicion].lower()}",parent=ventana)
                return None
            fichasApostadas.append(cantidad)
        if sum(fichasApostadas) == 0:
            messagebox.showerror("Error","Debe apostar al menos una ficha",parent=ventana)
            return None
        return fichasApostadas
    #Limpiar entradas
    def limpiarEntradas():
        for entrada in entradas:
            entrada.delete(0, tkinter.END)
            entrada.insert(0, "0")
    #Animacion de los rodillos
    def animarRodillos(resultado, fichasApostadas):
        #Contador de animacion
        contador = [0]
        def animacion():
            if contador[0] < 20:
                for posicion in range(3):
                    simbolo = random.choice(rodillos[posicion])
                    etiquetasRodillos[posicion].config(
                        text=simbolo)
                contador[0] += 1
                ventana.after(150, animacion)
            else:
                #Mostrar resultado final
                for posicion in range(3):
                    etiquetasRodillos[posicion].config(
                        text=resultado[posicion])
                #Comprobar ganador
                gano = comprobarGanador(resultado)
                #Actualizar fichas y puntaje
                actualizarFichas(jugadorActual,fichasApostadas,gano)
                nuevoPuntaje = actualizarPuntaje(jugadorActual,gano)
                #Guardar resultados
                guardarJugadores(jugadores)
                #Actualizar informacion
                actualizarInformacion()
                #Mostrar resultado
                if gano:
                    mensaje.config(text="¡FELICIDADES! ¡GANASTE!\n"
                        f"Ganaste {sum(fichasApostadas)} fichas adicionales.\n"
                        f"Puntos obtenidos: +2",fg="green")
                else:
                    mensaje.config(text="¡PERDISTE!\n"
                        "Las fichas apostadas se perdieron.\n"
                        "Puntos obtenidos: -1",fg="red")
                #Habilitar boton
                botonGirar.config(state="normal")
                #Limpiar entradas
                limpiarEntradas()
        animacion()
    #Realizar jugada
    def realizarGiro():
        fichasApostadas = validarApuesta()
        if fichasApostadas is None:
            return
        #Confirmar apuesta
        confirmar = messagebox.askyesno("Confirmar apuesta",
            f"Rojas: {fichasApostadas[0]}\n"
            f"Azules: {fichasApostadas[1]}\n"
            f"Verdes: {fichasApostadas[2]}\n"
            f"Blancas: {fichasApostadas[3]}\n\n"
            "¿Desea realizar la apuesta?",parent=ventana)
        if confirmar:
            #Deshabilitar boton durante el giro
            botonGirar.config(state="disabled")
            mensaje.config(text="¡Los rodillos están girando!",fg="gray" )
            #Obtener resultado
            resultado = girarRodillos()
            #Iniciar animacion
            animarRodillos(resultado,fichasApostadas)
    #Boton girar
    botonGirar = tkinter.Button(ventana,text="GIRAR",font=("Arial", 16, "bold"),bg="gold",command=realizarGiro)
    botonGirar.pack(pady=10)
    #Boton volver
    botonVolver = tkinter.Button(ventana,text="Volver",font=("Arial", 13),command=ventana.destroy)
    botonVolver.pack(pady=5)

