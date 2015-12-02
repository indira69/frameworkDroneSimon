from drivers.driver import Driver
from sensor import Sensor
from sensorDataMagnometro import SensorDataMagnometro

__author__ = 'Diego Garcia'

<<<<<<< HEAD

=======
>>>>>>> 583f7e9fd353d1bf8100cf47c3730aa5c738e858
class SensorMagnometro(Sensor):

    def __init__(self, driver):
        """
        :type driver Driver
        """

        self.sensorData = SensorDataMagnometro(driver)
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