import os

os.system('clear')

# i = 0

# while i < 10:
#     print(i)
#     i += 1
    
    
# carros= ["Gol", "Palio", "Fox"]

# tam=len(carros)
# j=0

# while j < tam:
#     print (carros[j])
#     j+=1
    
    
carros=[]

carro = input("Digite o nome do novo carro:  ")

while carro != "-1":
    carros.append(carro)
    carro = input("Digite o nome do novo carro:  ")
    
os.system('clear')
    
for i in carros:
    print(i)
    
print(carros)