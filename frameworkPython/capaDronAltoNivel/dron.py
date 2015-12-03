import abc
#Abstract Base Class todo son objetos en python y derivan de abc

from abc import ABCMeta
from capaDronBajoNivel import ControladorDronMulticoptero

class Dron (object):
    __metaclass__ = ABCMeta

    def __init__(self,ControladorDronMulticoptero):
        """
        :type controladorDron: Driver
        """

        # este sera un diccionario
        self.controladorDron = ControladorDronMulticoptero()
        #self.status = None
        #self.driver = None

    @abc.abstractmethod
    def apagar(self):
        # pone los datos que viene en forma de diccionario de la capa controlador Dron
        raise NotImplementedError( "Should have implemented this" )
