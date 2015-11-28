from drivers.driver import Driver
from actuador import Actuador
from actuadorDataMotor import ActuadorDataMotor

class ActuadorMotor(Actuador):

    def __init__(self, driver):
        """
        :type driver: Driver
        """

        self.actuadorData = ActuadorDataMotor(driver.getData())
        self.status = driver.getStatus()
        self.driver = driver

    def setData(self):

         raise NotImplementedError( "Should have implemented this" )

    def getStatus(self):

        return self.status

    def encender(self):
        #inicializa y pone en ON el actuador
         raise NotImplementedError( "Should have implemented this" )

    def apagar(self):
        # apaga el actuador
         raise NotImplementedError( "Should have implemented this" )