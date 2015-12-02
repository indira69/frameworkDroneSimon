from drivers.driver import Driver
from sensorData import SensorData

__author__ = 'Diego Garcia'


class SensorDataMagnometro(SensorData):

    def __init__(self, driver):
        """
        :type driver Driver
        """

        #data = {angulo : 0}
        self.data = driver.getData()
        self.age = ""

    def getData(self):

        return self.data

    def getAge(self):

        return self.age

    def setData(self, data):

        self.data = data

    def setAge(self, age):

        self.age = age

