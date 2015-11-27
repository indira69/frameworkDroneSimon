from sensorData import SensorData
from drivers.driver import Driver


class SensorDataUltrasonido(SensorData):

    def __init__(self, driver):
        """
        :type driver Driver
        """

        #data = {'altura' : 0}
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
