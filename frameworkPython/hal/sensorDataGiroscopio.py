from sensorData import SensorData
from drivers.driver import Driver

from datetime import *


__author__ = 'Diego Garcia'


class SensorDataGiroscopio(SensorData):

    def __init__(self, driver):
        """
        :type driver Driver
        """

        #data = {'x': 0, 'y': 0, 'z': 0, 'angulo': 0}
        self.data = driver.getData()
        self.age = datetime.today()

    def getData(self):
        # tiene los datos del sensor
        self.data.getData()
        self.age = datetime.today()
        return self.data

    def getAge(self):
        # tiene los datos del sensor
        return self.age

    def setData(self, data):

        self.data = data

    def setAge(self, age):

        self.age = age