# lista_carros=["Gol", "Palio", "Fox"]

# Tuplas não podem ter seus valores modificados a não ser via a realização de um typecast para uma lista
tupla_carros = ("Gol", "Palio", "Saveiro")

lista_carros = list(tupla_carros)

lista_carros[2] = "Fox"

tupla_carros = tuple(lista_carros)

for i in tupla_carros:
    print(i)
