# tipos de variavel

x = 1
x = "Marcos"
x = 15.6
x = True

n1 = 5
n2 = 3

x = complex(n1, n2)

nomes = ["Marcos", "Vinicius", "Maria", 1, 58.3, True]  # array

nomes = ("Marcos", "Vinicius", "Maria", 1, 58.3, True)  # tupla

lista = range(0, 100, 1)

print(lista)

y = {
    "Nome": "Marcos",
    "Idade": 30,
    "Cidade": "Brasilia"
}

print(y, type(y))

z = {1, 1, 1, 5, 5, 8, 9, 5}  # set

zf = frozenset(z)

print(z, type(z))

print(zf, type(zf))


print(x.imag)

print(x.real)

print("Valor: " + str(x))

print("Tipo: " + str(type(x)))


print(nomes)

print(nomes[1])

for i in nomes:
    print(i)
