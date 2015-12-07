from drivers.driver import Driver
from sensor import Sensor
from sensorDataGiroscopio import SensorDataGiroscopio
from datetime import *

__author__ = 'Diego Garcia'


class SensorGiroscopio(Sensor):

    def __init__(self, driver):
        """
        :type driver: Driver
        """

        self.sensorData = SensorDataGiroscopio(driver, datetime.today())
        self.status = driver.getStatus()
        self.driver = driver

    def getLastInfo(self):
        # devuelve la informacion que tiene sensorData
        last_info = self.sensorData
        self.sensorData.setData(self.driver.getData())
        self.sensorData.setAge(datetime.today())
        return last_info

    def getEstado(self):
        #devuelve el estado del sensor
        return self.status

    def reset(self):
        #inicializa el sensor
        self.driver.reset()

    def forceRead(self):
        #obliga a leer al sensor
        self.driver.forceRead()

    def verPosicion(self):
        """
        :return: una tupla con un vistaso de la posicion
        """
        data = self.sensorData.getData()
        return (data['x'], data['y'], data['z'])

    def verInclinacion(self):
        """
        :return: inclinacion x, inclinacion y
        """
        return (self.sensorData.getData()['inclinacion_x'], self.driver.getData()['inclinacion_y'])
