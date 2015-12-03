_autor_= "I.C.C."

from hal.actuadorOpenPilot import ActuadorOpenPilot
from hal.sensorGPS import SensorGPS
from hal.sensorGiroscopio import SensorGiroscopio
from hal.sensorUltrasonido import SensorUltrasonido
from hal.sensorMagnometro import SensorMagnometro
from hal.sensorBateria import SensorBateria

from controladorDronVolador import ControladorDronVolador

class ControladorDronMulticoptero(ControladorDronVolador):

    def __init__(self):
        self.actuadorOP= ActuadorOpenPilot()
        self.sensorGPS=SensorGPS()
        self.sensorGiroscopio=SensorGiroscopio()
        self.sensorUltrasonido = SensorUltrasonido()
        self.sensorMagnometro = SensorMagnometro()
        self.sensorBateria= SensorBateria()

    # encender equivale a decir armar motores en OP
    def encender(self):
        self.actuadorOP.encender()

    def apagar(self):
        self.actuadorOP.apagar()

    # giro lateral de la cabeza
    def yaw(self, grados):
        velocidad= grados*360/100
        self.actuadorOP.setYaw(velocidad)

    # giro lateral de la cabeza a la izquierda
    def yaw_izquierda(self, grados):
        velocidad=grados*360/100
        self.actuadorOP.setYaw(velocidad)


    # giro lateral de la cabeza a la derecha
    def yaw_derecha(self, grados):
        velocidad=grados*360/100
        self.actuadorOP.setYaw(velocidad)


    # elevar el dron  distancia estará a
    def up(self, distancia):
        distancia1=distancia*????
        self.actuadorOP.setThrotle(distancia1)

    # bajar el dron distancia
    def down(self, distancia):
        distancia1=distancia*?????
        self.actuadorOP.setThrotle(distancia1)

    # cabeceo - elevación de la cabeza
    def pitch_arriba(self, grados):
        velocidad=grados*360/100
        self.actuadorOP.setPitch(velocidad)

    # cabeceo - bajar la cabeza
    def pitch_abajo(self, grados):
        velocidad=grados*360/100
        self.actuadorOP.setPitch(velocidad)

    # giro lateral de costado a la derecha
    def roll_derecha(self, grados):
        velocidad=grados*360/100
        self.actuadorOP.setRoll(velocidad)

    # giro lateral de costado a la izquierda
    def roll_izquierda(self, grados):
        velocidad=grados*360/100
        self.actuadorOP.setRoll(velocidad)
