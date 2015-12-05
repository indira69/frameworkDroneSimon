import abc
#Abstract Base Class todo son objetos en python y derivan de abc

from abc import ABCMeta
from capaDronBajoNivel.controladorDron import ControladorDron
from capaDronBajoNivel.controladorDronVolador import ControladorDronVolador


from dron import Dron
from scipy.spatial import distance


class DronVolador (Dron):
    __metaclass__ = ABCMeta

    def __init__(self,controladorDronVolador):
        """
        :type controladorDronVolador: ControladorDronVolador
        """
        # inicializa
        Dron.__init__(controladorDronVolador)

    @abc.abstractmethod
    def aterrizar(self):
        raise NotImplementedError( "Should have implemented this" )

    @abc.abstractmethod
    def orbitar(self,centro, radio):
        raise NotImplementedError( "Should have implemented this" )

    @abc.abstractmethod
    def bajar(self, distancia):
        raise NotImplementedError( "Should have implemented this" )

    @abc.abstractmethod
    def sobrevolar(self, listaPuntos3D):
        raise NotImplementedError( "Should have implemented this" )

    @abc.abstractmethod
    def subir(self, distancia):
        raise NotImplementedError( "Should have implemented this" )


