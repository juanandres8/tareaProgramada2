'''
Casino -- Tarea programada #2

Tecnológico de Costa Rica

Escuela: Ingeniería en Computación
Curso: Introducción a la Programación
Docente: Ing. Laura Coto Sarmiento
Integrantes:
- Juan Andrés Arias Arias -- Carné 2026014635
- Fabiana Quesada Benavides -- Carné 2025078693

Periodo: Semestre II, 2026
Versión del proyecto:** 3.14.7

------------------------------------------------------------------------

1. Descripción general
- public/tareas-programadas/TP#2_2S_2026_Casino.pdf

El proyecto consiste en desarrollar un casino utilizando Python y la
biblioteca Tkinter para construir la interfaz gráfica. El sistema
permite registrar jugadores, iniciar sesión, administrar dinero y
fichas, participar en distintos juegos y consultar información de los
jugadores.
Los juegos incluidos son:
-   Ruleta.
-   Tragamonedas.
-   Blackjack.
-   Dados.
Además, el sistema permite consultar un ranking de jugadores y generar
un archivo de análisis con sus datos principales.

------------------------------------------------------------------------

2. Repositorio de GitHub

Enlace al repositorio: https://github.com/juanandres8/tareaProgramada2

------------------------------------------------------------------------
3. Organización del proyecto

El programa está dividido en módulos para separar las responsabilidades
y facilitar la comprensión y el mantenimiento del código.
-----------------------------------------------------------------------
  Archivo                           |  Funcionalidad
----------------------------------- -----------------------------------
   casino.py                        |  Punto de entrada. Importa el módulo
                                    |  de sesión y ejecuta
                                    |  iniciarSesion().

   sesion.py                        |  Presenta las ventanas de registro e
                                    |  inicio de sesión. Valida los datos
                                    |  y permite acceder al menú
                                    |  principal.

   ventanaPrincipal.py              |  Muestra el menú principal y las
                                    |  opciones para jugar, administrar
                                    |  fichas, consultar el ranking,
                                    |  generar el análisis y cerrar
                                    |  sesión.

   ventanaJugar.py                  |  Presenta los juegos disponibles y
                                    |  muestra las cantidades de fichas
                                    |  que posee el jugador.

   jugadores.py                     |  Carga y guarda la información de
                                    |  los jugadores utilizando `pickle`.

   fichas.py                        |  Permite agregar dinero, comprar
                                    |  fichas y canjear fichas por dinero.

   ruleta.py                        |  Implementa la ruleta, las apuestas
                                    |  por color o número y la
                                    |  actualización de fichas y puntaje.

   tragamonedas.py                  |  Implementa tres rodillos con
                                    |  símbolos aleatorios y comprueba si
                                    |  los tres coinciden.

   blackJack.py                     |  Implementa el mazo, el reparto de
                                    |  cartas, el cálculo de manos y la
                                    |  determinación del ganador.

   dados.py                         |  Implementa dos dados y las apuestas
                                    |  por suma exacta, par o impar y
                                    |  dobles.

   ranking.py                       |  Ordena los jugadores por puntaje y
                                    |  genera el archivo `ranking.html`.

   analisis.py                      |  Genera el archivo `analisis.csv`
                                    |  con los datos de los jugadores.
  -----------------------------------------------------------------------

4. Estructura de los datos

Cada jugador se almacena mediante una lista con tres componentes:

```
python
[(username, nombre, apellido),[dinero, fichasRojas, fichasAzules, fichasVerdes, fichasBlancas],puntaje]
```
Los datos se consultan mediante posiciones:
  Referencia        Información
  ----------------- ----------------------------
  `jugador[0][0]`   Username
  `jugador[0][1]`   Nombre
  `jugador[0][2]`   Apellido
  `jugador[1][0]`   Dinero disponible
  `jugador[1][1]`   Cantidad de fichas rojas
  `jugador[1][2]`   Cantidad de fichas azules
  `jugador[1][3]`   Cantidad de fichas verdes
  `jugador[1][4]`   Cantidad de fichas blancas
  `jugador[2]`      Puntaje acumulado
4.1. Valores de las fichas
  Color      Valor
  -------- -------
  Roja        \$10
  Azul        \$50
  Verde       \$20
  Blanca      \$5
La liquidez total del jugador se calcula sumando el dinero disponible y
el valor monetario de todas sus fichas.

------------------------------------------------------------------------

5. Funcionamiento de los módulos principales

    5.1. Registro e inicio de sesión

El módulo `sesion.py` presenta la ventana inicial.
Para registrar un jugador solicita username, nombre y apellido.
Comprueba que los campos estén completos, valida el formato de los datos y
verifica que el username no esté registrado previamente.
Para iniciar sesión, el programa solicita el username y comprueba que
corresponda a un jugador existente. Cuando corresponde, también solicita
el dinero inicial del jugador.

    5.2. Menú principal y menú de juegos

ventanaPrincipal.py muestra el nombre del jugador y las opciones
principales del casino.
Desde allí se puede abrir el menú de juegos, administrar fichas,
generar el ranking, generar el análisis o cerrar sesión.
ventanaJugar.py muestra los accesos a Ruleta, Tragamonedas, Blackjack y Dados.
También consulta la información guardada para mostrar
las cantidades de fichas rojas, azules, verdes y blancas del jugador.

    5.3. Administración de fichas

El módulo fichas.py permite agregar dinero, comprar fichas y canjearlas por dinero.
Para comprar, calcula el costo de las cantidades
solicitadas y comprueba que el saldo sea suficiente.
Para canjear,comprueba que el jugador tenga las fichas solicitadas y calcula el
dinero que recibirá.

    5.4. Ruleta

El módulo ruleta.py crea 37 casillas, numeradas del 0 al 36.
El cero es verde; los números pares se clasifican como negros y los impares como rojos.
El resultado se selecciona aleatoriamente.
El jugador puede apostar por un color o por un número.
Después del resultado, el programa comprueba la apuesta y actualiza las fichas y el puntaje.

    5.5. Tragamonedas

El módulo tragamonedas.py utiliza tres rodillos y cinco símbolos
posibles: cereza, limón, uvas, rayo y estrella.
Cada rodillo selecciona un símbolo aleatorio.
El jugador gana cuando los tres símbolos son iguales.
El programa descuenta las fichas apostadas y aplica el premio y
los puntos según el resultado.

    5.6. Blackjack

El módulo blackJack.py crea un mazo de 52 cartas con cuatro palos.
Baraja las cartas y reparte dos al jugador y dos al crupier.
Calcula el valor de cada mano y contempla que el As pueda valer 1 u 11.
El jugador puede pedir otra carta o plantarse.
El crupier solicita cartas mientras su mano tenga 16 puntos o menos.
Al finalizar, se comparan las manos para determinar el resultado.

    5.7. Dados

El módulo dados.py genera dos números aleatorios entre 1 y 6 y
devuelve ambos valores en una tupla.
El jugador puede seleccionar una deestas apuestas:
-   Suma exacta: pronosticar un total entre 2 y 12.
-   Par o impar: indicar si la suma de los dados será par o impar.
-   Dobles: pronosticar que ambos dados tendrán el mismo valor.
El módulo valida el pronóstico según el tipo de apuesta, comprueba las
cantidades de fichas y actualiza los datos del jugador después del
lanzamiento.

    5.8. Ranking y análisis

El módulo ranking.py ordena a los jugadores de mayor a menor puntaje
mediante un algoritmo de ordenamiento por inserción y genera ranking.html.
La tabla presenta username, puntaje y liquidez total.
El módulo analisis.py genera analisis.csv, que contiene nombre,
apellido, username, puntaje y liquidez total de cada jugador.

------------------------------------------------------------------------

6. Almacenamiento de información y archivos generados

El módulo jugadores.py utiliza pickle para guardar y recuperar la
lista de jugadores en un archivo binario llamado jugadores.
-   cargarJugadores() abre el archivo y recupera los registros. Si el
    archivo no existe, devuelve una lista vacía.
-   guardarJugadores(jugadores) guarda la lista actualizada.
El proyecto genera además:
-   ranking.html: archivo que permite visualizar el ranking en un
    navegador.
-   analisis.csv: archivo con información de los jugadores que puede
    abrirse en un programa de hojas de cálculo.

------------------------------------------------------------------------

7. Validaciones implementadas

Se incorporan validaciones para evitar que el programa continúe con
datos incorrectos o transacciones que el jugador no puede realizar.

    7.1. Registro e inicio de sesión
-   Se comprueba que los campos requeridos no estén vacíos.
-   El username debe contener letras, números o guion bajo, sin
    espacios.
-   El nombre y el apellido deben contener caracteres permitidos para
    nombres.
-   Se evita registrar usernames repetidos.
-   Se comprueba que el username exista al iniciar sesión.

    7.2. Administración de fichas
-   Las cantidades ingresadas deben ser números enteros.
-   No se permiten cantidades negativas.
-   Se requiere ingresar al menos una ficha para comprar o canjear.
-   Se comprueba que el jugador tenga dinero suficiente para comprar.
-   Se comprueba que tenga suficientes fichas para canjear.
-   Se solicita confirmación antes de completar las operaciones.

    7.3. Juegos
-   Se validan los tipos de apuesta permitidos.
-   Las cantidades apostadas deben ser enteras y no negativas.
-   Se comprueba que las cantidades no superen las fichas disponibles.
-   Se evita realizar apuestas sin fichas.
-   En la ruleta, se valida que el color o número seleccionado
    pertenezca a las opciones permitidas.
-   En Dados, la suma exacta debe ser un entero entre 2 y 12; para par o
    impar se acepta el texto correspondiente; para dobles, la casilla de
    pronóstico debe quedar vacía.

------------------------------------------------------------------------

8. Decisiones tomadas durante el desarrollo

Las siguientes decisiones se reflejan en la estructura y el
funcionamiento de los archivos entregados:

1.  **Separación por módulos:** se dividió el programa en archivos
    independientes para separar la sesión, los menús, la administración
    de fichas, los juegos y los reportes.
2.  **Uso de Tkinter:** se eligió esta biblioteca para construir las
    ventanas, botones, etiquetas y campos de entrada de la aplicación.
3.  **Estructura común para jugadores:** se utiliza una misma estructura
    de lista para almacenar los datos personales, el dinero, las fichas
    y el puntaje. Esto permite que los módulos trabajen con la misma
    información.
4.  **Persistencia con `pickle`:** se utiliza un archivo binario para
    conservar los registros y los cambios de los jugadores entre
    ejecuciones.
5.  **Funciones para los procesos de los juegos:** se separaron tareas
    como generar resultados, comprobar apuestas y actualizar fichas o
    puntajes para facilitar las pruebas y la reutilización.
6.  **Validación según el tipo de entrada:** cada campo se valida de
    acuerdo con lo que debe recibir. Por ejemplo, en Dados la suma
    exacta requiere un entero, mientras que par o impar requiere texto.
7.  **Generación de reportes externos:** se decidió producir un ranking
    HTML y un análisis CSV para consultar la información fuera de la
    interfaz del casino.

------------------------------------------------------------------------

9. Pruebas realizadas y aspectos por verificar

Durante las pruebas del proyecto se revisaron los procesos de registro e
inicio de sesión, la navegación entre ventanas, la administración de
fichas, las apuestas de los juegos y la actualización de la información
del jugador.
También se ajustaron elementos de la interfaz para mejorar la
visualización de las opciones y de las fichas disponibles.
Revisión de la versión final del repositorio:
-   Todos los módulos están incluidos y tienen los mismos nombres
    utilizados en las importaciones.
-   Las ventanas abren y regresan correctamente al menú
    correspondiente.
-   Las fichas y el puntaje se actualizan y permanecen guardados
    después de cerrar el programa.
-   Se comprueban las opciones válidas e inválidas de cada tipo de
    apuesta.
-   `ranking.html` y `analisis.csv` se generan correctamente.
-   Al repositorio de GitHub contenie la versión final del código y
    el presente README.

------------------------------------------------------------------------
    
10. Colaboración de los participantes

El proyecto fue desarrollado por Juan Andrés Arias Arias(Estudiante 1) y Fabiana
Quesada Benavides(Estudiante 2). 


------------------------------------------------------------------------
'''









