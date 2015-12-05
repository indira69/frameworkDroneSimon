from drivers.driver import Driver
from sensorData import SensorData

__author__ = 'Diego Garcia'


class SensorDataGPS(SensorData):

    def __init__(self, driverGPS):
        """
        :type driverGPS Driver
        """

        #data = {'latitud : 0, longitud : 0, altura : 0, velocidad'}
        self.data = driverGPS.getData()
        self.age = ""

    def getData(self):
        return self.data

    def getAge(self):
        return self.age

    def setData(self, data):
        self.data = data

    def setAge(self, age):
        self.age = age