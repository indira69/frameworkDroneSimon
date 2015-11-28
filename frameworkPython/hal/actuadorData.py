import abc
from abc import ABCMeta

from drivers.driver import Driver

class ActuadorData(object):
    __metaclass__ = ABCMeta

    @abc.abstractmethod
    def setData(self,data):
        # pone los datos que debe manejar el actuador
         raise NotImplementedError( "Should have implemented this" )

    @abc.abstractmethod
    def getData(self):
        # recupera los datos del actuador
         raise NotImplementedError( "Should have implemented this" )

    @abc.abstractmethod
    def setStatus(self):
        # recupera el estado del actuador
         raise NotImplementedError( "Should have implemented this" )

