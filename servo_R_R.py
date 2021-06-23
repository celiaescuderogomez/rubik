#https://howtoraspberrypi.com/servo-raspberry-pi/
import RPi.GPIO as GPIO
import time



#1 pin de alimentacion
#6 pin de tierra
pwm_gpio = 11 #pin del servo
frequence = 50 #fecuencia

#Calcula el porcentaje pasando el angulo
def angle_to_percent (angle) :
    start = 4
    end = 12.5
    ratio = (end - start)/180 #Calcul ratio from angle to percent

    angle_as_percent = angle * ratio

    return start + angle_as_percent

#Funciones del servo
def centrar():
    GPIO.setmode(GPIO.BOARD) #Use Board numerotation mode
    GPIO.setwarnings(True) #Disable warnings
    GPIO.setup(pwm_gpio, GPIO.OUT)
    pwm = GPIO.PWM(pwm_gpio, frequence)
    pwm.start(angle_to_percent(72))
    time.sleep(2)
    pwm.stop()
    GPIO.cleanup()

def horario():
    GPIO.setmode(GPIO.BOARD) #Use Board numerotation mode
    GPIO.setwarnings(True) #Disable warnings
    GPIO.setup(pwm_gpio, GPIO.OUT)
    pwm = GPIO.PWM(pwm_gpio, frequence)
    pwm.start(angle_to_percent(180))
    time.sleep(2)
    pwm.stop()
    GPIO.cleanup()

def antiHorario():
    GPIO.setmode(GPIO.BOARD) #Use Board numerotation mode
    GPIO.setwarnings(False) #Disable warnings
    GPIO.setup(pwm_gpio, GPIO.OUT)
    pwm = GPIO.PWM(pwm_gpio, frequence)
    pwm.start(angle_to_percent(-32))
    time.sleep(2)
    pwm.stop()
    GPIO.cleanup()
