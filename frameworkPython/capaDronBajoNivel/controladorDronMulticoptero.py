_autor_= "I.C.C."

from hal.actuadorOpenPilot import ActuadorOpenPilot
from hal.sensorGPS import SensorGPS
from hal.sensorGiroscopio import SensorGiroscopio
from hal.sensorUltrasonido import SensorUltrasonido
from hal.sensorMagnetometro import SensorMagnetometro
from hal.sensorBateria import SensorBateria

from controladorDronVolador import ControladorDronVolador

class ControladorDronMulticoptero(ControladorDronVolador):

    def __init__(self):
        self.actuadorOP= ActuadorOpenPilot()
        self.sensorGPS=SensorGPS()
        self.sensorGiroscopio=SensorGiroscopio()
        self.sensorUltrasonido = SensorUltrasonido()
        self.sensorMagnetometro = SensorMagnetometro()
        self.sensorBateria= SensorBateria()
        self.altitudSuelo=self.sensorGPS.getLastInfo().getData()['altitud']
        self.alcanceUltrasonido=self.sensorUltrasonido.

    # encender equivale a decir armar motores en OP
    def encender(self):
        self.actuadorOP.encender()

    def apagar(self):
        self.actuadorOP.apagar()

    # giro lateral de la cabeza desde la pocisión donde esta
    def yaw(self, grados):
        # si es absoluto
        giro1=50+(100-50)*grados/180

        #si es en relacion para ir a la izquierda grados debe estar en negativo
        giro2= self.actuadorOP.getYaw()+ (100-50)*grados/180
        self.actuadorOP.setYaw(giro2)

    # giro lateral de la cabeza a la izquierda desde la posicion donde esta
    def yaw_izquierda(self, giro):
        giro=grados*360/100
        self.actuadorOP.setYaw(giro)

    # giro lateral de la cabeza a la derecha desde la pocisión donde esta
    def yaw_derecha(self, grados):
        velocidad=grados*360/100
        self.actuadorOP.setYaw(velocidad)

    # elevar el dron  distancia estará a
    def up(self, distancia):
        # el throtle es la velocidad de los motores
        distancia1=distancia
        self.actuadorOP.setThrotle(distancia1)

    # bajar el dron distancia
    def down(self, distancia):
        distancia1=distancia
        self.actuadorOP.setThrotle(distancia1)

    # cabeceo - elevacion de la cabeza
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

    # devuelve el angulo de la cabeza del dron  del 0 al 360 donde el 0 es el norte
    def getAnguloCabeza(self):
        return self.sensorMagnetometro.getAnguloCabezaDron()

    # me da la distancia del dron al suelo
    def getDistancaSuelo(self):
        return self.sensorUltrasonido.getAltura()

    # devuelve x y z (longitud, latitud y altura al suelo) como una tupla
    def getCoordenadas(self):
        xyz=self.sensorGPS.getCoordenadas()
        x=xy['latitud']
        y=xy['longitud']
        z=xy['altitud']
        return (x,y,z)

    # avanza el dron
    def irAdelante(self, velocidad):

        actuadorOP.irAdelante(velocidad)



