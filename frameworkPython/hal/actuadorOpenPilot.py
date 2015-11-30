# coding=utf-8
_autor_ = "Jorge Encinas"
# modificado por Indira Camacho

from frameworkPython.drivers.driverCanalPWM import CanalPWM
from time import sleep
from actuadorDataOpenPilot import ActuadorDataOpenPilot

# que es duty?, vla max val min deverian ser cttes?
class ActuadorOpenPilot:
    """control PWM para 6 canales en Modo 2"""

    def __init__(self):
        self.pwm1 = 16  # 36 # aleron - roll
        self.pwm2 = 20  # 38 # elevador - pitch
        self.pwm3 = 21  # 40 # acelerador - tortle
        self.pwm4 = 13  # 33 # timon - yaw
        self.pwm5 = 19  # 35 # aux 1
        self.pwm6 = 26  # 37 # aux 2
        self.freq = 55  # frecuencia
        self.valMaximo = 10.6  # duty max
        self.valMinimo = 5.1  # duty min
        self.defecto = (self.valMaximo - self.valMinimo) / 2 + self.valMinimo  # 50% entre el max y el min
        self.canal1 = CanalPWM(self.pwm1, self.freq, self.valMinimo, self.valMaximo, self.defecto)
        self.canal2 = CanalPWM(self.pwm2, self.freq, self.valMinimo, self.valMaximo, self.defecto)
        self.canal3 = CanalPWM(self.pwm3, self.freq, self.valMinimo, self.valMaximo, self.valMinimo)
        self.canal4 = CanalPWM(self.pwm4, self.freq, self.valMinimo, self.valMaximo, self.defecto)
        self.canal5 = CanalPWM(self.pwm5, self.freq, self.valMinimo, self.valMaximo, self.valMinimo)
        self.canal6 = CanalPWM(self.pwm6, self.freq, self.valMinimo, self.valMaximo, self.valMinimo)
        self.diccionarioData={'roll':self.getRoll(), 'pitch':self.getPitch(),'tortle':self.getTortle(),'yaw':self.getYaw(),'modoVuelo':self.getModoVuelo(),'prendidoApagado':self.getOnOff()}
        self.data= ActuadorDataOpenPilot(self.diccionarioData)



   #reset : reinicia comunicacion con canales y ajusta valores de canales a su estado inicial
    def reset(self):
        self.interrumpir()
        self.canal1.inicio()
        self.canal2.inicio()
        self.canal3.inicio()
        self.canal4.inicio()
        self.canal5.inicio()
        self.canal6.inicio()

    # solo resetea valores sin reinniciar comunicación
    def resetearValores(self):
        self.setAleron(50)
        self.setElevador(50)
        self.setAcelerador(0)
        self.setTimon(50)
        self.setAux1(0)
        self.setAux2(0)
    """ uso para except KeyboardInterrupt o similares"""

    #stop: detiene todos los impulsos, seniales y desconecta el OP
    def stop(self):
        self.canal1.interrumpir()
        self.canal2.interrumpir()
        self.canal3.interrumpir()
        self.canal4.interrumpir()
        self.canal5.interrumpir()
        self.canal6.interrumpir()

    #roll- Aleron: inclinacion derecha e izquierda
    def setRoll(self, vel):
        self.canal1.setDuty(vel)

    #pitch - elevador - cabeceo: inclinacion cabeza arriba/abajo
    def setPitch(self, vel):
        self.canal2.setDuty(vel)

    #tortle - Acelerador : potencia, la direccion en la que va, depende de angulo de inclinacion del dron
    def setTortle(self, vel):
        self.canal3.setDuty(vel)

    #yaw- Timon: giro de cabeza a derecha o izquierda
    def setYaw(self, vel):
        self.canal4.setDuty(vel)

    #seleccionar modos de vuelo - estabilizado - acrobático, tiene hasta 6 opciones como: rate (ratios) y otros
    def setModoVuelo(self, modo):
        self.canal5.setDuty(modo)

    # armar y desarmar (encender y apagar)-  armado cuando el motor esta listo para arrancar (acelerar)
    # desarmado es cuando esta esperando ser armado, no arranca
    def setOnOff(self, onOff):
        self.canal6.setDuty(onOff)

    def encender(self):
        self.setOnOff(1)

    def apagar(self):
        self.setOnOff(0)

    # roll- Aleron inclinacion derecha e izquierda
    def getRoll(self):
        return self.canal1.valor

    # pitch - elevador - cabeceo: inclinacion cabeza arriba/abajo
    def getPitch(self):
        return self.canal2.valor

    # tortle - Acelerador : potencia, la direccion en la que va, depende de angulo de inclinacion del dron
    def getTortle(self):
        return self.canal3.valor

   # yaw- Timon: giro de cabeza a derecha o izquierda
    def getYaw(self):
        return self.canal4.valor

    # devuelve estabilizado o acrobatico
    def getModoVuelo(self):
        return self.canal5.valor

    # armar y desarmar (encender y apagar)-  armado cuando el motor esta listo para arrancar (acelerar)
    # desarmado es cuando esta esperando ser armado, no arranca
    # devuelve 0 o 1 dependiendo 0-apagado 1-prendido
    def getOnOff(self):
        return self.canal6.valor

    def testCanal(self):
        for i in range(50, 100):
            self.setAleron(i)
            self.setElevador(i)
            self.setAcelerador(i)
            self.setTimon(i)
            self.setAux1(i)
            self.setAux2(i)
            sleep(0.05)
            print i
        for i in range(100, 0, -1):
            self.setAleron(i)
            self.setElevador(i)
            self.setAcelerador(i)
            self.setTimon(i)
            self.setAux1(i)
            self.setAux2(i)
            sleep(0.05)
            print i
        self.resetearValores()

    #data = {'roll':0,  'pitch':0, 'tortle':0,'yaw':0, 'modoVuelo':estabilizado/acrobatico/ rate (ratios. hasta 6), 'prendido':si/no}
    def setData(self, data):
        self.data.setData(data)

    def getData(self):
        return self.data.getData()

