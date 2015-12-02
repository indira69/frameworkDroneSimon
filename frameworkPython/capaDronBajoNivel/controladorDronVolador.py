_autor_= "I.C.C."

import abc
#Abstract Base Class todo son objetos en python y derivan de abc

from abc import ABCMeta
from controladorDron import ControladorDron

class ControladorDronVolador(ControladorDron):
    __metaclass__ = ABCMeta

   # giro lateral de la cabeza
    @abc.abstractmethod
    def yaw(self, grados):
        # pone los datos que viene en forma de diccionario de la capa controlador Dron
        raise NotImplementedError( "Should have implemented this" )

    # giro lateral de la cabeza a la izquierda
    @abc.abstractmethod
    def yaw_izquierda(self, grados):
        raise NotImplementedError( "Should have implemented this" )

    # giro lateral de la cabeza a la derecha
    @abc.abstractmethod
    def yaw_derecha(self, grados):
        raise NotImplementedError( "Should have implemented this" )

    # elevar el dron
    @abc.abstractmethod
    def up(self, distancia):
        raise NotImplementedError( "Should have implemented this" )

    # bajar el dron
    @abc.abstractmethod
    def down(self, distancia):
        raise NotImplementedError( "Should have implemented this" )

    # cabeceo - elevación de la cabeza
    @abc.abstractmethod
    def pitch_arriba(self, grados):
        raise NotImplementedError( "Should have implemented this" )

    # cabeceo - bajar la cabeza
    @abc.abstractmethod
    def pitch_abajo(self, grados):
        raise NotImplementedError( "Should have implemented this" )

    # giro lateral de costado a la derecha
    @abc.abstractmethod
    def roll_derecha(self, grados):
        raise NotImplementedError( "Should have implemented this" )

    # giro lateral de costado a la izquierda
    @abc.abstractmethod
    def roll_izquierda(self, grados):
        raise NotImplementedError( "Should have implemented this" )
