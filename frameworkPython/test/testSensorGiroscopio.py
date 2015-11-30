import unittest
from drivers.driver import Driver
from hal.sensorGiroscopio import SensorGiroscopio


data = {'x': 1, 'y': 6, 'z': 3, 'angulo' : 90}
status = 'ok'

class DriverGiroscopioMock(Driver):

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

class SensorGPSTest(unittest.TestCase):

    def setUp(self):

        self.sensorGiroscopio = SensorGiroscopio(DriverGiroscopioMock())

    def test_getLastInfo_NoNone(self):

        self.assertIsNotNone(self.sensorGiroscopio.getLastInfo())

    def test_getEstado_NoNone(self):

        self.assertIsNotNone(self.sensorGiroscopio.getEstado())

    def test_verPosicion_NoNone(self):

        self.assertIsNotNone(self.sensorGiroscopio.verPosicion())

    def test_verPosicion(self):

        sensorGiroscopio = self.sensorGiroscopio
        esperado = (data['x'], data['y'], data['z'])
        self.assertEquals(sensorGiroscopio.verPosicion(), esperado)

    def test_verInclinacion_NoNone(self):

        self.assertIsNotNone(self.sensorGiroscopio.verInclinacion())

    def test_verInclinacion(self):

        sensorGiroscopio = self.sensorGiroscopio
        esperado = data['angulo']
        self.assertEquals(sensorGiroscopio.verInclinacion(), esperado)


