import unittest
from drivers.driver import Driver
from hal.sensorDataMagnometro import SensorDataMagnometro


data = {'angulo': 90}

class DriverMagnometroMock(Driver):

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


class SensorDataMagnometroTest(unittest.TestCase):

    def setUp(self):

        self.dataMagnometro = SensorDataMagnometro(DriverMagnometroMock())

    def test_getData_NoNone(self):

        self.assertIsNotNone(self.dataMagnometro.getData())

    def test_getData(self):

        self.assertEquals(self.dataMagnometro.getData(), data)

    def test_setData(self):

        dataMagnometro = self.dataMagnometro
        new_data = {'altura': 50}
        dataMagnometro.setData(new_data)
        self.assertEquals(dataMagnometro.getData(), new_data)

    def test_getAge(self):

        self.assertIsNotNone(self.dataMagnometro.getData())

    def test_setAge(self):

        dataMagnometro = self.dataMagnometro
        new_age = 'new age'
        dataMagnometro.setAge(new_age)
        self.assertEquals(dataMagnometro.getAge(), new_age)