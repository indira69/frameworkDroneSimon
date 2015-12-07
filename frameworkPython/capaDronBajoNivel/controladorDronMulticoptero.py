_autor_= "I.C.C."

import time
from hal.actuadorOpenPilot import ActuadorOpenPilot
from hal.sensorGPS import SensorGPS
from hal.sensorGiroscopio import SensorGiroscopio
from hal.sensorUltrasonido import SensorUltrasonido
from hal.sensorMagnetometro import SensorMagnetometro
from hal.sensorBateria import SensorBateria

from drivers.driverGPS import DriverGPS
from drivers.driverMagnetometro import DriverMagnetometro
from drivers.driverUltrasonido import DriverUltrasonido

# falta driver de nivel de bateria y de giroscopio


from controladorDronVolador import ControladorDronVolador

class ControladorDronMulticoptero(ControladorDronVolador):

    def __init__(self):
        self.actuadorOP= ActuadorOpenPilot()
        self.sensorGPS=SensorGPS(DriverGPS())
        self.sensorGiroscopio=SensorGiroscopio(DriverGiroscopio())
        self.alcanceUltrasonido=4000
        self.sensorUltrasonido = SensorUltrasonido(DriverUltrasonido(),alcanceUltrasonido)
        self.sensorMagnetometro = SensorMagnetometro(DriverMagnetometro())
        self.sensorBateria= SensorBateria()

        # convierto la info del GPS a centimetros porque viene en metros
        self.altitudSuelo=self.sensorGPS.getLastInfo().getData()['altitud']*100
        self.alcanceUltrasonido=self.sensorUltrasonido.getAlcance()
        self.velocidadMaxGiroOP=50
        self.velocidadCeroGiroOP=50

        self.velocidadEstable=70
        self.velocidad10cm=30
        self.velocidad5cm=20
        self.velocidadMaxMotores=100
        self.distanciaMinimaDelSuelo=30  # 30 centimetros

    # encender equivale a decir armar motores en OP
    def encender(self):
        self.actuadorOP.encender()

    def setAltitudSuelo(self):
        self.altitudSuelo=self.sensorGPS.getLastInfo().getData()['altitud']

    def apagar(self):
        self.actuadorOP.apagar()

    # giro lateral de la cabeza desde la pocisión donde esta
    # velocidad es un entero de 1 al 50, no puede ser 0
    # si grados es negativo ira a la izquierda
    def yaw(self, grados, velocidad):
        # si es absoluto
        # giro1=50+(100-50)*grados/180

        #si es en relacion para ir a la izquierda grados debe estar en negativo
        #giro2= self.actuadorOP.getYaw()+ (100-50)*grados/180
        #self.actuadorOP.setYaw(giro2)

        anguloInicial=self.sensorMagnetometro.getAnguloCabezaDron()
        gradosAlcanzados=0

        direccion=1
        if (grados<0):
            direccion=-1

        grados=abs(grados)
        self.actuadorOP.setYaw(self.velocidadCeroGiroOP + velocidad*direccion)
        while (gradosAlcanzados<grados & velocidad>=1):
            gradosAlcanzados=abs(anguloInicial-self.sensorMagnetometro.getAnguloCabezaDron())
            time.sleep(.300)
        self.actuadorOP.setYaw(self.velocidadCeroGiroOP)

    # giro lateral de la cabeza a la izquierda desde la posicion donde esta
    def yaw_izquierda(self, grados, velocidad):
        self.yaw(-grados,velocidad)

    # giro lateral de la cabeza a la derecha desde la pocisión donde esta
    def yaw_derecha(self, grados, velocidad):
        self.yaw(grados,velocidad)

    # elevar el dron  distancia estara en centimetros y es la distancia que debe subir desde donde esta
    # velocidad para elevarse debe ser mayor a velocidadEstable y menor a velocidadMaxMotores
    # velocidad se sumara a la velocidad estable - hasta velocidadMaxMotores
    def up(self, distancia, velocidad):

        distanciaInicial=self.getDistancaSuelo()
        distanciaAlcanzada=distanciaInicial
        distanciaFinal=distanciaInicial+distancia

        # el throtle es la velocidad de los motores
        velocidad=self.velocidadEstable+velocidad
        if(velocidad>self.velocidadMaxMotores):
            velocidad=self.velocidadMaxMotores

        self.actuadorOP.setThrotle(velocidad)
        while (distanciaAlcanzada<distanciaFinal & velocidad>self.velocidadEstable):
             distanciaAlcanzada=self.getDistancaSuelo()
             time.sleep(.300)
        self.actuadorOP.setThrotle(velocidadEstable)

    # bajar el dron hasta "distancia" del piso. Estará en centimetros
    # velocidad tendría que ser menor a la estable si es mayor la dejo en velocidad estable
    def down(self, distancia, velocidad):
        if (velocidad>self.velocidadEstable):
            velocidad=velocidadEstable

        distanciaInicial=self.getDistanciaSuelo()
        distanciaAlcanzada=distanciaInicial
        distanciaFinal=distancia

        if (distanciaFinal<30):
            distanciaFinal=30

        self.actuadorOP.setThrotle(velocidad)
        while (distanciaAlcanzada>distanciaFinal & velocidad<self.velocidadEstable):
             distanciaAlcanzada=self.getDistanciaSuelo()
             time.sleep(.300)
        self.actuadorOP.setThrotle(velocidadEstable)

    # me devuelve la distancia del dron al suelo, si esta fuera del alcance del ultrasonido devuelve
    # distancia GPS. para ello se deberá setar 1ro distancia altitud suelo
    def getDistanciaSuelo(self):
        distanciaSuelo=self.sensorUltrasonido.getLastInfo()['altura']
        if (distanciaSuelo>=self.alcanceUltrasonido):
            distanciaSuelo=self.sensorGPS.getLastInfo()['altitud']*100-self.altitudSuelo
        return distanciaSuelo

    def aterrizar1(self):
        self.nivelarDron()
        self.down(30,self.velocidadEstable/2)
        self.down(10,self.velocidad10cm)
        self.down(5,self.velocidad5cm)
        self.apagar()

    def aterrizar2(self):
        distanciaInicial=self.getDistanciaSuelo()
        distanciaAlcanzada=distanciaInicial

        velocidad=velocidadEstable/2
        self.actuadorOP.setThrotle(velocidad)
        while (distanciaAlcanzada>40 ):
             distanciaAlcanzada=self.getDistanciaSuelo()
             time.sleep(.300)

        velocidad=velocidadEstable/3
        self.actuadorOP.setThrotle(velocidad)
        while (distanciaAlcanzada>10 ):
             distanciaAlcanzada=self.getDistanciaSuelo()
             time.sleep(.300)


        velocidad=self.velocidad10cm
        self.actuadorOP.setThrotle(velocidad)
        while (distanciaAlcanzada>5 ):
             distanciaAlcanzada=self.getDistanciaSuelo()
             time.sleep(.300)

        self.actuadorOP.setThrotle(self.velocidad5cm)
        time.sleep(.300)
        self.actuadorOP.setThrotle(self.velocidad5cm/2)
        self.apagar()

    # cabeceo - elevacion de la cabeza, es el giroscopio atributo Y
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

    # devuelve x y z (longitud, latitud y altura al suelo en cm) como una tupla
    def getCoordenadas(self):
        xyz=self.sensorGPS.getCoordenadas()
        x=xy['latitud']
        y=xy['longitud']
        z=self.getDistancaSuelo()
        return (x,y,z)

    # avanza el dron
    def irAdelante(self, velocidad):

        actuadorOP.irAdelante(velocidad)

    def nivelarDron(self):
        #hace que X e Y del giroscopio esten en 0
         raise NotImplementednError( "Should have implemented this" )



