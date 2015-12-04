import unittest
from drivers.driver import Driver
from hal.sensorDataGPS import SensorDataGPS


data = {'latitud': 543, 'longitud': 345, 'altura': 656}

class DriverGPSMock(Driver):

    def __init__(self):

        self.data = data

    def getData(self):

        return self.data

    def getStatus(self):

        raise  NotImplementedError( "Should have implemented this")

    def forceRead(self):

        raise NotImplementedError( "Should have implemented this" )

    def reset(self):

        raise NotImplementedError( "Should have implemented this" )


class SensorDataGPSTest(unittest.TestCase):

    def setUp(self):

        self.dataGPS = SensorDataGPS(DriverGPSMock())

    def test_getData_NoNone(self):

        self.assertIsNotNone(self.dataGPS.getData())

    def test_getData_Latitud(self):

        self.assertEquals(self.dataGPS.getData()['latitud'], data['latitud'])

    def test_getData_Longitud(self):

        self.assertEquals(self.dataGPS.getData()['longitud'], data['longitud'])

    def test_getData_altura(self):

        self.assertEquals(self.dataGPS.getData()['altura'], data['altura'])

    def test_getData(self):

        self.assertEquals(self.dataGPS.getData(), data)

    def test_setData(self):

        dataGPS = self.dataGPS
        new_data = {'latitud': 234, 'longitud': 178, 'altura': 756}
        dataGPS.setData(new_data)
        self.assertEquals(dataGPS.getData(), new_data)


    def test_getAge(self):

        self.assertIsNotNone(self.dataGPS.getData())

    def test_setAge(self):

        dataGPS = self.dataGPS
        new_age = 'new age'
        dataGPS.setAge(new_age)
        self.assertEquals(dataGPS.getAge(), new_age)