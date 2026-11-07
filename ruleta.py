#Elaborado por: Fabiana Quesada y Juan Arias
#Fecha de creación: 6/11/2026
#Ultima modificacion:
#Version:3.14.7

#Importaciones
import random
import re
from tkinter import Toplevel,Label,Entry,Button
from jugadores import cargarJugadores, guardarJugadores
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
def obtenerMultiplicador(tipoApuesta, apuesta, resultado):
    """
    Funcionalidad:
    Obtiene el multiplicador de una apuesta
    según el resultado de la ruleta.
    Entrada:
    - tipoApuesta: Tipo de apuesta realizada.
    - apuesta: Color o número seleccionado.
    - resultado: Número y color obtenidos.
    Salida:
    - multiplicador: Multiplicador correspondiente.
    """
    if comprobarApuesta(tipoApuesta, apuesta, resultado):

        if tipoApuesta=="numero":
            return pagos["numero"]["multiplicador"]
        else:
            return pagos[apuesta]["multiplicador"]
    else:
        return 0
def actualizarFichas(jugador, fichasApostadas, multiplicador):
    """
    Funcionalidad:
    Descuenta las fichas apostadas y entrega
    el premio cuando el jugador gana.
    Entrada:
    - jugador:Datos del jugador.
    - fichasApostadas:Cantidades apostadas por color.
    - multiplicador:Multiplicador de la apuesta.
    Salida:
    - jugador:Datos del jugador actualizados.
    """
    for posicion in range(4):
        cantidad=fichasApostadas[posicion]
        # Descontar las fichas apostadas
        jugador[1][posicion+1]-=cantidad
        # Entregar el premio si gana
        if multiplicador>0:
            premio=cantidad * multiplicador
            jugador[1][posicion+1]+=premio
    return jugador
