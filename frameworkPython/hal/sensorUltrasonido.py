from drivers.driver import Driver
from sensor import Sensor
from sensorDataUltrasonido import SensorDataUltrasonido

from datetime import *

__author__ = 'Diego Garcia'


class SensorUltrasonido(Sensor):

    def __init__(self, driver, alcance):
        """
        :type driver: Driver
        """

        self.data = SensorDataUltrasonido(driver)
        self.status = driver.getStatus()
        self.driver=driver
        self.alcance=alcance
        self.data.setAge(datetime.today())

    def getLastInfo(self):
        # devuelve la informacion que tiene sensorData
        self.data.setData(self.driver.getData())
        self.data.setAge(datetime.today())
        return self.data.getData()

    def getEstado(self):
        #devuelve el estado del sensor
        return self.status

    def reset(self):
        #inicializa el sensor
        self.driver.reset()

    def forceRead(self):
        #obliga a leer al sensor
        self.driver.forceRead()

    #
    def getAltura(self):

        return self.data.getData()['altura']
