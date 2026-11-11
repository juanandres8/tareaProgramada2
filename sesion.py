#Elaborado por: Fabiana Quesada y Juan Arias
#Fecha de creación: 30/10/2026
#Ultima modificacion:
#Version:3.14.7

#Importaciones
import tkinter
import re
from jugadores import *
from ventanaPrincipal import *
from tkinter import simpledialog, messagebox
#Funciones
def iniciarSesion():
    """
    Funcionalidad:
    Crea y muestra la ventana principal de sesión del casino.
    Entrada:
    - Ninguna.
    Salida:
    - Ninguna: No retorna ningún valor.
    """
    #Ventana de sesión
    ventanaSesion=tkinter.Tk()
    ventanaSesion.title("Casino")
    ventanaSesion.geometry("800x500")
    jugadores=cargarJugadores()#Carga los jugadores registrados
    def abrirRegistro():
        """
        Funcionalidad:
        Abre una ventana secundaria para registrar jugadores.
        Entrada:
        - Ninguna.
        Salida:
        - Ninguna:No retorna ningún valor.
        """
        
        #Ventana de registro
        ventanaRegistro = tkinter.Toplevel(ventanaSesion)# Crea otra ventana
        ventanaRegistro.title("Registro")# Título de la ventana
        ventanaRegistro.geometry("500x400")# Tamaño de la ventana
        #Campo Username
        etiquetaUsername = tkinter.Label(ventanaRegistro,text="Username:",font=("Arial", 12))#Crea etiqueta
        etiquetaUsername.pack(pady=10)
        entradaUsername = tkinter.Entry(ventanaRegistro,font=("Arial", 12))
        entradaUsername.pack(pady=4)
        #Campo Nombre
        etiquetaNombre = tkinter.Label(ventanaRegistro, text="Nombre:", font=("Arial", 12))#Crea etiqueta
        etiquetaNombre.pack(pady=10)
        entradaNombre = tkinter.Entry(ventanaRegistro, font=("Arial", 12))#Crea caja de texto
        entradaNombre.pack(pady=4)#Coloca la caja
        #Campo Apellido
        etiquetaApellido = tkinter.Label(ventanaRegistro, text="Apellido:", font=("Arial", 12))#Crea etiqueta
        etiquetaApellido.pack(pady=10)
        entradaApellido = tkinter.Entry(ventanaRegistro, font=("Arial", 12))#Crea caja de texto
        entradaApellido.pack(pady=4)#Coloca la caja
        #Etiqueta para mensajes de error
        etiquetaMensaje=tkinter.Label(ventanaRegistro, text="",fg="red")#Crea etiqueta
        etiquetaMensaje.pack(pady=10)
        def comprobarRegistro():
            """
            Funcionalidad:
            Valida los datos del jugador, comprueba que el username no exista y guarda su registro en el archivo.
            Entrada:
            - Ninguna.
            Salida:
            - Ninguna: Muestra el resultado del registro.
            """
            username=entradaUsername.get().strip()#Obtiene el username
            nombre=entradaNombre.get().strip()#Obtiene el nombre
            apellido=entradaApellido.get().strip()#Obtiene el apellido
            if username=="":#Comprueba si está vacío
                etiquetaMensaje.config(text="Username inválido", fg="red")
            elif re.match(r"^[a-zA-Z0-9_]+$",username)==None:
                etiquetaMensaje.config(text="Debe ingresar un username sin espacios", fg="red")
            elif nombre=="":
                etiquetaMensaje.config(text="Debe ingresar un nombre", fg="red")
            elif re.match(r"^[a-zA-ZáéíóúÁÉÍÓÚñÑüÜ ]+$",nombre)==None:
                etiquetaMensaje.config(text="Nombre inválido", fg="red")
            elif apellido=="":
                etiquetaMensaje.config(text="Debe ingresar un apellido", fg="red")
            elif re.match(r"^[a-zA-ZáéíóúÁÉÍÓÚñÑüÜ ]+$",apellido)==None:
                etiquetaMensaje.config(text="Apellido inválido", fg="red") 
            else:
                repetido = False#Indica si el username ya existe
                # Busca el username en los jugadores
                for jugador in jugadores:
                    if jugador[0][0]==username:
                        repetido = True
                        break
                if repetido:
                    etiquetaMensaje.config(text="El username ya existe", fg="red")
                else:
                    nuevoJugador =[
                        (username, nombre, apellido),
                        [0.0, 0, 0, 0, 0],0]
                    jugadores.append(nuevoJugador)
                    guardarJugadores(jugadores)#Guarda jugadores 
                    etiquetaMensaje.config(text="Jugador registrado", fg="green")
        botonGuardar = tkinter.Button(ventanaRegistro,text="Guardar registro",font=("Arial", 12),command=comprobarRegistro)
        botonGuardar.pack(pady=10)  # Coloca botón
        # Función para abrir inicio de sesión
    def abrirInicioSesion():
        """
        Funcionalidad:
        Abre una ventana secundaria para iniciar sesión.
        Entrada:
        - Ninguna.
        Salida:
        - Ninguna:No retorna ningún valor.
        """
        
        # Ventana de inicio de sesión
        ventanaInicio = tkinter.Toplevel(ventanaSesion) #Crea ventana secundaria
        ventanaInicio.title("Iniciar sesión")
        ventanaInicio.geometry("800x500")                
        # Campo Username
        etiquetaUsername = tkinter.Label(ventanaInicio, text="Username:", font=("Arial", 12))
        etiquetaUsername.pack(pady=10)
        entradaUsername = tkinter.Entry(ventanaInicio, font=("Arial", 12))
        entradaUsername.pack(pady=4)
        # Etiqueta para mensajes
        etiquetaMensaje = tkinter.Label(ventanaInicio, text="", fg="red")
        etiquetaMensaje.pack(pady=10)
        # Función para comprobar el inicio de sesión
        def comprobarInicioSesion():
            """
            Funcionalidad:
            Valida el username y comprueba si el jugador existe en la lista de jugadores registrados.
            Entrada:
            - Ninguna.
            Salida:
            - Ninguna: Muestra el resultado en la ventana.
            """
            username = entradaUsername.get().strip()  # Obtiene username
            if username == "":
                etiquetaMensaje.config(text="Debe ingresar un username", fg="red")
            elif re.match(r"^[a-zA-Z0-9_]+$", username) == None:
                etiquetaMensaje.config(text="Username inválido", fg="red")
            else:
                existe=False
                for jugador in jugadores:
                    if jugador[0][0]==username:
                        existe=True
                        break
                if existe:
                    #Buscar jugador
                    jugadorActual = None
                    for jugador in jugadores:
                        if jugador[0][0] == username:
                            jugadorActual = jugador
                            break
                    #Consultar dinero solamente si no ha sido registrado
                    if jugadorActual[1][0] == 0.0:
                        dinero = simpledialog.askfloat( "Dinero inicial","¿Cuánto dinero tiene disponible?",parent=ventanaInicio,minvalue=0)
                        #Comprobar si canceló
                        if dinero is None:
                            return
                        #Validar que sea mayor a $5
                        if dinero <= 5:
                            messagebox.showerror("Dinero insuficiente", "Debe ingresar un monto mayor a $5", parent=ventanaInicio)
                            #Regresar a la primera ventana
                            ventanaInicio.destroy()
                            ventanaSesion.deiconify()
                            return
                        #Guardar dinero
                        jugadorActual[1][0] = dinero
                        guardarJugadores(jugadores)
                    #Ingresar al casino
                    etiquetaMensaje.config( text="Inicio de sesión correcto", fg="green")
                    ventanaInicio.destroy()
                    ventanaPrincipal(username)
                else:
                    etiquetaMensaje.config(text="El jugador no existe", fg="red")
        # Botón para ingresar
        botonIngresar = tkinter.Button(ventanaInicio, text="Ingresar", font=("Arial", 12),command=comprobarInicioSesion)
        botonIngresar.pack(pady=5)
        
    #Título
    titulo=tkinter.Label(ventanaSesion,text="Bienvenido al Casino",font=("Arial",28))
    titulo.pack(pady=20)
    #Botón de registro
    botonRegistro = tkinter.Button(ventanaSesion,text="Registrarse",font=("Arial", 16),command=abrirRegistro)#Da formato al texto del boton
    botonRegistro.pack(pady=20)#Coloca el boton
    # Botón de inicio de sesión
    botonInicioSesion = tkinter.Button(ventanaSesion,text="Iniciar sesión",font=("Arial",12),command=abrirInicioSesion)
    botonInicioSesion.pack(pady=10)# Coloca el botón
    ventanaSesion.mainloop()
