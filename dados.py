# Elaborado por: Fabiana Quesada y Juan Arias
# Fecha de creación: 15/11/2026
# Ultima modificacion: 15/11/2026
# Version: 3.14.7

# Importaciones
import random
import tkinter
from tkinter import Toplevel, Label, Entry, Button, Radiobutton, StringVar, messagebox
from jugadores import cargarJugadores, guardarJugadores


# Diccionario con los valores de las fichas
valoresFichas = {"rojas": 10,"azules": 50,"verdes": 20,"blancas": 5}
# Diccionario con los pagos del juego
pagosDados = {"ganar": {"multiplicador": 2, "puntos": 1},"perder": {"multiplicador": 0, "puntos": -1}}
# Funcion A: Lanzar los dados
def lanzarDados():
    '''
    Funcionalidad:
    Genera el resultado aleatorio de dos dados.
    Entrada:
    - Ninguna.
    Salida:
    - resultado(tuple): Tupla con los dos valores obtenidos.
    '''
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    resultado = (dado1, dado2)
    return resultado
# Funcion B: Comprobar si el jugador gano
def comprobarApuesta(tipoApuesta, apuesta, resultado):
    '''
    Funcionalidad:
    Comprueba si el resultado de los dados coincide con la apuesta.
    Entrada:
    - tipoApuesta(str): Tipo de apuesta seleccionada.
    - apuesta(str): Valor o condicion apostada.
    - resultado(tuple): Resultado de los dos dados.
    Salida:
    - gano(bool): Indica si el jugador gano.
    '''
    dado1 = resultado[0]
    dado2 = resultado[1]
    suma = dado1 + dado2
    gano = False
    if tipoApuesta == "Suma exacta":
        if suma == int(apuesta):
            gano = True
    elif tipoApuesta == "Par o impar":
        apuesta = apuesta.strip().lower()
        if apuesta == "par" and suma % 2 == 0:
            gano = True
        elif apuesta == "impar" and suma % 2 != 0:
            gano = True
    elif tipoApuesta == "Dobles":
        if dado1 == dado2:
            gano = True
    return gano
# Funcion C: Actualizar las fichas del jugador
def actualizarFichas(jugador, fichasApostadas, multiplicador):
    '''
    Funcionalidad:
    Descuenta las fichas apostadas y agrega el pago correspondiente.
    Entrada:
    - jugador(list): Informacion del jugador.
    - fichasApostadas(list): Cantidad apostada de cada color.
    - multiplicador(int): Multiplicador del premio.
    Salida:
    - Ninguna.
    '''
    for posicion in range(4):
        jugador[1][posicion + 1] -= fichasApostadas[posicion]
        jugador[1][posicion + 1] += (fichasApostadas[posicion] * multiplicador)
# Funcion D: Actualizar el puntaje
def actualizarPuntaje(jugador, puntos):
    '''
    Funcionalidad:
    Actualiza el puntaje general del jugador.
    Entrada:
    - jugador(list): Informacion del jugador.
    - puntos(int): Puntos ganados o perdidos.
    Salida:
    - puntaje(int): Nuevo puntaje del jugador.
    '''
    jugador[2] += puntos
    return jugador[2]
