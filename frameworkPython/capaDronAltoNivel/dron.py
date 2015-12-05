import abc
# Abstract Base Class todo son objetos en python y derivan de abc

from abc import ABCMeta
from capaDronBajoNivel.controladorDron import ControladorDron
from scipy.spatial import distance


class Dron (object):
    __metaclass__ = ABCMeta

    def __init__(self,controladorDron):
        """
        :type controladorDron: ControladorDron
        """
        # Este es un controlador con funciones de nivel intermedio en la comunicación del dron
        self.controladorDron = controladorDron
        self.encendido=False
        self.modo=None
        self.puntoPartida=self.controladorDron.getCoordenadas()
        self.posicionActual=self.controladorDron.getCoordenadas()

    def volver(self):
        self.ir(self.puntoPartida)

    #calcula la distancia euclideana entre dos puntos
    def distancia3d(self,p1,p2):
        return distance.euclidean(p1,p2)
        #a = (1,2,3)
        #b = (4,5,6)
        #dst =

    @abc.abstractmethod
    # dirige la cabeza al punto XYZ
    def mirarA(self, puntoXYZ):
        raise NotImplementedError( "Should have implemented this" )

    def ir(self,puntoDestino):
        distancia = distance.euclidean(self.posicionActual, puntoDestino)
        self.mirarA(puntoDestino)
        self.ir(puntoDestino)

    def encender(self):
        self.controladorDron.encender()

    def apagar(self):
        self.controladorDron.apagar()

    # devuelve la posición x,y,z del dron donde z es la altura del piso
    def getPosicion(self):
        self.posicionActual=self.controladorDron.getCoordenadas()
        return self.posicionActual

    def actualizarPuntoPartida(self):
        self.posicionActual=self.controladorDron.getCoordenadas()
        self.puntoPartida=self.posicionActual
        return self.puntoPartida





