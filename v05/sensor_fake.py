from math import isclose


class Sensor:
    SENSOR_DISTANCIA_ERRO = 10

    def sensorSetUP(self):
        self.range = iter(range(400, 4000, 1))
        self.getXY()
        self.leitura_anterior = self.leitura


    def getXY(self):
        x = y = next(self.range)
        self.leitura =  x, y


    def ler(self):
        self.getXY()
        if not self.leitura:
            self.leitura = [0, 0]

        if not all((isclose(self.leitura_anterior[0], self.leitura[0], abs_tol=self.SENSOR_DISTANCIA_ERRO),
                   isclose(self.leitura_anterior[1], self.leitura[1], abs_tol=self.SENSOR_DISTANCIA_ERRO))):
            self.callAlerta()

        self.leitura_anterior = self.leitura


