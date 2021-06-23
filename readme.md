# Documentación Rubik Solver
Rubik solver es un proyecto de programación en python desarrollado para resolver el  cubo de rubik con una Raspberry y 4 servos.

## Introducción
Cuando se planteó el desarrollo del codigo se estudiaron diversos proyectos ya existentes, la mayoria desarrollados en C. 

Para este proyecto se ha utilizado Python ya que posee la ventaja de tener multitud de librerias las cuales han facilitado enormemente el trabajo
además de ser un lenguaje sencillo de aprender.

Las librerias externas utilizadas son:
* [PiCamera](https://picamera.readthedocs.io/en/release-1.13/) para controlar la camara
* [OpenCV](https://pypi.org/project/opencv-python/) para aislar los colores por separado y procesarlos
* [Webcolors](https://pypi.org/project/webcolors/) para traducir los colores hexadecimales detectados por OpenCV
* [Rubik_Solver](https://pypi.org/project/rubik-solver/) esta es la libreria mas importante, traduce los colores analizados por una matriz de movimientos para resolver el cubo de rubik

Más adelante se explicará más en profundidad dichas librerias.

## Estructura de ficheros
Se ha estructurado el codigo de la forma mas modular y clara posible, dicha estructura es la siguiente:
* camera.py, contiene las funciones de nuestra camara
* detectcolors.py contiene las funciones para analizar la imagen capturada por la camara
* moves.py en este fichero se encuentran las funciones para replicar los movimientos que hariamos con las manos
* servo_L_A.py controlador para el servo izquierdo de apertura de pinzas
* servo_L_R.py controlador para el servo izquierdo que rota la pinza
* servo_R_A.py controlador para el servo derecho de apertura de pinzas
* servo_R_R.py controlador para el servo derecho que rota la pinza
* rubik.py fichero principal, este es el fichero que ejecutamos para que se realice todo el proceso

## Analisis del codigo
Para explicar todo el codigo seguirmos el siguiente diagrama de flujo:
(introducir imagen del diagrama)

Todo este proceso se ve reflejado en el fichero rubik.py el cual es el que se tiene que ejecutar 
para el funcionamiento del programa.

### Captura de colores y traducción a texto
La primera parte de codigo consiste en capturar las 6 caras del cubo y traducirlo a una cadena de caracteres que la libreria rubik_solver
pueda interpretar, rubik_solver permite varios algoritmos de resolución pero el mas rapido es Kociemba, por desgracia para que este algoritmo funcione
tenemos que colocar el cubo de rubik en la siguiente posición:  
U centro: AMARILLO  
L centro: AZUL  
F centro: ROJO  
R centro: VERDE  
B centro: NARANJA  
D centro: BLANCO  
Una vez tenemos el cubo en la posición correcta seguiremos el siguiente bucle para analizar todos los colores:

Se mueve la cara que se quiere analizar a UP -> Captura de imagen -> Analisis de colores -> Concatenar con el resto de caras en un String -> Repetimos el proceso con el resto de caras

Durante este proceso se han creado 4 funciones en el fichero moves.py para ir rotando el cubo y asi analizar las caras (moveToLeft, moveToFront, moveToRight, moveToBack, moveToDown) 
a dichas funciones se le pasa un Bool para indicarle si se quiere ir a esa cara o se quiere revertir el proceso para dejar el cubo en su posición original.

#### Captura de imagen
El proceso de captura de imagen es bastante sencillo, al haber utilizado la camara oficial de raspberry la documentación y el codigo son muy claros.

La función capturarImagen declarada en el fichero camera.py realiza una imagen con las dimensiones 500x500
y la guarda en la raiz del proyecto.

#### Analisis de colores
Cuando la imagen ha sido realizada necesitamos aislar los colores y analizarlos, las funciones que se van 
a nombrar a continuación estan declaradas en el fichero detectcolors.py pero nosotros solamente vamos a llamar desde rubik.py
a la función detectarColores. 

La libreria openCV crea una variable con la imagen de la cara, a continuación se declara
una matriz con las coordenadas donde openCV encontrá cada uno de los colores, 
en este punto se ha comentido una confusión logica ya que no se tuvo en cuenta que el cubo estaba
en posicion horizontal y no en vertical por tanto las primeras pruebas daban resultados erroneos ya que
la matriz de colores estaba mal:

    # Posición incorrecta de los colores
    # ----------------
    # | 0  | 1  | 2  |
    # ----------------
    # | 3  | 4  | 5  |
    # ----------------
    # | 6  | 7  | 8  |
    # ----------------
    
    # Posición correcta de los colores
    # ----------------
    # | 6  | 3  | 0 |
    # ----------------
    # | 7  | 4  | 1  |
    # ----------------
    # | 8  | 5  | 2  |
    # ----------------

Una vez solucionado el problema se declará un bucle para analizar las 6 caras una por una. 

Gracias a openCV y numpy (una libreria de python para vectores y matrices) se puede analizar los
colores de una imagen aislando los colores en rojo verde y azul formando un RGB para luego parasarlo a 
hexadecimal y para que así webcolors pueda traducirlo a un color alfabetico.

El problema de webcolors es que no devuelve un color absoluto, como su nombre indica posee todos
los colores usados en desarrollo web, para traducir estos colores a simplemente los 6 del cubo de rubik
se ha anallizado el codigo de la libreria y se creado una matriz de equivalencias con los colores web y los colores 
Rojo, Amarillo, Verde, Blanco, Naranja y Azul.

Finalmente devolvemos a rubik.py un String con los colores de nuestra cara.

#### Comprobación de seguridad
El analisis de color tiene un porcentaje de fallo en ciertos colores dependiendo de la iluminación de la habitación, esto puede desencadenar en que falle todo el codigo, debido a esto se ha realizado una comprobación manual por parte del usuario al final del analisis de cada cara, el usuario puede comprobar si el string de colores es correcto, si no puede escribirlo manualente en el terminal y pulsar intro para continuar en lugar de tener que volver a empezar de nuevo.

El aspecto final del String de colores seria mas o menos el siguiente:
```
rbbwyorwgybbrbwwbgwgoorywyoygygggboroygrowbrorowrwbgyy
```

### Resolución de movimientos con Rubik_solver
Esta es seguranente la parte más importante y donde mas tiempo se ha ahorrado gracias
a la libreria de [Rubik_Solver](https://pypi.org/project/rubik-solver/).

Su uso consiste en una función a la cual le pasamos dos parametros, los colores
del cubo de rubik en el orden correcto y el algoritmo que queremos usar, en este caso Kociemba.

En este punto el codigo se desarrolló sobre un ordenador portatil el cual tiene mucha mas potencia que una Raspberry, al trasladar dicho codigo a una Raspberry el codigo de rubik_solver funcionaba mucho mas lento, como resultado cortaba el proceso porque detectaba que no habia encontrado una solución, para solucionar este problema se ha tenido que modificar la misma libreria para parchear esta parte y que no corte el proceso, de esta forma aunque tarde unos segundos en devolver la matriz de movimientos funciona correctamente.

### Resultado final
Para terminar el proceso debemos analizar cada movimiento devuelto por rubik_solver y ejecutar una función equivalente a cada movimiento declarada en moves.py,
es decir si necesitamos hacer R, ejecutamos moves.moveRight, si necesitamos hacer F, ejecutamos moves.moveFront, todos los movimientos de rubik_solver pertenecen a las anotaciones estandar de rubik ([Más info](http://www.rubiksplace.com/move-notations/)).

En lugar de hacer un if por cada movimiento se ha declarado una función de equivalencias para cada función:
```
def equivalencias(case):
    return {"R": moves.moveRight,
            "L": moves.moveLeft,
            "U": moves.moveTop,
            "D": moves.moveDown,
            "F": moves.moveFront,
            "B": moves.moveBack,
            "R'": moves.moveRightR,
            "L'": moves.moveLeftR,
            "U'": moves.moveTopR,
            "D'": moves.moveDownR,
            "F'": moves.moveFrontR,
            "B'": moves.moveBackR}.get(case)
```
Dichas funciones reciben un parametro numero (90 o 180) dependiendo de los grados que queramos mover la cara.

### Movimientos de pinzas
Las pinzas al final se mueven gracias a 2 servos por cada pinza, aunque ambos servos son similares y la logica del codigo es la misma, no tienen las mismas funciones.

Los servos de apertura (servo_L_A.py y servo_R_A.py) contienen las funciones
de abrir y cerrar las pinzas, el codigo es similar y solo cambia los grados que queremos rotar el servo:
```
    GPIO.setmode(GPIO.BOARD) # Indicamos el modo
    GPIO.setwarnings(False) # Deshabilitamos los warnings
    GPIO.setup(pwm_gpio, GPIO.OUT) # Indicamos el ping del servo declarado anteriormente
    pwm = GPIO.PWM(pwm_gpio, frequence) # Indicamos la frecuencia, en este caso 60
    pwm.start(angle_to_percent(50)) # Indicamos el angulo al que queremos mover ek servo
    time.sleep(2) # Esperamos a que termine
    pwm.stop() # Detenemos el proceso
    GPIO.cleanup() # Limpiamos el GPIO para que no entre en conflicto cuando se vuelva a utilizar
```
Como hemos podido observar la función que indica los grados es angle_to_percent, esto se debe a que una señal de 0.5ms corresponde a 0 ° y una señal de 2.5ms a 180 °. Sabiendo que nuestro ciclo es de 20 ms, esto nos permite calcular el ciclo de trabajo para 0 ° y 180 ° así:
```
x = 0.5 / 20
y = 2.5 / 20
```
Luego encontramos que el ciclo de trabajo correspondiente a 0 ° es 0.025, o 2.5% y que el correspondiente a 180 ° es 0.125, o 12.5%. ([Fuente](https://raspberrypi-espana.es/servo-frambuesa-pi/))

```
def angle_to_percent (angle) :
    start = 4
    end = 12.5
    ratio = (end - start)/180 #Calcul ratio from angle to percent

    angle_as_percent = angle * ratio

    return start + angle_as_percent
```

Por otro lador los servos de rotación (servo_R_R.py y servo_L_R.py) contienen las funciones horario, antiHorario, y centrar,
estas tres funciones, como su nombre indica, rotan las pinzas de forma precisa, dado que los servos son similares a los de apertura 
su codigo es el mismo y solo cambia los grados en cada función.