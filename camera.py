from picamera import PiCamera
from time import sleep
camera = PiCamera()

def capturarImagen():
    camera.resolution = (500, 500)
    camera.start_preview(alpha=192)
    sleep(1)
    camera.capture("imagen.jpg")
    camera.stop_preview()
