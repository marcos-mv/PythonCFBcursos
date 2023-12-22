class Carro:
    velMax = 0
    ligado = False
    cor = ""
    
    def __init__(self,vm,func,cor):
        self.velMax = vm
        self.ligado = func
        self.cor = cor
     
    def mostrar(self):   
        print("Velocidade Máxima: " + str(self.velMax))
        print("Cor do Veículo: " + str(self.cor))

        estado = "Sim" if self.ligado else "Não"

        print("Funcionando: " + estado +"\n")
        
    def ligar(self):
        self.ligado=True
        
    def desligar(self):
        self.ligado = False
        
    def andar(self):
        if self.ligado:
            print("Carro funcionando")
        else:
            print("Carro desligado!")
        
    


c1 = Carro(200, False, "Preto")
c2 = Carro(250, False, "Branco")
c3 = Carro(180, False, "Azul")

c1.ligar()

c1.mostrar()
c2.mostrar()
c3.mostrar()

c1.andar()
c2.andar()

c3.ligar()
c3.andar()



