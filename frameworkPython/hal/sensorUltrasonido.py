__author__ = 'Diego Garcia'
# modificado I.C.C

from drivers.driver import Driver
from sensor import Sensor
from sensorDataUltrasonido import SensorDataUltrasonido

from datetime import *

class SensorUltrasonido(Sensor):

    def __init__(self, driver, alcance):
        """
        :type driver: Driver
        """
        # age= datetime.today() guarda la fecha y la hora de la última lectura del sensor
        self.sensorData = SensorDataUltrasonido(driver.getData(), datetime.today())
        self.status = driver.getStatus()
        self.driver=driver
        self.alcance=alcance


    def getLastInfo(self):
        # devuelve la informacion que tiene sensorData, luego de leer el driver
        self.sensorData.setData(self.driver.getData())
        self.sensorData.setAge(datetime.today())
        return self.sensorData

    def getEstado(self):
        #devuelve el estado del sensor
        return self.status

    def reset(self):
        #inicializa el sensor
        self.driver.reset()

    def forceRead(self):
        #obliga a leer al sensor
        self.driver.forceRead()

    #al llamar driver.getData se obliga a leer al driver
    def getAltura(self):
        self.sensorData.setData(self.driver.getData())
        self.sensorData.setAge(datetime.today())
        return self.sensorData.getData()['altura']

    #devuelve el alcance máximo del ultrasonido si 0 es que esta en el piso
    # si está en el máximo puede estar mas de  el máximo
    def getAlcance(self):
        return self.alcance
