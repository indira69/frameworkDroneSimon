from drivers.driver import Driver
from sensorData import SensorData

__author__ = 'Diego Garcia'


class SensorDataGPS(SensorData):

    def __init__(self, driverGPS):
        """
        :type driverGPS Driver
        """

        # sensorData es un diccionario sensorData = {'latitud : 0, longitud : 0, altitud:0'}
        self.data = driverGPS.getData()
        self.age = "No age"

    def getData(self):
        self.data= self.driverGPS.getLastInfo()
        return self.data

    def getAge(self):
        return self.age

    def setData(self, data):
        self.data = data

    def setAge(self, age):
        self.age = age