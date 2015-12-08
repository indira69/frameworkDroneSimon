_autor_= "I.C.C."

import abc
#Abstract Base Class todo son objetos en python y derivan de abc

from abc import ABCMeta

class ControladorDron(object):
    __metaclass__ = ABCMeta

    # encender equivale a decir armar motores en OP
    @abc.abstractmethod
    def encender(self):
        raise NotImplementedError( "Should have implemented this" )

    @abc.abstractmethod
    def apagar(self):
        raise NotImplementedError( "Should have implemented this" )

    @abc.abstractmethod
    def getStatus(self):
         raise NotImplementedError( "Should have implemented this" )

    @abc.abstractmethod
    def getAnguloCabeza(self):
        raise NotImplementedError( "Should have implemented this" )

    @abc.abstractmethod
    def getCoordenadas(self):
        raise NotImplementedError( "Should have implemented this" )

    @abc.abstractmethod
    def irAdelante(self):
        raise NotImplementedError( "Should have implemented this" )

    @abc.abstractmethod
    def setModo(self):
        raise NotImplementedError( "Should have implemented this" )