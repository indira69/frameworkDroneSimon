import unittest
from drivers.driver import Driver
from hal.sensorDataGiroscopio import SensorDataGiroscopio


data = {'x': 1, 'y': 6, 'z': 3, 'angulo' : 90}

class DriverGiroscoioMock(Driver):

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

        self.dataGPS = SensorDataGiroscopio(DriverGiroscoioMock())

    def test_getData_NoNone(self):

        self.assertIsNotNone(self.dataGPS.getData())

    def test_getData_X(self):

        self.assertEquals(self.dataGPS.getData()['x'], data['x'])

    def test_getData_Y(self):

        self.assertEquals(self.dataGPS.getData()['y'], data['y'])

    def test_getData_Z(self):

        self.assertEquals(self.dataGPS.getData()['z'], data['z'])

    def test_getData_Angulo(self):

        self.assertEquals(self.dataGPS.getData()['angulo'], data['angulo'])

    def test_getData(self):

        self.assertEquals(self.dataGPS.getData(), data)

    def test_setData(self):

        dataGPS = self.dataGPS
        new_data = {'x': 4, 'y': 7, 'z': 6, 'angulo' : 50}
        dataGPS.setData(new_data)
        self.assertEquals(dataGPS.getData(), new_data)

    def test_setAge(self):

        dataGPS = self.dataGPS
        new_age = 'new age'
        dataGPS.setAge(new_age)
        self.assertEquals(dataGPS.getAge(), new_age)