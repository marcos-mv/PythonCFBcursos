class Carro:
    velMax = 0
    ligado = False
    cor = ""

c1 = Carro()
c2 = Carro()
c3 = Carro()

c1.velMax=160
c1.cor="Vermelho"
c1.ligado=False

c2.velMax=200
c2.cor="Azul"
c2.ligado=False

c3.velMax=150
c3.cor="Verde"
c3.ligado=True

Carro.cor = "Lilas"

print(c3.cor)

print("Velocidade Máxima: " + str(c1.velMax))
print("Cor do Veículo: " + str(c1.cor))

estado = "Sim" if c1.ligado else "Não"

print("Funcionando: " + estado +"\n")

print("Velocidade Máxima: " + str(c2.velMax))
print("Cor do Veículo: " + str(c2.cor))

estado = "Sim" if c2.ligado else "Não"

print("Funcionando: " + estado)


