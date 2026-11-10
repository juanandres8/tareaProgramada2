#Elaborado por: Fabiana Quesada y Juan Arias
#Fecha de creación: 10/11/2026
#Ultima modificacion:
#Version:3.14.7

#Importaciones
import tkinter
from tkinter import messagebox
from jugadores import cargarJugadores, guardarJugadores

#Diccionario con el valor de cada ficha
valoresFichas = {"rojas": 10,"azules": 50,"verdes": 20,"blancas": 5}

#Definicion de funciones
def ventanaFichas(ventanaAnterior, username):
    """
    Funcionalidad:
    Crea y muestra la ventana para comprar y canjear fichas.
    Entradas:
    - ventanaAnterior: Ventana desde la cual se abre.
    - username: Nombre del jugador.
    Salidas:
    - Ninguna.
    """
    #Crear ventana
    ventana = tkinter.Toplevel(ventanaAnterior)
    ventana.configure(bg="lightblue")
    ventana.title("Administrar fichas")
    ventana.geometry("600x650")
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
    titulo = tkinter.Label(ventana,
        text="Administración de fichas",
        font=("Georgia", 24),
        bg="lightblue")
    titulo.pack(pady=15)
    #Informacion del jugador
    etiquetaJugador = tkinter.Label(ventana,
        text="Jugador: " + username,
        font=("Arial", 12),
        bg="lightblue")
    etiquetaJugador.pack(pady=5)
    #Mostrar dinero disponible
    etiquetaDinero = tkinter.Label(ventana,
        text="Dinero disponible: $" + str(jugadorActual[1][0]),
        font=("Arial", 14),
        bg="lightblue")
    etiquetaDinero.pack(pady=10)
    #Mostrar fichas disponibles
    etiquetaFichas = tkinter.Label(ventana,
        text="",
        font=("Arial", 12),
        bg="lightblue")
    etiquetaFichas.pack(pady=10)
    #Mostrar valores de las fichas
    etiquetaValores = tkinter.Label(ventana,
        text="Valor de las fichas:\n"
        "Rojas: $10 | Azules: $50\n"
        "Verdes: $20 | Blancas: $5",
        font=("Arial", 12),
        bg="lightblue")
    etiquetaValores.pack(pady=10)
    #Actualizar informacion
    def actualizarInformacion():
        etiquetaDinero.config( text=f"Dinero disponible: ${jugadorActual[1][0]}")
        etiquetaFichas.config(
            text=f"Fichas disponibles:\n"
            f"Rojas: {jugadorActual[1][1]} | "
            f"Azules: {jugadorActual[1][2]}\n"
            f"Verdes: {jugadorActual[1][3]} | "
            f"Blancas: {jugadorActual[1][4]}")
    actualizarInformacion()
    #Campos para ingresar cantidades
    tituloCantidad = tkinter.Label( ventana,
        text="Ingrese la cantidad de fichas:",
        font=("Arial", 13),
        bg="lightblue")
    tituloCantidad.pack(pady=10)
    colores = ["rojas", "azules", "verdes", "blancas"]
    entradas = []
    for color in colores:
        etiquetaColor = tkinter.Label(ventana,
            text=color.capitalize(),
            font=("Arial", 11),
            bg="lightblue")
        etiquetaColor.pack()
        entrada = tkinter.Entry(ventana,font=("Arial", 11))
        entrada.insert(0, "0")
        entrada.pack(pady=3)
        entradas.append(entrada)
    #Obtener cantidades ingresadas
    def obtenerCantidades():
        cantidades = []
        for entrada in entradas:
            try:
                cantidad = int(entrada.get())
                if cantidad < 0:
                    messagebox.showerror("Error","No puede ingresar cantidades negativas")
                    return None
                cantidades.append(cantidad)
            except ValueError:
                messagebox.showerror("Error","Debe ingresar cantidades enteras")
                return None
        if sum(cantidades) == 0:
            messagebox.showerror("Error","Debe ingresar al menos una ficha")
            return None
        return cantidades
    #Comprar fichas
    def comprarFichas():
        cantidades = obtenerCantidades()
        if cantidades is None:
            return
        total = 0
        for posicion in range(4):
            total += cantidades[posicion] * valoresFichas[colores[posicion]]
        if total > jugadorActual[1][0]:
            messagebox.showerror("Compra","No tiene suficiente dinero")
            return
        confirmar = messagebox.askyesno(
            "Confirmar compra",
            f"Total de la compra: ${total}\n"
            "¿Desea realizar la compra?" )
        if confirmar:
            jugadorActual[1][0] -= total
            for posicion in range(4):
                jugadorActual[1][posicion + 1] += cantidades[posicion]
            guardarJugadores(jugadores)
            actualizarInformacion()
            messagebox.showinfo("Compra","Compra realizada correctamente")
    #Canjear fichas
    def canjearFichas():
        cantidades = obtenerCantidades()
        if cantidades is None:
            return
        #Comprobar que tenga suficientes fichas
        for posicion in range(4):
            if cantidades[posicion] > jugadorActual[1][posicion + 1]:
                messagebox.showerror( "Canje",f"No tiene suficientes fichas {colores[posicion]}")
                return
        #Calcular dinero que recibirá
        total = 0
        for posicion in range(4):
            total += cantidades[posicion] * valoresFichas[colores[posicion]]
        confirmar = messagebox.askyesno("Confirmar canje",f"Dinero que recibirá: ${total}\n""¿Desea realizar el canje?" )
        if confirmar:
            jugadorActual[1][0] += total
            for posicion in range(4):
                jugadorActual[1][posicion + 1] -= cantidades[posicion]
            guardarJugadores(jugadores)
            actualizarInformacion()
            messagebox.showinfo( "Canje","Canje realizado correctamente")
    #Botones
    botonComprar = tkinter.Button(ventana,
        text="Comprar fichas",
        font=("Times New Roman", 14),
        command=comprarFichas)
    botonComprar.pack(pady=10)
    botonCanjear = tkinter.Button(ventana,
        text="Canjear fichas",
        font=("Times New Roman", 14),
        command=canjearFichas)
    botonCanjear.pack(pady=10)
    #Boton volver
    botonVolver = tkinter.Button( ventana,
        text="Volver",
        font=("Times New Roman", 14),
        command=ventana.destroy)
    botonVolver.pack(pady=10)
