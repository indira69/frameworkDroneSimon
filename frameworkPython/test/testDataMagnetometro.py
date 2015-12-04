import unittest
from drivers.driver import Driver
from hal.sensorDataMagnetometro import SensorDataMagnetrometro


data = {'angulo': 90}

class DriverMagnetometroMock(Driver):

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


class SensorDataMagnetometroTest(unittest.TestCase):

    def setUp(self):

        self.dataMagnometro = SensorDataMagnetrometro(DriverMagnetometroMock())

    def test_getData_NoNone(self):

        self.assertIsNotNone(self.dataMagnometro.getData())

    def test_getData(self):

        self.assertEquals(self.dataMagnometro.getData(), data)

    def test_setData(self):

        dataMagnetometro = self.dataMagnometro
        new_data = {'altura': 50}
        dataMagnetometro.setData(new_data)
        self.assertEquals(dataMagnetometro.getData(), new_data)

    def test_getAge(self):

        self.assertIsNotNone(self.dataMagnometro.getData())

    def test_setAge(self):

        dataMagnetometro = self.dataMagnometro
        new_age = 'new age'
        dataMagnetometro.setAge(new_age)
        self.assertEquals(dataMagnetometro.getAge(), new_age)