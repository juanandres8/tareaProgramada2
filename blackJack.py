#Elaborado por: Fabiana Quesada y Juan Arias
#Fecha de creación: 
#Ultima modificacion:
#Version:3.14.7

#Importaciones
import random
from tkinter import *
from jugadores import *
#Funciones
def crearMazo():
    """
    Funcionalidad:
    Crea un mazo de 52 cartas utilizando una lista de tuplas.
    Entrada:
    -Ninguna.
    Salida:
    - mazo:Lista de tuplas con palo, nombre y valor.
    """
    palos=["Corazones", "Diamantes", "Treboles", "Picas"]
    cartas=[
        ("As","1/11"),
        ("2","2"),
        ("3","3"),
        ("4","4"),
        ("5","5"),
        ("6","6"),
        ("7","7"),
        ("8","8"),
        ("9","9"),
        ("10","10"),
        ("J","10"),
        ("Q","10"),
        ("K","10")
    ]
    mazo=[]
    for palo in palos:
        for nombre,valor in cartas:
            mazo.append((palo, nombre, valor))
    return mazo
def barajarMazo():
    """
    Funcionalidad:
    Crea y mezcla aleatoriamente las cartas del mazo.
    Entrada:
    - Ninguna.
    Salida:
    - mazo: Lista de 52 cartas mezcladas.
    """
    mazo=crearMazo()
    random.shuffle(mazo)#Mezcla las cartas
    return mazo
def repartirCartas(mazo):
    """
    Funcionalidad:
    Reparte dos cartas al jugador y dos al crupier.
    Entrada:
    - mazo: Lista de cartas mezcladas.
    Salida:
    - manoJugador: Cartas del jugador.
    - manoCrupier: Cartas del crupier.
    """
    manoJugador=[]
    manoCrupier=[]
    for i in range(2):
        manoJugador.append(mazo.pop())
        manoCrupier.append(mazo.pop())
    return manoJugador,manoCrupier
def calcularMano(mano):
    """
    Funcionalidad:
    Calcula el valor de las cartas de una mano,
    considerando que el As puede valer 1 u 11.
    Entrada:
    - mano: Lista de tuplas con las cartas.
    Salida:
    - total: Puntos totales de la mano.
    """
    total=0
    ases=0
    for carta in mano:
        if carta[2]=="1/11":
            total+=11
            ases+=1
        else:
            total+=int(carta[2])
    while total>21 and ases>0:
        total-=10
        ases-=1
    return total
def pedirCarta(mazo, mano):
    """
    Funcionalidad:
    Extrae una carta del mazo y la agrega
    a la mano del jugador.
    Entrada:
    - mazo: Lista de cartas disponibles.
    - mano: Cartas actuales del jugador.
    Salida:
    - mano: Mano con la nueva carta.
    """
    carta=mazo.pop()
    mano.append(carta)
    return mano
def turnoCrupier(mazo, manoCrupier):
    """
    Funcionalidad:Permite al crupier pedir cartas mientrastenga 16 puntos o menos.
    Entrada:
    - mazo): Cartas disponibles.
    - manoCrupier: Cartas actuales del crupier.
    Salida:
    - manoCrupier: Mano final del crupier.
    """
    while calcularMano(manoCrupier)<=16 and len(mazo)>0:
        pedirCarta(mazo,manoCrupier)
    return manoCrupier
def determinarGanador(manoJugador, manoCrupier):
    """
    Funcionalidad:
    Compara los puntos del jugador y del crupier
    para determinar quién gana la partida.
    Entrada:
    - manoJugador: Cartas del jugador.
    - manoCrupier: Cartas del crupier.
    Salida:
    - ganador: Resultado de la partida.
    """
    puntosJugador=calcularMano(manoJugador)
    puntosCrupier=calcularMano(manoCrupier)
    if puntosJugador>21:
        return "crupier"
    elif puntosCrupier>21:
        return "jugador"
    elif puntosJugador>puntosCrupier:
        return "jugador"
    elif puntosCrupier>puntosJugador:
        return "crupier"
    else:
        return "empate"
def calcularPagoBlackjack(ganador,fichasApostadas):
    """
    Funcionalidad:
    Calcula las fichas que recibe el jugador
    según el resultado de la partida.
    Entrada:
    - ganador: Resultado de la partida.
    - fichasApostadas: Fichas apostadas por color.
    Salida:
    - fichasGanadas: Cantidades de fichas que recibe.
    """
    fichasGanadas=[]
    for cantidad in fichasApostadas:
        if ganador=="jugador":
            fichasGanadas.append(cantidad * 2)
        elif ganador=="empate":
            fichasGanadas.append(cantidad)
        else:
            fichasGanadas.append(0)
    return fichasGanadas
def actualizarFichasBlackjack(jugador,fichasApostadas,ganador):
    """
    Funcionalidad:
    Actualiza las fichas del jugador según
    el resultado de la partida de Blackjack.
    Entrada:
    - jugador: Datos del jugador.
    - fichasApostadas: Cantidades apostadas por color.
    - ganador: Resultado de la partida.
    Salida:
    - jugador: Datos del jugador actualizados.
    """
    fichasGanadas=calcularPagoBlackjack(ganador,fichasApostadas)
    for posicion in range(4):
        #Descontar las fichas apostadas
        jugador[1][posicion+1]-=fichasApostadas[posicion]
        #Entregar las fichas correspondientes
        jugador[1][posicion+1]+=fichasGanadas[posicion]
    return jugador
