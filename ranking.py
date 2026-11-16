#Elaborado por: Fabiana Quesada y Juan Arias
#Fecha de creación: 15/11/2026
#Ultima modificacion:
#Version:3.14.7

#Importaciones
from jugadores import *
import tkinter
#Funciones
def generarRanking():
    """
    Funcionalidad:
    Obtiene la lista de jugadores registrados
    para generar el ranking del casino.
    Entrada:
    - Ninguna.
    Salida:
    - Ninguna.
    """
    jugadores=cargarJugadores()
    #Ordenar los jugadores por puntaje de mayor a menor
    for i in range(1, len(jugadores)):
        actual=jugadores[i]
        j = i - 1
        while j>=0 and jugadores[j][2]<actual[2]:
            jugadores[j+1]=jugadores[j]
            j-=1
        jugadores[j+1]=actual
    #Crea el archivo HTML del ranking
    archivo=open("ranking.html", "w",encoding="utf-8")
    archivo.write("<html>\n")
    archivo.write("<head><title>Ranking del Casino</title></head>\n")
    archivo.write("<body style='text-align: center;'>\n")
    archivo.write("<h1>Ranking de jugadores</h1>\n")
    #Crea la tabla
    archivo.write("<table border='1' style='margin: auto;'>\n")
    archivo.write("<tr><th>Username</th><th>Puntaje</th><th>Liquidez total</th></tr>\n")
    numeroFila=0
    #Agregar los jugadores a la tabla
    for jugador in jugadores:
        username=jugador[0][0]
        puntaje=jugador[2]
        liquidez=(jugador[1][0]+jugador[1][1]*10+jugador[1][2]*50+jugador[1][3]*20+jugador[1][4]*5)
        if numeroFila%2==0:
            color="lightblue"
        else:
            color="white"
        archivo.write(f"<tr style='background-color: {color};'>"f"<td>{username}</td>"f"<td>{puntaje}</td>"
                      f"<td>{liquidez}</td></tr>\n")
        numeroFila += 1
    archivo.write("</table>\n")
    archivo.write("</body>\n")
    archivo.write("</html>\n")
    archivo.close()
def ventanaRanking(ventanaAnterior):
    """
    Funcionalidad:
    Muestra una ventana para confirmar la
    generación del ranking de jugadores.
    Entrada:
    - ventanaAnterior:Ventana principal del casino.
    Salida:
    - Ninguna.
    """
    ventana=tkinter.Toplevel(ventanaAnterior)
    ventana.title("Generar Ranking")
    ventana.geometry("350x200")
    texto=tkinter.Label(ventana,text="¿Desea generar el ranking de jugadores?")
    texto.pack(pady=20)
    def confirmar():
        """
        Funcionalidad:
        Genera el archivo HTML y muestra
        un mensaje de confirmación.
        Entrada:
        - Ninguna.
        Salida:
        - Ninguna.
        """
        generarRanking()
        texto.config(text="Ranking generado correctamente")
        botonConfirmar.config(state="disabled")
    botonConfirmar=tkinter.Button(ventana,text="Confirmar",command=confirmar)
    botonConfirmar.pack(pady=5)
    botonCancelar=tkinter.Button(ventana,text="Cerrar",command=ventana.destroy)
    botonCancelar.pack(pady=5)
