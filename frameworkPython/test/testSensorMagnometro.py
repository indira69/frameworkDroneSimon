import unittest
from drivers.driver import Driver
from hal.sensorMagnometro import SensorMagnometro


data = {'angulo' : 120}
status = 'ok'

class DriverMagnometroMock(Driver):

    def __init__(self):

        self.data = data
        self.status = status

    def getData(self):

        return self.data

    def getStatus(self):

        return self.status

    def forceRead(self):

        raise NotImplementedError( "Should have implemented this" )

    def reset(self):

        raise NotImplementedError( "Should have implemented this" )

class SensorMagnometroTest(unittest.TestCase):

    def setUp(self):

        self.sensorMagnometro = SensorMagnometro(DriverMagnometroMock())

    def test_getLastInfo_NoNone(self):

        self.assertIsNotNone(self.sensorMagnometro.getLastInfo())

    def test_getEstado_NoNone(self):

        self.assertIsNotNone(self.sensorMagnometro.getEstado())

    def test_getAltura(self):

        self.assertEquals(self.sensorMagnometro.getAnguloCabezaDron(), data['angulo'])


