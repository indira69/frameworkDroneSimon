_autor_= "I.C.C."

import abc
#Abstract Base Class todo son objetos en python y derivan de abc

from abc import ABCMeta

class ControladorDron(object):
    __metaclass__ = ABCMeta

    # encender equivale a decir armar motores en OP
    @abc.abstractmethod
    def encender(self):
        # pone los datos que viene en forma de diccionario de la capa controlador Dron
        raise NotImplementedError( "Should have implemented this" )

    @abc.abstractmethod
    def apagar(self):
        # pone los datos que viene en forma de diccionario de la capa controlador Dron
        raise NotImplementedError( "Should have implemented this" )

    @abc.abstractmethod
    def apagar(self):
        # pone los datos que viene en forma de diccionario de la capa controlador Dron
        raise NotImplementedError( "Should have implemented this" )