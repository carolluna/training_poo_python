class Conta:
    def __init__(self, numero, titular, saldo, limite):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite

    def extrato(self):
        print(f"O saldo do {self.titular} é de {self.saldo} reais")
        
    def deposita(self, valor):
        self.saldo += valor


    