def actualizarPuntaje(jugador, puntos):
    """
    Funcionalidad:
    Actualiza el puntaje del jugador según
    los puntos obtenidos en la ruleta.

    Entrada:
    -jugador: Datos del jugador.
    -puntos: Puntos ganados o perdidos.
    Salida:
    - puntaje: Puntaje actualizado.
    """

    jugador[2] += puntos

    return jugador[2]
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
    ventana.geometry("500x400")
    titulo=Label(ventana,text="Juego de Ruleta",font=("Arial",16))
    titulo.pack(pady=20)
    # Cargar los jugadores
    jugadores=cargarJugadores()
    for jugador in jugadores:
        if jugador[0][0]==username:
            puntaje=jugador[2]
            textoPuntaje=Label(ventana,text=f"Jugador: {username} | Puntaje: {puntaje}")
            textoPuntaje.pack(pady=4)
            textoFichasDisponibles=Label(ventana,text=f"Rojas: {jugador[1][1]} | "
                     f"Azules: {jugador[1][2]} | "
                     f"Verdes: {jugador[1][3]} | "
                     f"Blancas: {jugador[1][4]}")
            textoFichasDisponibles.pack(pady=8)
            break
    #Solicita la apuesta
    textoApuesta=Label(ventana,text="Ingrese rojo, negro, verde o un número del 0 al 36 para apostar:")
    textoApuesta.pack(pady=8)
    entradaApuesta=Entry(ventana)
    entradaApuesta.pack(pady=8)
    textoFichas=Label(ventana, text="Fichas que desea apostar:")
    textoFichas.pack(pady=10)
    coloresFichas=["Rojas", "Azules", "Verdes", "Blancas"]
    entradasFichas=[]
    for color in coloresFichas:
        textoColor=Label(ventana, text=color)
        textoColor.pack()
        entrada=Entry(ventana)
        entrada.insert(0, "0")
        entrada.pack(pady=3)
        entradasFichas.append(entrada)
    mensaje=Label(ventana, text="")
    mensaje.pack(pady=8)
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
            jugadores=cargarJugadores()
            jugadorActual=None
            for jugador in jugadores:
                if jugador[0][0]==username:
                    jugadorActual=jugador
                    break
            if jugadorActual is None:
                mensaje.config(text="Jugador no encontrado")
                return
            # Validar las fichas apostadas
            totalFichas=0
            fichasApostadas=[]
            for posicion in range(4):
                try:
                    cantidad=int(entradasFichas[posicion].get())
                except ValueError:
                    mensaje.config(text="Ingrese cantidades enteras")
                    return
                if cantidad<0:
                    mensaje.config(text="No puede apostar fichas negativas")
                    return
                if cantidad>jugadorActual[1][posicion + 1]:
                    mensaje.config(text="No tiene fichas suficientes")
                    return
                totalFichas+=cantidad
                fichasApostadas.append(cantidad)
            if totalFichas==0:
                mensaje.config(text="Debe apostar al menos una ficha")
                return
            valoresFichas=[10,50,20,5]
            valorApuesta=0
            for posicion in range(4):
                valorApuesta+=fichasApostadas[posicion]*valoresFichas[posicion]
            def confirmarJugada():
                """
                Funcionalidad:
                Realiza la apuesta después de confirmarla
                y guarda los resultados del jugador.
                Entrada:
                - Ninguna.
                Salida:
                - Ninguna.
                """
                ventanaConfirmacion.destroy()
                resultado=girarRuleta()
                puntos=calcularPuntos(tipoApuesta, apuesta, resultado)
                multiplicador = obtenerMultiplicador(tipoApuesta, apuesta, resultado)
                # Actualizar fichas y puntaje
                actualizarFichas(jugadorActual, fichasApostadas, multiplicador)
                nuevoPuntaje=actualizarPuntaje(jugadorActual, puntos)
                guardarJugadores(jugadores)
                # Actualizar el puntaje en pantalla
                textoPuntaje.config(text=f"Jugador: {username} | Puntaje: {nuevoPuntaje}")
                # Actualizar las fichas en pantalla
                textoFichasDisponibles.config(text=f"Rojas: {jugadorActual[1][1]} | "
                         f"Azules: {jugadorActual[1][2]} | "
                         f"Verdes: {jugadorActual[1][3]} | "
                         f"Blancas: {jugadorActual[1][4]}")
                if multiplicador>0:mensaje.config(text=f"Salió el {resultado[0]} ({resultado[1]})\n"
                             f"¡Ganaste!\n"
                             f"Puntos de esta jugada: {puntos}\n"
                             f"Multiplicador: x{multiplicador}")
                else:
                    mensaje.config(text=f"Salió el {resultado[0]} ({resultado[1]})\n"
                             f"Perdiste la apuesta\n"
                             f"Puntos de esta jugada: {puntos}")
            # Ventana para confirmar la apuesta
            ventanaConfirmacion=Toplevel(ventana)
            ventanaConfirmacion.title("Confirmar apuesta")
            ventanaConfirmacion.geometry("300x300")
            textoConfirmacion=Label(ventanaConfirmacion,text=f"Apuesta: {apuesta}\n"
                     f"Rojas: {fichasApostadas[0]}\n"
                     f"Azules: {fichasApostadas[1]}\n"
                     f"Verdes: {fichasApostadas[2]}\n"
                     f"Blancas: {fichasApostadas[3]}\n\n"
                     f"Total apostado: ${valorApuesta}\n\n"
                     "¿Desea confirmar la apuesta?")
            textoConfirmacion.pack(pady=14)
            botonConfirmar=Button(ventanaConfirmacion,text="Confirmar",command=confirmarJugada)
            botonConfirmar.pack(pady=4)
            botonCancelar=Button(ventanaConfirmacion,text="Cancelar",command=ventanaConfirmacion.destroy)
            botonCancelar.pack(pady=4)
            ventanaConfirmacion.grab_set()
    #Botón para girar la ruleta
    botonGirar=Button(ventana, text="Girar Ruleta",command=realizarGiro)
    botonGirar.pack(pady=10)
    # Botón para regresar a la ventana anterior
    botonVolver = Button(ventana, text="Volver",command=ventana.destroy)
    botonVolver.pack(pady=10)
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
        "multiplicador": 3,
        "puntos": 2
    }
}
