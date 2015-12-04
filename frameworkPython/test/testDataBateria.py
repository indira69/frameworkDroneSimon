import unittest
from drivers.driver import Driver
from hal.sensorDataBateria import SensorDataBateria


data = {'nivel': 40}

class DriverBateriaMock(Driver):

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


class SensorDataBateriaTest(unittest.TestCase):

    def setUp(self):

        self.dataBateria = SensorDataBateria(DriverBateriaMock())

    def test_getData_NoNone(self):

        self.assertIsNotNone(self.dataBateria.getData())

    def test_getData(self):

        self.assertEquals(self.dataBateria.getData(), data)

    def test_setData(self):

        dataBateria = self.dataBateria
        new_data = {'nivel': 50}
        dataBateria.setData(new_data)
        self.assertEquals(dataBateria.getData(), new_data)

    def test_getAge(self):

        self.assertIsNotNone(self.dataBateria.getData())

    def test_setAge(self):

        dataBateria = self.dataBateria
        new_age = 'new age'
        dataBateria.setAge(new_age)
        self.assertEquals(dataBateria.getAge(), new_age)