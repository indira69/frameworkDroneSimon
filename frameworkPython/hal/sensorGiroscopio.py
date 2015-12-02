from drivers.driver import Driver
from sensor import Sensor
from sensorDataGiroscopio import SensorDataGiroscopio

__author__ = 'Diego Garcia'


class SensorGiroscopio(Sensor):

    def __init__(self, driver):
        """
        :type driver: Driver
        """

        self.data = SensorDataGiroscopio(driver)
        self.status = driver.getStatus()
        self.driver=driver

    def getLastInfo(self):
        # devuelve la informacion que tiene sensorData
        return self.data

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
        data = self.data.getData()
        return (data['x'], data['y'], data['z'])

    def verInclinacion(self):
        """
        :return: angulo
        """
        return self.data.getData()['angulo']
