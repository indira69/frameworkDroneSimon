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
        self.controladorDron = ControladorDron()
        self.encendido=False
        self.modo=None
        self.puntoPartida=self.controladorDron.getCoordenadas()
        self.posicionActual=self.controladorDron.getCoordenadas()

    def volver(self):
        self.irA(self.puntoPartida)

    #calcula la distancia euclideana entre dos puntos
    def distancia3d(self,p1,p2):
        return distance.euclidean(p1,p2)
        #a = (1,2,3)
        #b = (4,5,6)
        #dst =

    @abc.abstractmethod
    # dirige la cabeza al punto XYZ, que es un diccionario con x,y,z
    def mirarA(self, puntoXYZ):
        raise NotImplementedError( "Should have implemented this" )

    # En el caso del Open Pilot la velocidad 0-30 aproximadamente
    #  dependerá en cuanto se calibró la velocidad de estable
    def irA(self, puntoDestino, velocidad):
        distancia = distance.euclidean(self.posicionActual, puntoDestino)
        self.mirarA(puntoDestino)
        self.controladorDron.irAdelante(velocidad)
        direccionX=1
        if (self.posiciónActual['x']>puntoDestino['x']):
            direccionX=-1

        direccionY=1
        if (self.posiciónActual['y']>puntoDestino['y']):
            direccionY=-1


        while (True):
            a=1

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





