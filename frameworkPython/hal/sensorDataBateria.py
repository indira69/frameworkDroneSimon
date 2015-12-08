from sensorData import SensorData
from drivers.driver import Driver

__author__ = 'Diego Garcia'


class SensorDataBateria(SensorData):

    def __init__(self, driver, age):
        """
        :type driver Driver
        """
        #sensorData = {'nivel': 0}
        self.data = driver.getData()
        self.age = age

    def getData(self):
        return self.data

    def getAge(self):
        return self.age

    def setData(self, data):
        self.data = data

    def setAge(self, age):
        self.age = age