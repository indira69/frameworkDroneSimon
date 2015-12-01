from hal.actuadorOpenPilot import ActuadorOpenPilot

class ControladorDron(object):

    def __init__(self):
        self.actuador= ActuadorOpenPilot()
