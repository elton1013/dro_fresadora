from serial import Serial
from math import isclose

class Sensor:
    SENSOR_DISTANCIA_ERRO = 100

    def sensorSetUP(self):
        self.serial = Serial(port='/dev/serial0', baudrate=9600, timeout=0.05)
        self.getXY()
        self.leitura_anterior = self.leitura


    def getXY(self):
        self.serial.write(b'1')
        try:
            self.leitura = [int(x) for x in self.serial.readline().split()]
            return
        except:
            self.callAlerta('Erro na comunicação.')

        self.leitura = [0, 0]


    def ler(self):
        self.getXY()

        if not all((isclose(self.leitura_anterior[0], self.leitura[0], abs_tol=self.SENSOR_DISTANCIA_ERRO),
                    isclose(self.leitura_anterior[1], self.leitura[1], abs_tol=self.SENSOR_DISTANCIA_ERRO))):
            self.callAlerta('Possivel falha do sensor!\nConfira o ponto de origem.')

        self.leitura_anterior = self.leitura
        
