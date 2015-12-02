import unittest
from drivers.driver import Driver
from hal.sensorDataUltrasonido import SensorDataUltrasonido


data = {'altura': 200}

class DriverUltrasonidoMock(Driver):

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


class SensorDataUltrasonidoTest(unittest.TestCase):

    def setUp(self):

        self.dataUltrasonido = SensorDataUltrasonido(DriverUltrasonidoMock())

    def test_getData_NoNone(self):

        self.assertIsNotNone(self.dataUltrasonido.getData())

    def test_getData(self):

        self.assertEquals(self.dataUltrasonido.getData(), data)

    def test_setData(self):

        dataUltrasonido = self.dataUltrasonido
        new_data = {'altura': 50}
        dataUltrasonido.setData(new_data)
        self.assertEquals(dataUltrasonido.getData(), new_data)

    def test_getAge(self):

        self.assertIsNotNone(self.dataUltrasonido.getData())

    def test_setAge(self):

        dataUltrasonido = self.dataUltrasonido
        new_age = 'new age'
        dataUltrasonido.setAge(new_age)
        self.assertEquals(dataUltrasonido.getAge(), new_age)