carro = {"Fabricante": "Honda",
         "Modelo": "City",
         "Ano": 2023,
         "Cor": "Vermelho"}

fab = carro.get("Fabricante")

fabr = carro["Fabricante"]

print(fab)

print(fabr)

carro["Cor"] = "rosa"
print(carro.get("Cor"))

print("Tamanho do Dictionary: " + str(len(carro)))

carro["Categoria"] = "Passeio"

if "Cor" in carro:
    print("Sim a cor é uma chave")


for i, j in carro.items():
    print(i + ":" + str(j))

print("Tamanho do Dictionary: " + str(len(carro)))

carro.pop("Categoria") # del carro["Categoria"]

carro.clear()