class Conta:
    def __init__(self, titular):
        self.titular = titular
        self.__saldo = 0

    def extrato(self):
        print("O saldo é {}".format(self.__saldo))

    def deposita(self, valor):
        self.__saldo += valor

    def saca(self, valor):
        self.__saldo += valor


    def saldo(self):
        return self.__saldo