# Funcion E: Ventana principal del juego
def ventanaDados(ventanaAnterior, username):
    '''
    Funcionalidad:
    Muestra la interfaz del juego de dados y permite realizar apuestas.
    Entrada:
    - ventanaAnterior: Ventana desde la que se ingreso al juego.
    - username(str): Nombre del jugador.
    Salida:
    - Ninguna.
    '''
    jugadores = cargarJugadores()
    jugadorActual = None
    for jugador in jugadores:
        if jugador[0][0] == username:
            jugadorActual = jugador
            break
    if jugadorActual is None:
        messagebox.showerror("Error", "No se encontro el jugador")
        return
    ventana = Toplevel(ventanaAnterior)
    ventana.title("Juego de Dados")
    ventana.geometry("520x700")
    ventana.config(bg="#ADD8E6")
    colorFondo = "#ADD8E6"
    colorTexto = "#102A43"
    # Mostrar informacion del jugador
    textoPuntaje = Label(ventana,
        text=f"Jugador: {username} | Puntaje: {jugadorActual[2]}",
        font=("Times New Roman", 12),
        bg=colorFondo,
        fg=colorTexto)
    textoPuntaje.pack(pady=10)
    textoFichasDisponibles = Label(ventana,
        text=f"Rojas: {jugadorActual[1][1]} | "
             f"Azules: {jugadorActual[1][2]} | "
             f"Verdes: {jugadorActual[1][3]} | "
             f"Blancas: {jugadorActual[1][4]}",font=("Times New Roman", 10),bg=colorFondo,fg=colorTexto)
    textoFichasDisponibles.pack(pady=5)
    Label(ventana,text="Seleccione el tipo de apuesta:",font=("Times New Roman", 13),bg=colorFondo,fg=colorTexto).pack(pady=5)
    # Variable que almacena el tipo de apuesta seleccionado
    tipoApuesta = StringVar(ventana)
    tipoApuesta.set("Suma exacta")
    # Etiqueta que muestra la indicacion correspondiente
    indicacionApuesta = Label(ventana, text="Ingrese un numero entero entre 2 y 12.", font=("Times New Roman", 10),bg=colorFondo,fg=colorTexto)
    indicacionApuesta.pack(pady=5)
    # Funcion para cambiar la indicacion segun la apuesta
    def cambiarIndicacion():
        tipo = tipoApuesta.get()
        if tipo == "Suma exacta":
            indicacionApuesta.config( text="Ingrese un numero entero entre 2 y 12.")
        elif tipo == "Par o impar":
            indicacionApuesta.config(text="Escriba Par o Impar.")
        elif tipo == "Dobles":
            indicacionApuesta.config(text="Deje la casilla vacia para apostar a Dobles.")
    # Boton para apostar a una suma exacta
    Radiobutton(ventana,text="Suma exacta",variable=tipoApuesta,value="Suma exacta", bg=colorFondo,fg=colorTexto,selectcolor="white",command=cambiarIndicacion).pack()
    # Boton para apostar a par o impar
    Radiobutton(ventana,text="Par o impar",variable=tipoApuesta,value="Par o impar", bg=colorFondo, fg=colorTexto,selectcolor="white",command=cambiarIndicacion).pack()
    # Boton para apostar a dobles
    Radiobutton(ventana,text="Dobles",variable=tipoApuesta, value="Dobles",bg=colorFondo, fg=colorTexto,selectcolor="white",command=cambiarIndicacion).pack()
    # Entrada para escribir el pronostico
    Label(ventana,text="Pronostico:",font=("Times New Roman", 10),bg=colorFondo,fg=colorTexto ).pack(pady=3)
    entradaApuesta = Entry(ventana, font=("Times New Roman", 10))
    entradaApuesta.pack(pady=5)
    # Mensaje para mostrar errores y resultados
    mensaje = Label(ventana,text="Ingrese su pronostico y las fichas que desea apostar.",font=("Times New Roman", 11),bg=colorFondo,fg=colorTexto,wraplength=470)
    mensaje.pack(pady=8)
    # Entradas para las cantidades de fichas
    entradasFichas = []
    colores = ["Rojas", "Azules", "Verdes", "Blancas"]
    Label(ventana,text="Cantidad de fichas que desea apostar:",font=("Times New Roman", 10),bg=colorFondo,fg=colorTexto).pack(pady=3)
    for color in colores:
        Label(ventana, text=color, bg=colorFondo,fg=colorTexto).pack()
        entrada = Entry(ventana,font=("Times New Roman", 10),width=12)
        entrada.pack(pady=2)
        entradasFichas.append(entrada)
    # Funcion para realizar el lanzamiento
    def realizarLanzamiento():
        tipo = tipoApuesta.get()
        apuesta = entradaApuesta.get().strip()
        # VALIDACION 1: SUMA EXACTA
        if tipo == "Suma exacta":
            # Comprobar que sea un numero entero
            if not apuesta.isdigit():
                mensaje.config(text="Para Suma exacta debe ingresar un numero entero entre 2 y 12.")
                return
            # Comprobar que este entre 2 y 12
            if int(apuesta) < 2 or int(apuesta) > 12:
                mensaje.config(text="La suma debe estar entre 2 y 12.")
                return
        # VALIDACION 2: PAR O IMPAR
        elif tipo == "Par o impar":
            # Convertir el texto a minusculas
            apuesta = apuesta.lower()
            # Comprobar que escribio Par o Impar
            if apuesta != "par" and apuesta != "impar":
                mensaje.config(text="Debe escribir Par o Impar.")
                return
            apuesta = apuesta.capitalize()
        # VALIDACION 3: DOBLES
        elif tipo == "Dobles":
            # Comprobar que la casilla este vacia
            if apuesta != "":
                mensaje.config(text="Para Dobles debe dejar la casilla vacia.")
                return
            apuesta = "Dobles"
        # Leer y validar las fichas apostadas
        fichasApostadas = []
        totalFichas = 0
        valorApuesta = 0
        valoresPorPosicion = [
            valoresFichas["rojas"],
            valoresFichas["azules"],
            valoresFichas["verdes"],
            valoresFichas["blancas"]]
        for posicion in range(4):
            textoCantidad = entradasFichas[posicion].get().strip()
            if textoCantidad == "":
                cantidad = 0
            else:
                try:
                    cantidad = int(textoCantidad)
                except ValueError:
                    mensaje.config(text="Ingrese cantidades enteras de fichas.")
                    return
            if cantidad < 0:
                mensaje.config( text="No puede apostar fichas negativas.")
                return
            if cantidad > jugadorActual[1][posicion + 1]:
                mensaje.config(text=f"No tiene suficientes fichas {colores[posicion].lower()}.")
                return
            fichasApostadas.append(cantidad)
            totalFichas += cantidad
            valorApuesta += cantidad * valoresPorPosicion[posicion]
        if totalFichas == 0:
            mensaje.config(text="Debe apostar al menos una ficha.")
            return
        # Ventana para confirmar la apuesta
        ventanaConfirmacion = Toplevel(ventana)
        ventanaConfirmacion.title("Confirmar apuesta")
        ventanaConfirmacion.geometry("340x360")
        ventanaConfirmacion.config(bg=colorFondo)
        textoConfirmacion = Label(ventanaConfirmacion,
            text=f"Tipo de apuesta: {tipo}\n"
                 f"Pronostico: {apuesta}\n\n"
                 f"Fichas rojas: {fichasApostadas[0]}\n"
                 f"Fichas azules: {fichasApostadas[1]}\n"
                 f"Fichas verdes: {fichasApostadas[2]}\n"
                 f"Fichas blancas: {fichasApostadas[3]}\n\n"
                 f"Total de fichas: {totalFichas}\n"
                 f"Monto apostado: ${valorApuesta}\n\n"
                 "¿Desea confirmar la apuesta?",
            bg=colorFondo,fg=colorTexto,font=("Times New Roman", 10))
        textoConfirmacion.pack(pady=15)
        # Funcion para confirmar la jugada
        def confirmarJugada():
            ventanaConfirmacion.destroy()
            resultado = lanzarDados()
            gano = comprobarApuesta(tipo,apuesta,resultado)
            if gano:
                multiplicador = pagosDados["ganar"]["multiplicador"]
                puntos = pagosDados["ganar"]["puntos"]
            else:
                multiplicador = pagosDados["perder"]["multiplicador"]
                puntos = pagosDados["perder"]["puntos"]
            # Actualizar las fichas y el puntaje
            actualizarFichas(jugadorActual,fichasApostadas,multiplicador)
            nuevoPuntaje = actualizarPuntaje(jugadorActual,puntos)
            guardarJugadores(jugadores)
            # Actualizar informacion en pantalla
            textoPuntaje.config(text=f"Jugador: {username} | Puntaje: {nuevoPuntaje}")
            textoFichasDisponibles.config(text=f"Rojas: {jugadorActual[1][1]} | "
                     f"Azules: {jugadorActual[1][2]} | "
                     f"Verdes: {jugadorActual[1][3]} | "
                     f"Blancas: {jugadorActual[1][4]}")
            if gano:
                mensaje.config(text=f"Dados: {resultado}\n"
                         f"Suma: {resultado[0] + resultado[1]}\n"
                         f"¡Ganaste!\n"
                         f"Puntos obtenidos: {puntos}" )
            else:
                mensaje.config(text=f"Dados: {resultado}\n"
                         f"Suma: {resultado[0] + resultado[1]}\n"
                         f"Perdiste la apuesta.\n"
                         f"Puntos obtenidos: {puntos}")
            # Limpiar las entradas
            entradaApuesta.delete(0, tkinter.END)
            for entrada in entradasFichas:
                entrada.delete(0, tkinter.END)
        # Boton para confirmar
        Button(ventanaConfirmacion,text="Confirmar",command=confirmarJugada).pack(pady=3)
        # Boton para cancelar
        Button(ventanaConfirmacion,text="Cancelar",command=ventanaConfirmacion.destroy).pack(pady=3)
        ventanaConfirmacion.grab_set()
    # Boton para lanzar los dados
    Button(ventana,text="Lanzar dados",font=("Times New Roman", 12),command=realizarLanzamiento).pack(pady=10)
    # Boton para volver
    Button(ventana,text="Volver",font=("Times New Roman", 10),command=ventana.destroy).pack(pady=3)
