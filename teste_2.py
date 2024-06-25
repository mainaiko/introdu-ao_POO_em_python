class Cachorro:
    def __init__(self, nome,cor,acordado=True):
        print ("Inicializando classe Cachorro")
        self.nome = nome
        self.cor = cor
        self.acordado = acordado
    def __del__(self):
        print("Removendo instancia da classe")
    def falar(self):
        print("auuuuu")

c = Cachorro("Luke", "pardo")
c.falar()