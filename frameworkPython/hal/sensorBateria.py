from drivers.driver import Driver
from sensor import Sensor
from sensorDataBateria import SensorDataBateria

class Bateria(Sensor):

    def __init__(self, driver):
        self.sensorData = SensorDataBateria(driver)
        self.status = driver.getStatus()
        self.driver

    def getLastInfo(self):
        return self.data

    def getEstado(self):
        return self.status

    def reset(self):
        self.driver.reset()

    def forceRead(self):
        self.driver.forceRead()