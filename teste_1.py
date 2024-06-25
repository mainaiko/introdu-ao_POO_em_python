class bicicleta:
    def __init__(self, cor,modelo,ano,valor):
        self.cor=cor
        self.modelo=modelo
        self.ano=ano
        self.valor=valor #atributos da classe
    def buzinar(self): #comportamentos sao definidos por metodos
        print("BIBI")
    def parar(self):
        print("parar")
    def correr(self):
        print("velocidade ok")

    # def __str__ (self):
    #     return f"Bicicleta: {self.cor}, {self.modelo}, {self.ano}, {self.valor}"
    def __str__(self):
        return f"{self.__class__.__name__}: {", ".join([f"{chave}={valor}"for chave,valor in self.__dict__.items()])}"



variavel = bicicleta("roxa", "bike", 2020, 1500)
#modelo de classe instanciada 

print(variavel)


