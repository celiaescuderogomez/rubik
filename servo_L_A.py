#https://howtoraspberrypi.com/servo-raspberry-pi/
import RPi.GPIO as GPIO
import time


#17 pin de alimentacion
#14 pin de tierra
pwm_gpio = 7 #pin del servo
frequence = 50 #fecuencia

def cleanServo():
    pwm.stop()
    GPIO.cleanup()

#Calcula el porcentaje pasando el angulo
def angle_to_percent (angle) :
    start = 4
    end = 12.5
    ratio = (end - start)/180 #Calcul ratio from angle to percent

    angle_as_percent = angle * ratio

    return start + angle_as_percent


#Funciones del servo
def abrir():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)
    GPIO.setup(pwm_gpio, GPIO.OUT)
    pwm = GPIO.PWM(pwm_gpio, frequence)
    pwm.start(angle_to_percent(5))
    time.sleep(2)
    pwm.stop()
    GPIO.cleanup()

def cerrar():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)
    GPIO.setup(pwm_gpio, GPIO.OUT)
    pwm = GPIO.PWM(pwm_gpio, frequence)
    pwm.start(angle_to_percent(55))
    time.sleep(2)
    pwm.stop()
    GPIO.cleanup()
