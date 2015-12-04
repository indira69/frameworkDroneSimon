from drivers.driver import Driver
from sensor import Sensor
from sensorDataMagnetometro import SensorDataMagnetometro

__author__ = 'Diego Garcia'


class SensorMagnetometro(Sensor):

    def __init__(self, driver):
        """
        :type driver Driver
        """

        self.sensorData = SensorDataMagnetometro(driver)
        self.status = driver.getStatus()
        self.driver = driver

    def getLastInfo(self):

        return self.sensorData

    def getEstado(self):

        return self.status

    def reset(self):

        self.driver.reset()

    def forceRead(self):

        self.driver.forceRead()

    def getAnguloCabezaDron(self):

        return self.sensorData.getData()['angulo']