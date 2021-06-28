import time
import moves as moves
import servo_R_A as servo_R_A
import servo_R_R as servo_R_R
import servo_L_A as servo_L_A
import servo_L_R as servo_L_R

servo_L_A.abrir()

servo_R_A.abrir()

servo_R_A.cerrar()

servo_L_A.cerrar()
servo_R_R.horario()
servo_R_R.antiHorario()
servo_R_R.centrar()
servo_L_R.horario()
servo_L_R.antiHorario()

servo_L_R.centrar()