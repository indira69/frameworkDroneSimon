from drivers.driver import Driver
from sensor import Sensor
from sensorDataGPS import SensorDataGPS


class SensorGPS(Sensor):

    def __init__(self, driver):
        """
        :type driver Driver
        """

        self.sensorData = SensorDataGPS(driver)
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

    def getCoordenadas(self):

        data = self.sensorData.getData()
        return (data['latitud'], data['longitud'], data['altura'])