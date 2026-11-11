#Elaborado por: Fabiana Quesada y Juan Arias
#Fecha de creación: 10/11/2026
#Ultima modificacion:
#Version:3.14.7

#Importaciones
import tkinter
from tkinter import messagebox, simpledialog
from jugadores import cargarJugadores, guardarJugadores

#Diccionario con el valor de cada ficha
valoresFichas = {
    "rojas": 10,
    "azules": 50,
    "verdes": 20,
    "blancas": 5}
#Definicion de funciones
def ventanaFichas(ventanaAnterior, username):
    """
    Funcionalidad:
    Crea y muestra la ventana para comprar y canjear fichas.
    Entradas:
    - ventanaAnterior: Ventana principal desde donde se abre.
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
        ventanaAnterior.deiconify()
        return
    #Titulo
    titulo = tkinter.Label(ventana,
        text="Administración de fichas",
        font=("Georgia", 24),
        bg="lightblue" )
    titulo.pack(pady=5)
    #Username
    etiquetaJugador = tkinter.Label(ventana,
        text="Jugador: " + username,
        font=("Arial", 12),
        bg="lightblue")
    etiquetaJugador.pack(pady=5)
    #Dinero disponible
    etiquetaDinero = tkinter.Label(ventana,
        text="",
        font=("Arial", 14),
        bg="lightblue")
    etiquetaDinero.pack(pady=5)
    #Fichas disponibles
    etiquetaFichas = tkinter.Label(ventana,
        text="",
        font=("Arial", 12),
        bg="lightblue")
    etiquetaFichas.pack(pady=10)
    #Valores de las fichas
    etiquetaValores = tkinter.Label(ventana,
        text="Valor de las fichas:\n"
        "Rojas: $10 | Azules: $50\n"
        "Verdes: $20 | Blancas: $5",
        font=("Arial", 12),
        bg="lightblue")
    etiquetaValores.pack(pady=5)
    #Actualizar informacion
    def actualizarInformacion():
        etiquetaDinero.config(text=f"Dinero disponible: ${jugadorActual[1][0]:.2f}")
        etiquetaFichas.config(text=f"Fichas disponibles:\n"
            f"Rojas: {jugadorActual[1][1]} | "
            f"Azules: {jugadorActual[1][2]}\n"
            f"Verdes: {jugadorActual[1][3]} | "
            f"Blancas: {jugadorActual[1][4]}")
    actualizarInformacion()
    #Agregar dinero
    def agregarDinero():
        #Solicitar cantidad de dinero
        dinero = simpledialog.askfloat( "Agregar dinero","¿Cuánto dinero desea agregar?", parent=ventana)
        #Comprobar si cancelo
        if dinero is None:
            return
        #Validar cantidad
        if dinero <= 0:
            messagebox.showerror( "Error","Debe ingresar una cantidad mayor a cero",parent=ventana)
            return
        #Confirmar operacion
        confirmar = messagebox.askyesno( "Confirmar",f"¿Desea agregar ${dinero:.2f} a su cuenta?",parent=ventana)
        if confirmar:
            #Sumar dinero al saldo actual
            jugadorActual[1][0] += dinero
            #Guardar cambios
            guardarJugadores(jugadores)
            #Actualizar informacion
            actualizarInformacion()
            messagebox.showinfo("Dinero", "Dinero agregado correctamente", parent=ventana)
    #Campos para ingresar cantidades
    tituloCantidad = tkinter.Label(ventana,
        text="Ingrese la cantidad de fichas:",
        font=("Arial", 13),
        bg="lightblue")
    tituloCantidad.pack(pady=5)
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
                    messagebox.showerror("Error","No puede ingresar cantidades negativas", parent=ventana)
                    return None
                cantidades.append(cantidad)
            except ValueError:
                messagebox.showerror("Error", "Debe ingresar cantidades enteras",parent=ventana)
                return None
        if sum(cantidades) == 0:
            messagebox.showerror("Error", "Debe ingresar al menos una ficha", parent=ventana)
            return None
        return cantidades
    #Limpiar entradas
    def limpiarEntradas():
        for entrada in entradas:
            entrada.delete(0, tkinter.END)
            entrada.insert(0, "0")
    #Comprar fichas
    def comprarFichas():
        cantidades = obtenerCantidades()
        if cantidades is None:
            return
        #Calcular costo de las fichas
        total = 0
        for posicion in range(4):
            total += ( cantidades[posicion] *valoresFichas[colores[posicion]])
        #Comprobar dinero disponible
        if total > jugadorActual[1][0]:
            messagebox.showerror( "Compra","No tiene suficiente dinero", parent=ventana)
            return
        #Confirmar compra
        confirmar = messagebox.askyesno("Confirmar compra", f"Total de la compra: ${total}\n" "¿Desea realizar la compra?",parent=ventana)
        if confirmar:
            #Descontar dinero
            jugadorActual[1][0] -= total
            #Agregar fichas
            for posicion in range(4):
                jugadorActual[1][posicion + 1] += cantidades[posicion]
            #Guardar cambios
            guardarJugadores(jugadores)
            #Actualizar informacion
            actualizarInformacion()
            limpiarEntradas()
            messagebox.showinfo("Compra","Compra realizada correctamente", parent=ventana )
    #Canjear fichas
    def canjearFichas():
        cantidades = obtenerCantidades()
        if cantidades is None:
            return
        #Comprobar fichas disponibles
        for posicion in range(4):
            if cantidades[posicion] > jugadorActual[1][posicion + 1]:
                messagebox.showerror("Canje", f"No tiene suficientes fichas {colores[posicion]}",parent=ventana )
                return
        #Calcular dinero que recibira
        total = 0
        for posicion in range(4):
            total += (cantidades[posicion] *valoresFichas[colores[posicion]] )
        #Confirmar canje
        confirmar = messagebox.askyesno("Confirmar canje", f"Dinero que recibirá: ${total}\n""¿Desea realizar el canje?", parent=ventana )
        if confirmar:
            #Sumar dinero
            jugadorActual[1][0] += total
            #Descontar fichas
            for posicion in range(4):
                jugadorActual[1][posicion + 1] -= cantidades[posicion]
            #Guardar cambios
            guardarJugadores(jugadores)
            #Actualizar informacion
            actualizarInformacion()
            limpiarEntradas()
            messagebox.showinfo("Canje","Canje realizado correctamente",parent=ventana)
    #Boton comprar
    botonComprar = tkinter.Button(ventana,
        text="Comprar fichas",
        font=("Times New Roman", 14),
        command=comprarFichas )
    botonComprar.pack(pady=5)
    #Boton canjear
    botonCanjear = tkinter.Button(ventana,
        text="Canjear fichas",
        font=("Times New Roman", 14),
        command=canjearFichas)
    botonCanjear.pack(pady=5)
    #Boton agregar dinero
    botonAgregarDinero = tkinter.Button(ventana,
        text="Agregar dinero",
        font=("Times New Roman", 14),
        command=agregarDinero)
    botonAgregarDinero.pack(pady=5)
    #Boton volver
    def volverPrincipal():
        ventana.destroy()
        ventanaAnterior.deiconify()
    botonVolver = tkinter.Button(ventana,
        text="Volver al menu principal",
        font=("Times New Roman", 14),
        command=volverPrincipal)
    botonVolver.pack(pady=5)
    #Regresar al menu al cerrar la ventana
    ventana.protocol( "WM_DELETE_WINDOW",volverPrincipal)
