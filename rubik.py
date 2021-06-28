#Comentar las dos lineas de codigo en el siguiente fichero
#/home/pi/.local/lib/python2.7/site-packages/rubik_solver/Solver/Kociemba/Search.py
#if time.time() - tStart > timeOut:
#raise SolverTimeoutError("Timeout, no solution within given time")
from rubik_solver import utils
import moves as moves
import detectcolor as detectcolor
import camera as camera

cube = ''

##Capturamos UP Descomentar en caso de querer meter los colores manualmente
print("Cara UP: Capturando imagen...")
camera.capturarImagen()
print("Cara UP: Analizando colores...")
caraUP = detectcolor.detectarColores()
caraUP ="bbygyyrry"
print("Cara UP: " + caraUP)
respuestaCaraUP = input("Son correctos estos colores?(y/n) ")
if respuestaCaraUP == 'y':
    cube = cube + caraUP
else:
    caraUP = input("Por favor escribe los colores correctos: ")
    cube = cube + caraUP

#Movemos a LEFT
moves.moveToLeft(True)

#Capturamos LEFT
print("Cara LEFT: Capturando imagen...")
camera.capturarImagen()
print("Cara LEFT: Analizando colores...")
caraLEFT = detectcolor.detectarColores()
caraLEFT = "oobwbwwwr"
print("Cara LEFT: " + caraLEFT)
respuestaCaraLEFT = input("Son correctos estos colores?(y/n) ")
if respuestaCaraLEFT == 'y':
    cube = cube + caraLEFT
else:
    caraLEFT = input("Por favor escribe los colores correctos: ")
    cube = cube + caraLEFT

#Movemos a la posicion original
moves.moveToLeft(False)

#movemos a FRONT
moves.moveToFront(True)

#Capturamos FRONT
print("Cara FRONT: Capturando imagen...")
camera.capturarImagen()
print("Cara FRONT: Analizando colores...")
caraFRONT = detectcolor.detectarColores()
caraFRONT = "wbrgrybbw"
print("Cara FRONT: " + caraFRONT)
respuestaCaraFRONT = input("Son correctos estos colores?(y/n) ")
if respuestaCaraFRONT == 'y':
    cube = cube + caraFRONT
else:
    caraFRONT = input("Por favor escribe los colores correctos: ")
    cube = cube + caraFRONT

#movemos a la posicion original
moves.moveToFront(False)

#movemos a RIGHT
moves.moveToRight(True)

#capturamos RIGHT
print("Cara RIGHT: Capturando imagen...")
camera.capturarImagen()
print("Cara RIGHT: Analizando colores...")
caraRIGHT = detectcolor.detectarColores()
caraRIGHT = "gogrgwggr"
print("Cara RIGHT: " + caraRIGHT)
respuestaCaraRIGHT = input("Son correctos estos colores?(y/n) ")
if respuestaCaraRIGHT == 'y':
    cube = cube + caraRIGHT
else:
    caraRIGHT = input("Por favor escribe los colores correctos: ")
    cube = cube + caraRIGHT

#movemos a la posicion original
moves.moveToRight(False)

#movemos a BACK
moves.moveToBack(True)

#capturamos BACK
print("Cara BACK: Capturando imagen...")
camera.capturarImagen()
print("Cara BACK: Analizando colores...")
caraBACK = detectcolor.detectarColores()
caraBACK = "ooyoorggb"
print("Cara BACK: " + caraBACK)
respuestaCaraBACK = input("Son correctos estos colores?(y/n) ")
if respuestaCaraBACK == 'y':
    cube = cube + caraBACK
else:
    caraBACK = input("Por favor escribe los colores correctos: ")
    cube = cube + caraBACK

#movemos a la posicion original
moves.moveToBack(False)

#movemos a DOWN
moves.moveToDown(True)

#capturamos DOWN
print("Cara DOWN: Capturando imagen...")
camera.capturarImagen()
print("Cara DOWN: Analizando colores...")
caraDOWN = detectcolor.detectarColores()
caraDOWN = "wroywboyy"
print("Cara DOWN: " + caraDOWN)
respuestaCaraDOWN = input("Son correctos estos colores?(y/n) ")
if respuestaCaraDOWN == 'y':
    cube = cube + caraDOWN
else:
    caraDOWN = input("Por favor escribe los colores correctos: ")
    cube = cube + caraDOWN

#movemos a la posicion original
moves.moveToDown(False)

#Descomentar en caso de querer meter los colores manualmente
cube = "oybwybgwrybwrbgwwroogwrygooyyoggoggbwrbgobybrwyyrwrbor"
print("Cubo entero: " + cube)
print("Numero de colores: "+ str(len(cube)))
print("Calculando movimientos por favor espere...")
movimientos = utils.solve(cube, 'Kociemba')
print(movimientos)
print("Numero de movimientos: "+ str(len(movimientos)))
input("Pulsa una tecla para confirmar")

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

for movimiento in movimientos:
    movString = str(movimiento)
    try:
        if movString.find("2") == -1:
           equivalencias(movString)(90)
        else:
           movString = movString.replace("2","")
           equivalencias(movString)(180)

    except:
        print(str(movimiento) +" Equivalencia no encontrada")
