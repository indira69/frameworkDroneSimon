from drivers.driver import Driver
from sensor import Sensor
from sensorDataBateria import SensorDataBateria

<<<<<<< HEAD
#modified by Diego Garcia

=======
>>>>>>> 583f7e9fd353d1bf8100cf47c3730aa5c738e858
class SensorBateria(Sensor):

    def __init__(self, driver):
        self.sensorData = SensorDataBateria(driver)
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

    def getNivel(self):
        return self.sensorData.getData()['nivel']