def ventanaBlackjack(ventanaL, username):
    """
    Funcionalidad:
    Crea la ventana gráfica del juego Blackjack.
    Entrada:
    - ventanaL: Ventana anterior.
    - username: Nombre de usuario del jugador.
    Salida:
    - Ninguna.
    """
    ventana=Toplevel(ventanaL)
    ventana.title("Blackjack")
    ventana.geometry("600x750")
    titulo=Label(ventana, text="Juego de Blackjack",font=("Arial", 16))
    titulo.pack(pady=20)
    textoJugador=Label(ventana,text=f"Jugador: {username}")
    textoJugador.pack(pady=11)
    #Cargar los jugadores registrados
    jugadores=cargarJugadores()
    for jugador in jugadores:
        if jugador[0][0]==username:
            textoFichasDisponibles = Label(ventana,text=f"Rojas: {jugador[1][1]} | "
                     f"Azules: {jugador[1][2]} | "
                     f"Verdes: {jugador[1][3]} | "
                     f"Blancas: {jugador[1][4]}")
            textoFichasDisponibles.pack(pady=5)
            break
    #Espacio para las cartas del crupier
    textoCrupier=Label(ventana,text="Cartas del crupier:",font=("Arial", 11))
    textoCrupier.pack(pady=10)
    cartasCrupier=Label(ventana, text="Sin cartas")
    cartasCrupier.pack(pady=5)
    #Espacio para las cartas del jugador
    textoCartasJugador=Label(ventana,text="Tus cartas:",font=("Arial", 11))
    textoCartasJugador.pack(pady=10)
    cartasJugador=Label(ventana, text="Sin cartas")
    cartasJugador.pack(pady=5)
    #Seleccionar las fichas para apostar
    textoFichas=Label(ventana, text="Fichas que desea apostar:")
    textoFichas.pack(pady=10)
    coloresFichas=["Rojas", "Azules", "Verdes", "Blancas"]
    entradasFichas=[]
    frameFichas=Frame(ventana)
    frameFichas.pack(pady=5)
    for color in coloresFichas:
        columna=Frame(frameFichas)
        columna.pack(side="left", padx=8)
        textoColor=Label(columna, text=color)
        textoColor.pack()
        entrada=Entry(columna, width=8)
        entrada.insert(0, "0")
        entrada.pack(pady=4)
        entradasFichas.append(entrada)
    mensaje=Label(ventana,text="")
    mensaje.pack(pady=10)
    def validarApuesta():
        """
        Funcionalidad:
        Comprueba que el jugador tenga suficientes
        fichas para realizar una apuesta.
        Entrada:
        - Ninguna.
        Salida:
        - fichasApostadas: Cantidades
          válidas o None si la apuesta es inválida.
        """
        jugadores=cargarJugadores()
        jugadorActual=None
        for jugador in jugadores:
            if jugador[0][0]==username:
                jugadorActual=jugador
                break
        if jugadorActual is None:
            mensaje.config(text="Jugador no encontrado")
            return None
        fichasApostadas=[]
        totalFichas=0
        for posicion in range(4):
            try:
                cantidad=int(entradasFichas[posicion].get())
            except ValueError:
                mensaje.config(text="Ingrese cantidades enteras")
                return None
            if cantidad<0:
                mensaje.config(text="No puede apostar fichas negativas")
                return None
            if cantidad>jugadorActual[1][posicion + 1]:
                mensaje.config(text="No tiene fichas suficientes")
                return None
            fichasApostadas.append(cantidad)
            totalFichas+=cantidad
        if totalFichas==0:
            mensaje.config(text="Debe apostar al menos una ficha")
            return None
        mensaje.config(text="Apuesta válida")
        return fichasApostadas
    #Botón para validar la apuesta
    botonValidar=Button(ventana,text="Validar apuesta",command=validarApuesta)
    botonValidar.pack(pady=10)
    # Datos de la partida actual
    partida={}
    def iniciarPartida():
        """
        Funcionalidad:
        Valida la apuesta y solicita confirmación
        antes de repartir las cartas.
        Entrada:
        - Ninguna.
        Salida:
        - Ninguna.
        """
        fichasApostadas=validarApuesta()
        if fichasApostadas is None:
            return
        def confirmarPartida():
            """
            Funcionalidad:
            Baraja el mazo y reparte las cartas
            al jugador y al crupier.
            Entrada:
            - Ninguna.
            Salida:
            - Ninguna.
            """
            ventanaConfirmacion.destroy()
            partida["mazo"]=barajarMazo()
            partida["manoJugador"],partida["manoCrupier"]=repartirCartas(partida["mazo"])
            partida["fichasApostadas"]=fichasApostadas
            partida["finalizada"]=False
            #Mostrar las cartas del jugador
            cartasJugador.config(text=f"{partida['manoJugador'][0]}\n"
                     f"{partida['manoJugador'][1]}\n"
                     f"Puntos: {calcularMano(partida['manoJugador'])}")
            #Mostrar solo una carta del crupier
            cartasCrupier.config(text=f"{partida['manoCrupier'][0]}\n""Carta oculta")
            botonIniciar.config(state="disabled")
            botonPlantarse.config(state="normal")
            if calcularMano(partida["manoJugador"])<21:
                botonPedir.config(state="normal")
            mensaje.config(text="Cartas repartidas")
        # Ventana para confirmar la apuesta
        ventanaConfirmacion=Toplevel(ventana)
        ventanaConfirmacion.title("Confirmar apuesta")
        ventanaConfirmacion.geometry("300x300")
        textoConfirmacion=Label(ventanaConfirmacion,text=f"Rojas: {fichasApostadas[0]}\n"
                 f"Azules: {fichasApostadas[1]}\n"
                 f"Verdes: {fichasApostadas[2]}\n"
                 f"Blancas: {fichasApostadas[3]}\n\n"
                 "¿Desea confirmar la apuesta?")
        textoConfirmacion.pack(pady=15)
        botonConfirmar=Button(ventanaConfirmacion,text="Confirmar",command=confirmarPartida)
        botonConfirmar.pack(pady=5)
        botonCancelar = Button(ventanaConfirmacion,text="Cancelar",command=ventanaConfirmacion.destroy)
        botonCancelar.pack(pady=5)
        ventanaConfirmacion.grab_set()
    botonIniciar=Button(ventana,text="Iniciar partida",command=iniciarPartida)
    botonIniciar.pack(pady=10)   
    def pedirCartaJugador():
        """
        Funcionalidad:
        Permite al jugador recibir otra carta y
        actualiza los puntos de su mano.
        Entrada:
        - Ninguna.
        Salida:
        - Ninguna.
        """
        pedirCarta(partida["mazo"], partida["manoJugador"])
        #Muestra todas las cartas del jugador
        textoCartas=""
        for carta in partida["manoJugador"]:
            textoCartas+=str(carta)+"\n"
        puntos=calcularMano(partida["manoJugador"])
        cartasJugador.config(text=textoCartas + f"Puntos: {puntos}")
        if puntos>21:
            mensaje.config(text="Te pasaste de 21. Gana el crupier.")
            finalizarPartida("crupier")
        elif puntos==21:
            mensaje.config(text="Llegaste a 21 puntos.")
            botonPedir.config(state="disabled")
        else:
            mensaje.config(text="Puedes pedir otra carta o plantarte.")
    #Botón para pedir otra carta
    frameBotones=Frame(ventana)
    frameBotones.pack(pady=5)
    botonPedir=Button(frameBotones,text="Pedir carta",command=pedirCartaJugador,state="disabled")
    botonPedir.pack(side="left",padx=10)
    def plantarse():
        """
        Funcionalidad:
        Finaliza el turno del jugador, permite jugar
        al crupier y determina el ganador.
        Entrada:
        - Ninguna.
        Salida:
        - Ninguna.
        """
        turnoCrupier(partida["mazo"],partida["manoCrupier"])
        # Mostrar las cartas del crupier
        textoCartas=""
        for carta in partida["manoCrupier"]:
            textoCartas+=str(carta)+"\n"
        puntosCrupier=calcularMano(partida["manoCrupier"])
        cartasCrupier.config(text=textoCartas + f"Puntos: {puntosCrupier}")
        # Determinar quién ganó
        ganador=determinarGanador(partida["manoJugador"],partida["manoCrupier"])
        if ganador=="jugador":
            mensaje.config(text="¡Ganaste la partida!")
        elif ganador=="crupier":
            mensaje.config(text="Ganó el crupier")
        else:
            mensaje.config(text="Nadie ganó. Empate")
        #Terminar la partida
        finalizarPartida(ganador)
    #Botón para plantarse
    botonPlantarse=Button(frameBotones,text="Plantarse",command=plantarse,state="disabled")
    botonPlantarse.pack(side="left",padx=10)
    def finalizarPartida(ganador):
        """
        Funcionalidad:
        Actualiza y guarda las fichas del jugador
        al terminar la partida de Blackjack.
        Entrada:
        - ganador: Resultado de la partida.
        Salida:
        - Ninguna.
        """
        if partida["finalizada"]:
            return
        jugadores=cargarJugadores()
        for jugador in jugadores:
            if jugador[0][0]==username:
                #Actualizar las fichas
                actualizarFichasBlackjack(jugador,partida["fichasApostadas"],ganador)
                #Guardar los cambios
                guardarJugadores(jugadores)
                #Actualizar las fichas en pantalla
                textoFichasDisponibles.config(text=f"Rojas: {jugador[1][1]} | "
                         f"Azules: {jugador[1][2]} | "
                         f"Verdes: {jugador[1][3]} | "
                         f"Blancas: {jugador[1][4]}")
                partida["finalizada"] = True
                botonPedir.config(state="disabled")
                botonPlantarse.config(state="disabled")
                return
        mensaje.config(text="Jugador no encontrado")
    
    
