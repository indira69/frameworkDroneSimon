_autor_= "I.C.C."

from hal.actuadorOpenPilot import ActuadorOpenPilot
from hal.sensorGPS import SensorGPS
from hal.sensorGiroscopio import SensorGiroscopio
from hal.sensorUltrasonido import SensorUltrasonido
from hal.sensorMagnometro import SensorMagnometro
from hal.sensorBateria import SensorBateria

from hal.sensorGPS import SensorGPS

class ControladorDronMulticoptero(object):

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
